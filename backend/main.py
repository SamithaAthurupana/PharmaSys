from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers.medicine_router import router as medicine_router
from routers.inventory_router import router as inventory_router
from routers.sales_router import router as sales_router
from routers.employee_router import router as employee_router
from routers.dashboard_router import router as dashboard_router
from routers.auth_router import router as auth_router

app = FastAPI(title="PharmaSys Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(medicine_router)
app.include_router(inventory_router)
app.include_router(sales_router)
app.include_router(employee_router)
app.include_router(dashboard_router)

@app.get("/")
def root():
    return {"status": "PharmaSys backend running"}