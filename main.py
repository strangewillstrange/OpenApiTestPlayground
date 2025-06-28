from fastapi import FastAPI, Body, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from database import orders, engine
from sqlalchemy import select
import sqlalchemy

app = FastAPI()

class Item(BaseModel):
    ItemID: str
    Description: str
    Quantity: int
    Price: float

class Address(BaseModel):
    BillingAddress1: Optional[str]
    BillingAddress2: Optional[str]
    BillingCity: Optional[str]
    BillingState: Optional[str]
    BillingZipCode: Optional[str]
    ShippingAddress1: Optional[str]
    ShippingAddress2: Optional[str]
    ShippingCity: Optional[str]
    ShippingState: Optional[str]
    ShippingZipCode: Optional[str]

class OrderDetails(BaseModel):
    order: str
    bin: str
    last4: str
    expDate: str
    FirstName: str
    LastName: str
    Email: str
    Phone: str
    OrderDate: str
    TotalAmount: float
    ARN: str
    BillingAddress: Address
    ShippingAddress: Address
    Items: List[Item]

class OrderQuery(BaseModel):
    bin: str
    last4: str
    expDate: str
    TotalAmount: float

conn = engine.connect()

@app.post("/order/upload", status_code=201)
def create_order(order: OrderDetails):
    result = conn.execute(select(orders).where(orders.c.order_id == order.order))
    if result.fetchone():
        raise HTTPException(status_code=409, detail="Order already exists.")
    conn.execute(orders.insert().values(order_id=order.order, data=order.dict()))
    return {"status": "success"}

@app.get("/order/upload/{orderId}")
def get_order(orderId: str):
    result = conn.execute(select(orders).where(orders.c.order_id == orderId)).fetchone()
    if not result:
        raise HTTPException(status_code=404, detail="Order not found.")
    return result.data

@app.put("/order/upload/{orderId}")
def update_order(orderId: str, order: OrderDetails):
    result = conn.execute(select(orders).where(orders.c.order_id == orderId))
    if not result.fetchone():
        raise HTTPException(status_code=404, detail="Order not found.")
    conn.execute(orders.update().where(orders.c.order_id == orderId).values(data=order.dict()))
    return {"status": "updated"}

@app.delete("/order/upload/{orderId}", status_code=204)
def delete_order(orderId: str):
    conn.execute(orders.delete().where(orders.c.order_id == orderId))
    return

@app.post("/order/query")
def query_order(query: OrderQuery):
    stmt = select(orders)
    results = conn.execute(stmt).fetchall()
    matched = []
    for row in results:
        data = row.data
        if all([
            data["bin"] == query.bin,
            data["last4"] == query.last4,
            data["expDate"] == query.expDate,
            data["TotalAmount"] == query.TotalAmount,
        ]):
            matched.append(data)
    return matched