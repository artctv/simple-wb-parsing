from __future__ import annotations
from typing import List

from sqlalchemy.sql import func
from sqlalchemy import ForeignKey, Integer, DateTime, String
from sqlalchemy.orm import Mapped, DeclarativeBase, mapped_column, relationship


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)


class Item(Base):
    __tablename__ = "item"

    vendor_code: Mapped[int] = mapped_column(Integer)
    prices: Mapped[List["Price"]] = relationship(back_populates="item")
    category: Mapped[str] = mapped_column(String)
    sale_quantity: Mapped[int] = mapped_column(Integer)


class Price(Base):
    __tablename__ = "price"

    value: Mapped[int] = mapped_column(Integer)
    item_id: Mapped[int] = mapped_column(ForeignKey("item.id"))
    item: Mapped["Item"] = relationship(back_populates="prices")
    created_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())
