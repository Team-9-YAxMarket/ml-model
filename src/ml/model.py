from typing import Any


def predict(request: dict[Any]) -> dict[Any]:
    """Return ML prediction.

    request = {
        "order": {
            "order_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "items": [
                {
                    "sku": "unique_sku_1",
                    "size_1": 0.1, "size_2": 0.2, "size_3": 0.3,
                    "weight": 0.4,
                    "type": [0, 1, 2],
                },
                {
                    "sku": "unique_sku_2",
                    "size_1": 1.1, "size_2": 1.2, "size_3": 1.3,
                    "weight": 1.4,
                    "type": [4, 5],
                },
            ],
        },
        "carton_leftovers": [
            {"carton_type": "YMA", "amount": 34},
            {"carton_type": "YMC", "amount": 20},
            {"carton_type": "YMF", "amount": 30},
            {"carton_type": "KSD", "amount": 0},
            ...
        ],
    }
    """

    ...

    return {
        "order_id": request["order"]["order_id"],
        "packs": [
            {
                "packages": ["ABC", "DEF"],
                "items": [
                    {"sku": "unique_sku_1", "amount": 1},
                    {"sku": "unique_sku_2", "amount": 1},
                    {"sku": "unique_sku_3", "amount": 1},
                ],
            },
            {
                "packages": ["GHI", "JKL"],
                "items": [
                    {"sku": "unique_sku_2", "amount": 2},
                    {"sku": "unique_sku_3", "amount": 1},
                ],
            },
        ],
    }
