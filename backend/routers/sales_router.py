from fastapi import APIRouter, HTTPException
from schemas.sales_schema import SaleCreate
from models.sales_model import create_sale

router = APIRouter(
    prefix="/sales",
    tags=["POS / Sales"]
)

@router.post("/")
def make_sale(sale: SaleCreate):
    try:
        sale_id, total = create_sale(sale)
        return {
            "message": "Sale completed successfully",
            "sale_id": sale_id,
            "total_amount": total
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
