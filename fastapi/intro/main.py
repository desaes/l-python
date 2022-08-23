from fastapi import FastAPI
from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    price: float
    on_sale: bool = False

products = [
    Product(id=1, name='3d printer', price=2000, on_sale=True),
    Product(id=2, name='amp', price=1000, on_sale=True),
    Product(id=3, name='decoder', price=1000, on_sale=True),
    Product(id=4, name='switch', price=20, on_sale=True),
    Product(id=5, name='pencil', price=1, on_sale=True),

]

app = FastAPI()

@app.get('/')
async def index():
    return {"Hello": "World"}

@app.get('/products/{id}')
async def search_product(id: int):
    for product in products:
        if product.id == id:
            return product
    return None

@app.put('/products/{id}')
async def update_product(id: int, product: Product):
    for item in products:
        if item.id == id:
            item = product
            return item
    return None
