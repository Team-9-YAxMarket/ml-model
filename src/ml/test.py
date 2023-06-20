import requests

data = {
       "items":[
          {
             "sku":"50d3c4fc66ad423b7feaadff2d682ee0",
             "length":21.0,
             "width":9.0,
             "height":14.0,
             "weight":4.3,
             "count":1,
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
             "cargotypes":[
                "490",
                "290",
                "441"
             ]
          }
       ]
    }

r = requests.post("http://localhost:8000/pack/", json=data)

print(r.json())