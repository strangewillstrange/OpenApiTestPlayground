from sqlalchemy import create_engine, Column, String, Float, Integer, JSON, Table, MetaData

DATABASE_URL = "sqlite:///./orders.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
metadata = MetaData()

orders = Table(
    "orders",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("order_id", String, unique=True, index=True),
    Column("data", JSON),
)

metadata.create_all(bind=engine)