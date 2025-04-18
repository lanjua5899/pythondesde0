from fastapi import APIRouter

router = APIRouter()

products_list = ["Producto 1", "Producto 2",
                 "Producto 3", "Producto 4", "Producto 5"]


@router.get("/")
async def products():
    return products_list
