# Yandex Hackathon Team 9

##  Data Science разработчик
Олеся Зорич

## Инструкция по сборке
###### 
```
git clone git@github.com:Team-9-YAxMarket/ml-model.git
```
Установите виртуальное окружение и активируйте его
```
python -m venv venv
```
```
source venv/Scripts/activate
```
#### Установите зависимости
```
pip install -r requirements.txt
```
#### Запуск и тестирование:
Запуск локального сервера
```
python run.py
```
Переход к тестовым данным
```
cd src/ml
```
Запуск тестовых данных для проверки модели
```
python test.py
```

## Стек технологий, использованных в проекте


* python 3.9
* fastapi
* uvicorn
* pydantic
* pandas
* catboost
* joblib
* uvicorn
* scikit-learn 
* scikit-multilearn
## Links

[Сайт с проектом где используется модель развернут по ссылке](http://ivr.sytes.net:9009/)