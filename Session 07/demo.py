from fastapi import FastAPI, status, Request, HTTPException
from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional, Any
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

products = [
    {"id": 1, "name": "Keyboard", "price": 500000},
    {"id": 2, "name": "Mouse", "price": 300000},
    {"id": 3, "name": "Screen", "price": 400000}
]

class BaseResponse(BaseModel):
    status_code: int
    message: str
    data: Optional[Any]
    errors: Optional[str]
    time_stamp: str
    path: str

class CreateProduct(BaseModel):
    id: int
    name: str = Field(min_length=2)
    price: float = Field(gt=0, lt=9000000)

def create_response(request, status_code: int, message: str, data = None, errors = None):
    return BaseResponse(
        status_code = status_code,
        message = message,
        data = data,
        errors = errors,
        time_stamp = datetime.now().isoformat(),
        path = request.url.path     
    )

app = FastAPI()

@app.get("/products")
def get_products(request: Request):
    return create_response(request, status.HTTP_200_OK, "Success!", products)
    
@app.get("/product/{id}")
def get_product_by_id(request: Request, id: int):
    for product in products:
        if product['id'] == id:
            return create_response(request, status.HTTP_200_OK, "Success!", product)
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Không tìm thấy sản phẩm"
    )

# API thêm mới sản phẩm
@app.post('/product', status_code=status.HTTP_201_CREATED)
def create_product(request : Request, new_product: CreateProduct):
    products.append({
        "id": new_product.id,
        "name": new_product.name,
        "price": new_product.price
    })
    return create_response(request, status.HTTP_201_CREATED, "Success!", new_product)

@app.exception_handler(HTTPException)
def http_exception_handler(
    request: Request,
    exc: HTTPException
):
    response = create_response(request, exc.status_code, "Failed!", errors = exc.detail)
    return JSONResponse(
        status_code = exc.status_code,
        content = response.model_dump()
    )
    
@app.exception_handler(Exception)
def global_exception_handler(
    request: Request,
    exc: Exception
):
    response = create_response(request, status.HTTP_500_INTERNAL_SERVER_ERROR, "Failed!", errors = str(exc))
    return JSONResponse(
        status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
        content = response.model_dump()
    )
    
@app.exception_handler(RequestValidationError)
def validation_handler(
    request: Request,
    exc: RequestValidationError
):
    response = create_response(request, status.HTTP_422_UNPROCESSABLE_CONTENT, "Validation failed", errors = exc.errors())
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
        content=response.model_dump()
    )