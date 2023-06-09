import pickle
from catboost import CatBoostClassifier
import numpy as np
from sklearn.preprocessing import LabelEncoder

def predict(x):
    # Загрузка модели из файла
    with open("file.pcl", "rb") as fid:
        loaded_model = pickle.load(fid)

    # Загрузка обученного LabelEncoder из модели
    label_encoder = loaded_model._le

    # Раскодирование предсказанных вероятностей
    y_pred_proba = loaded_model.predict_proba(x)
    y_pred = label_encoder.inverse_transform(np.argmax(y_pred_proba, axis=1))

    return y_pred