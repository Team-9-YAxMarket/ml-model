from fastapi import FastAPI

from src.api.request_models import Order
from src.api.response_models import HealthCheckResponse, PredictResponse
from src.core.settings import settings
from src.ml import model
from src.ml.model import predict


def create_app() -> FastAPI:
    app = FastAPI(debug=settings.DEBUG, root_path=settings.ML_ROOT_PATH)

    @app.get("/health/", response_model=HealthCheckResponse)
    def health():
        return {"status": "ok"}

    @app.post("/pack/", response_model=PredictResponse)
    def get_prediction(request: Order):
        order = dict(request)
        items = []
        for item in dict(request)["items"]:
            item = dict(item)
            items.append(item)

        try:
            result = predict({"orderId": "test_order", "items": items})
            order["package"] = result
            print("Модель успешно импортирована и вызвана.")
            return order
        except Exception as e:
            raise RuntimeError(
                "Ошибка при импорте модели или вызове функции predict:", str(e)
            )

    return app
