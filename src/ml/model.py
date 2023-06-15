import os

import pandas as pd
import numpy as np
from sklearn.preprocessing import OrdinalEncoder
from catboost import CatBoostClassifier
import pickle
from pickle import load
import joblib
from skmultilearn.model_selection import iterative_train_test_split 


MODEL_PATH = "C:\\pythons\\hack\\ml-model\\src\\ml\\"

def get_product_info(pid):
    p_data = {}
    
    return p_data


def predict(data):
    
    
    # Загрузка модели из файла - это понятно, внутри катбустер
    with open(MODEL_PATH+"model.pcl", "rb") as fid:
        tun_model = pickle.load(fid)
    
    # Преобразование словарей в датафреймы
    items = data["items"]
    manual = []
    items_ = items.copy()
    items = []
    if len(items)>3:
        for idx, x in enumerate(items_):
            if idx<3:
                items.append(x)
            else:
                manual.append(x)
    else:
        items = items_
    
    
    df = pd.DataFrame(items)
    df["orderId"] = data["orderId"]
    df = df[["orderId", "sku", "count", "size1", "size2", "size3", "weight", "type"]]
    numeric_columns = ["count", "size1", "size2", "size3", "weight"]
    df[numeric_columns] = df[numeric_columns].astype(float)

    # удалим часть информации о карготипах:
    df.drop(['type'], axis = 1, inplace = True)
    
    # Создаем новый признак:
    df['pack_volume'] = df['size1'] * df['size2'] * df['size3']

    # делаем агрегацию по уникальному заказу
    df_agg = df.groupby('orderId').agg({
    'pack_volume': 'mean',
    'weight': 'mean',
    'sku': 'count'
    }).reset_index() 
    
    df_agg.rename(columns={'sku': 'item_count'}, inplace=True)
    
    # сведения о товарах в заказе:
    order_agg = df.pivot_table(index='orderId', columns=df.groupby('orderId').cumcount()+1, aggfunc='first')
    order_agg.columns = [f'{col[0]}_{col[1]}' for col in order_agg.columns]
    order_agg = order_agg.reset_index()

    # Объединяем информацию о заказе
    df_new = df_agg.merge(order_agg, how='inner', on='orderId')

    df_new = add_missing_columns(df_new)

    # Удаляем лишние столбцы
    drop_list = ['orderId', 'sku_1', 'sku_2', 'sku_3']
    thisFilter = df.filter(drop_list)
    df_new.drop(thisFilter, inplace=True, axis=1)

    # ПРЕДСКАЗАНИЕ МОДЕЛИ
    y_pred = tun_model.predict_proba(df_new)

    # pаскодировка предсказания:
    encoder = joblib.load(MODEL_PATH+'model_encoder.pkl')
    predicted_labels = np.argmax(y_pred, axis=1)
    y_pred_norm = encoder.inverse_transform(predicted_labels.reshape(-1, 1))
    
    ###############
    response = {
      "orderId": '111',
      "package": '111',
      "items": [{"sku": "unique_sku_1", "add_packs":['aaa','bbb']}],
      "no_room_for": manual,
      "status": "ok"
    }
    ###############
    return response

# Создаем функцию, которая добавит все недостающие столбцы для обучения модели:
def add_missing_columns(df_new):
    all_columns = ['orderId', 'pack_volume', 'weight', 'item_count', 'count_1', 'count_2', 'count_3',
                   'pack_volume_1', 'pack_volume_2', 'pack_volume_3', 'size1_1', 'size1_2', 'size1_3',
                   'size2_1', 'size2_2', 'size2_3', 'size3_1', 'size3_2', 'size3_3', 'sku_1', 'sku_2', 'sku_3',
                   'weight_1', 'weight_2', 'weight_3']
    existing_columns = df_new.columns.tolist()
    missing_columns = list(set(all_columns) - set(existing_columns))
    for col in missing_columns:
        df_new[col] = 0
    df_new = df_new.reindex(columns=all_columns)
    return df_new 
