from http import HTTPStatus
from typing import Any

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from src.api.request_models import FullInfoRequest
from src.api.response_models import RecommendationResponse, HealthCheckResponse
from src.core.settings import settings
from src.ml.ml_model import make_recommendation


def create_app() -> FastAPI:
    app = FastAPI(debug=settings.DEBUG, root_path=settings.ML_ROOT_PATH)

    @app.get(
        "/health",
        response_model=HealthCheckResponse,
        status_code=HTTPStatus.OK,
        summary="Healthcheck",
        response_description=HTTPStatus.OK.phrase,
    )
    def healthcheck():
        return {"status": "ok"}

    @app.post(
        "/pack",
        response_model=RecommendationResponse,
        status_code=HTTPStatus.OK,
        response_description=HTTPStatus.OK.phrase,
    )
    def return_pack_recommendation(order_with_carton: FullInfoRequest) -> Any:
        try:
            result = make_recommendation(order_with_carton.dict())
        except Exception:
            return JSONResponse(
                status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
                content={
                    "orderId": str(order_with_carton.order.order_id),
                    "status": "fail",
                },
            )

        return result

    return app
