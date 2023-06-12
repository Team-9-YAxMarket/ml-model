import os

import pandas as pd
import numpy as np
import pickle
import joblib


def predict(data):

    # Загрузка модели из файла - это понятно, внутри катбустер
    with open("./src/ml/model.pcl", "rb") as fid:
        base_model = pickle.load(fid)

    # Преобразование словарей в датафреймы
    items = data["items"]
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

    # Объеденяем информацию о заказе
    df_new = df_agg.merge(order_agg, how='inner', on = 'orderId')
    df_new.drop(['orderId', 'sku_1', 'sku_2', 'sku_3'], axis=1, inplace=True)

    # ПРЕДСКАЗАНИЕ МОДЕЛИ
    y_pred = base_model.predict_proba(df_new)

    # заскодировка предсказания:
    encoder = joblib.load('model_encoder.pkl')
    predicted_labels = np.argmax(y_pred, axis=1)
    y_pred_norm = encoder.inverse_transform(predicted_labels.reshape(-1, 1))

    ###############
    response = {
      "orderId": data["orderId"],
      "package": y_pred_norm[0][0],
      "items": [
        {"sku": "unique_sku_1", "add_packs": ['пузырьки']},
        {"sku": "unique_sku_2", "add_packs": ['стекло','отдельная упаковка']},
        {"sku": "unique_sku_3", "add_packs": []},
      ],
      "no_room_for": [
        {"sku": "unique_sku_4", "add_packs": ['пузырьки']},
      ],
      "status": "ok"
    }
    ###############

    return response