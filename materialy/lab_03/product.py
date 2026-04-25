# -*- coding: utf-8 -*-
class Product:
    def __init__(self, name: str, price: float, quantity: int):
        if price <= 0:
            raise ValueError("Cena musi być dodatnia")
        if quantity < 0:
            raise ValueError("Ilość musi być dodatnia")
        self.name = name
        self.price = price
        self.quantity = quantity

    def add_stock(self, amount: int):
        if amount < 0:
            raise ValueError("Wartość musi być dodatnia")
        self.quantity += amount

    def remove_stock(self, amount: int):
        if amount < 0:
            raise ValueError("wartość musi być dodatnia")
        if amount > self.quantity:
            raise ValueError("Nie wystarczający stan magazynowy")
        self.quantity -= amount

    def is_available(self) -> bool:
        return self.quantity > 0

    def total_value(self) -> float:
        return self.price * self.quantity

    def apply_discount(self, percent: float):
        if percent < 0 or percent > 100:
            raise ValueError("Zniżka procentowa powinna być w zakresie 0 - 100")
        self.price -= self.price * (percent / 100)