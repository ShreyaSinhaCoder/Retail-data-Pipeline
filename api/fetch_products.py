import requests
import json

url = "https://fakestoreapi.com/products"
response = requests.get(url)

with open("products.json", "w") as f:
    json.dump(response.json(), f)

print("Products data fetched successfully")