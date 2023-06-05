from typing import Any


def make_recommendation(request: dict[Any]) -> dict[Any]:
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
