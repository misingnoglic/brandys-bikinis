import requests
from secrets import *
url = f"https://{shopify_api_id}:{shopify_api_pass}@brandys-bikinis.myshopify.com/admin/products.json"
r = requests.get(url)
products = [(p['id'], p['title']) for p in r.json()['products']]
print("const products = [")
for id, title in products:
    print(f"    {id},  // {title}")
print("]")
