from fastapi import FastAPI
from pydantic import BaseModel, Field

products = [
    {"id": 1, "name": "Keyboard", "price": 500000},
    {"id": 2, "name": "Mouse", "price": 300000},
    {"id": 3, "name": "Screen", "price": 400000}
]

class CreateProduct(BaseModel):
    id: int
    name: str = Field(min_length=2)
    price: float = Field(gt=0, lt=9000000)

class UpdateProduct(BaseModel):
    name:str
    price:float

app = FastAPI()

@app.get('/')
def get_root():
    return {
        "message": "Chào mừng đến với server của tôi"
    }
    
# API lấy toàn bộ sản phẩm
@app.get('/products')
def get_products():
    return {
        "data": products
    }
    
# API lấy 1 sản phẩm theo id
# /product/1
@app.get('/product/{product_id}')
def get_product_by_id(product_id: int):
    for product in products:
        if product['id'] == product_id:
            return {
                "data": product
            }
    return {
        "message": "Không tìm thấy sản phẩm",
        "data": None
    }
    # return {
    #     "data" : next((p for p in products if p['id'] == product_id), None)
    # }
    
# API lấy danh sách sản phẩm theo khoảng giá
# /product?start_price=200000&end_price=450000
@app.get('/product')
def get_products_by_price(start_price: float, end_price: float):
    filter_products = []
    for product in products:
        if start_price < product['price'] < end_price:
            filter_products.append(product)
    if filter_products:
        return {
            "message": "Danh sách sản phẩm tìm trong khoảng giá",
            "data": filter_products
        }
    return {
        "message": "Trong khoảng giá không có sản phẩm",
        "data": None
    }
    
# API thêm mới sản phẩm
@app.post('/product')
def create_product(new_product: CreateProduct):
    products.append({
        "id": new_product.id,
        "name": new_product.name,
        "price": new_product.price
    })
    return {
        "message": "Thêm sản phẩm thành công",
        "data": new_product
    }
    
# API cập nhật sản phẩm  
@app.put('/product/{product_id}')
def update_product(product_id: int, update_product: UpdateProduct):
    for product in products:
        if product['id'] == product_id:
            product['name'] = update_product.name
            product['price'] = update_product.price
            return {
                "message": "Cập nhật sản phẩm thành công",
                "data":{
                    "id": product_id,
                    "name": update_product.name,
                    "price": update_product.price
                }
            }
    return {
        "message": "Sản phẩm không tồn tại",
        "data": None
    }
    
# API xóa sản phẩm 
@app.delete('/product/{product_id}')
def delete_product(product_id:int):
    for product in products:
        if product['id'] == product_id:
            products.remove(product)
            return {
                "message":"Xóa sản phẩm thành công",
                "data":product
            }
    return {
        "message":"Không tồn tại sản phẩm",
        "data":None 
    }