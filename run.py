from fastapi import FastAPI, Request
import uvicorn
import argparse

from src import create_app
from src.ml.model import predict

from src.api.request_models import Order

app = create_app()

if __name__ == "__main__":
    try:
        result = predict({"orderId": "test_order", "items": []})
        print("Модель успешно импортирована и вызвана.")
    except Exception as e:
        print("Ошибка при импорте модели или вызове функции predict:", str(e))

    parser = argparse.ArgumentParser()
    parser.add_argument("--port", default=8000, type=int, dest="port")
    parser.add_argument("--host", default="0.0.0.0", type=str, dest="host")
    args = vars(parser.parse_args())

    uvicorn.run(app, host=args['host'], port=args['port'])
