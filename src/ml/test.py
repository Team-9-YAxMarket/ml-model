import requests

# data = {"orderId": "unique_order_id",
#  "items": [
#     {"sku": "unique_sku_1", "count": 1, "size1": "5.1", "size2": "2.2", "size3": "5.3",
#      "weight": "7.34", "type": ["2"]},
#     {"sku": "unique_sku_2", "count": 3, "size1": "4", "size2": "5.23", "size3": "6.2",
#      "weight": "7.45", "type": ["8", "9", "10"]},
#     {"sku": "unique_sku_3", "count": 2, "size1": "11", "size2": "12.5", "size3": "13.3",
#      "weight": "14.2", "type": ["15", "16"]}
#    ]
# }
data = {
   "orderId":"c81aa704-c75c-413f-947e-14d8c8ad08e2",
   "package": "",
   "status": "",
   "items":[
      {
         "sku":"50d3c4fc66ad423b7feaadff2d682ee0",
         "length":21.0,
         "width":9.0,
         "height":14.0,
         "weight":4.3,
         "count":1,
         "barcode":"1845678901002",
         "img":"https://avatars.mds.yandex.net/get-mpic/4736439/img_id8019086743167567106.jpeg/orig",
         "cargotypes":[
            "290",
            "901"
         ]
      },
      {
         "sku":"24ce9dba9f301ada55f60e25ee1498d2",
         "length":21.0,
         "width":28.0,
         "height":3.0,
         "weight":2.4,
         "count":1,
         "barcode":"1845678901003",
         "img":"https://avatars.mds.yandex.net/get-mpic/1750349/img_id521242709732615283.png/orig",
         "cargotypes":[
            "490",
            "290",
            "441"
         ]
      }
   ]
}
r = requests.get("http://localhost:8000/pack", json=data)

print(r.url)
print(r.json())


