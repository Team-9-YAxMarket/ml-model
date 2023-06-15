import requests

data = {
    "orderId": "12345",
    "items": [
    {"sku": "111", "count": 1, "size1": "5.1", "size2": "2.2", "size3": "5.3",
     "weight": "7.34", "type": ["2"]},
    {"sku": "222", "count": 3, "size1": "4", "size2": "5.23", "size3": "6.2",
     "weight": "7.45", "type": ["8", "9", "10"]},
    {"sku": "unique_sku_3", "count": 2, "size1": "11", "size2": "12.5", "size3": "13.3",
     "weight": "14.2", "type": ["15", "16"]}
    ]
}

r = requests.post("http://localhost:8080/pack", json=data)

print(r.json())
print()
print('*'*50)

data = {
    "orderId": "12345",
    "items": [
    {"sku": "111", "count": 1, "size1": "5.1", "size2": "2.2", "size3": "5.3",
     "weight": "7.34", "type": ["2"]}
    ]
}

r = requests.post("http://localhost:8080/pack", json=data)

print(r.json())
print()
print('*'*50)
      

data = {
    "orderId": "12345",
    "items": [
    {"sku": "111", "count": 1, "size1": "5.1", "size2": "2.2", "size3": "5.3",
     "weight": "7.34", "type": ["2"]},
    {"sku": "222", "count": 3, "size1": "4", "size2": "5.23", "size3": "6.2",
     "weight": "7.45", "type": ["8", "9", "10"]},
    {"sku": "333", "count": 2, "size1": "11", "size2": "12.5", "size3": "13.3",
     "weight": "14.2", "type": ["15", "16"]},
    {"sku": "444", "count": 2, "size1": "11", "size2": "12.5", "size3": "13.3",
     "weight": "14.2", "type": ["15", "16"]}
    ]
}

r = requests.post("http://localhost:8080/pack", json=data)

print(r.json())
