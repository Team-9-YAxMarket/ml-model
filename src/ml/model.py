import pandas as pd
import numpy as np
import pickle
import joblib
import requests

def predict(data):
    # Загрузка модели из файла на GitHub
    model_url = "https://github.com/Team-9-YAxMarket/ml-model/raw/main/src/ml/file_tun.pcl"
    response = requests.get(model_url)
    with open("file_tun.pcl", "wb") as file:
        file.write(response.content)
    tun_model = pickle.load(open("file_tun.pcl", "rb"))

    # Преобразование словарей в датафреймы
    items = data.get("items", [])
    if not items:
        return 'пустой список items'

    df = pd.DataFrame(items)
    df["orderId"] = data.get("orderId", "default_orderId")
    df = df[["orderId", "sku", "count", "size1", "size2", "size3", "weight", "type"]]
    numeric_columns = ["size1", "size2", "size3", "weight"]
    df[numeric_columns] = df[numeric_columns].astype(float)

    # Удаляем столбец "type"
    df.drop("type", axis=1, inplace=True)

    # Создаем новый признак:
    df['pack_volume'] = df['size1'] * df['size2'] * df['size3']

    # Делаем агрегацию по уникальному заказу
    df_agg = df.groupby('orderId').agg({
        'pack_volume': 'mean',
        'weight': 'mean',
        'sku': 'count'
    }).reset_index()

    df_agg.rename(columns={'sku': 'item_count'}, inplace=True)

    # Проверяем значение item_count и возвращаем соответствующий результат
    if df_agg['item_count'].max() > 3:
        return 'рекомендована ручная сборка'

    # Сведения о товарах в заказе:
    order_agg = df.pivot_table(index='orderId', columns=df.groupby('orderId').cumcount() + 1, aggfunc='first')
    order_agg.columns = [f'{col[0]}_{col[1]}' for col in order_agg.columns]
    order_agg = order_agg.reset_index()

    # Объединяем информацию о заказе
    df_new = df_agg.merge(order_agg, how='inner', on='orderId')

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

    df_new = add_missing_columns(df_new)

    # Удаляем лишние столбцы
    df_new.drop(['orderId', 'sku_1', 'sku_2', 'sku_3'], axis=1, inplace=True)

    # Загрузка энкодера из файла на GitHub
    encoder_url = "https://github.com/Team-9-YAxMarket/ml-model/raw/main/src/ml/encoder.pkl"
    response = requests.get(encoder_url)
    with open("encoder.pkl", "wb") as file:
        file.write(response.content)
    encoder = joblib.load(open("encoder.pkl", "rb"))

    # ПРЕДСКАЗАНИЕ МОДЕЛИ
    y_pred = tun_model.predict_proba(df_new)

    # Раскодировка предсказания:
    predicted_labels = np.argmax(y_pred, axis=1)
    y_pred_norm = encoder.inverse_transform(predicted_labels.reshape(-1, 1))

    return y_pred_norm[0, 0]