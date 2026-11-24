
from abc import ABC, abstractmethod
from datetime import date


# ===== АБСТРАКЦИЯ =====

class MenuItem(ABC):
    def __init__(self, name, base_price):
        self.name = name
        self.base_price = base_price

    @abstractmethod
    def calculatePrice(self):
        pass


# ===== ПОЛИМОРФИЗМ: БЛЮДА =====

class Pizza(MenuItem):
    def __init__(self, name, base_price, size):
        super().__init__(name, base_price)
        self.size = size

    def calculatePrice(self):
        if self.size == "large":
            return self.base_price * 1.3
        return self.base_price


class Drink(MenuItem):
    def __init__(self, name, base_price, isIce):
        super().__init__(name, base_price)
        self.isIce = isIce

    def calculatePrice(self):
        return self.base_price

    def __str__(self):
        if self.isIce:
            return self.name + " (со льдом)"
        return self.name


class ComboSet(MenuItem):
    def __init__(self, name, items):
        super().__init__(name, 0)
        self.items = items

    def calculatePrice(self):
        total = 0
        for item in self.items:
            total += item.calculatePrice()
        return total * 0.85


# ===== ИНКАПСУЛЯЦИЯ: ЗАКАЗ =====

class Order:
    def __init__(self):
        self.__items = []
        self.__status = "New"

    def addItem(self, item):
        if self.__status != "New":
            raise Exception("Нельзя добавлять блюда в этот заказ!")

        self.__items.append(item)

    def nextStep(self):
        statuses = ["New", "Preparing", "Delivering", "Completed"]

        if self.__status != "Completed":
            index = statuses.index(self.__status)
            self.__status = statuses[index + 1]
            print("Статус:", self.__status)
        else:
            print("Заказ уже завершён!")

    def getTotalCost(self):
        total = 0
        for item in self.__items:
            total += item.calculatePrice()
        return total

    def showOrder(self):
        print("\nВаш заказ:")
        for item in self.__items:
            print(item.name, "-", item.calculatePrice(), "сом")

        print("Итого:", self.getTotalCost(), "сом")
        print("Статус:", self.__status)

    def pay(self, paymentMethod):
        paymentMethod.collectPayment(self.getTotalCost())


# ===== ИНТЕРФЕЙС ОПЛАТЫ =====

class PaymentStrategy(ABC):
    @abstractmethod
    def collectPayment(self, amount):
        pass


class CardPayment(PaymentStrategy):
    def __init__(self, month, year):
        self.month = month
        self.year = year

    def collectPayment(self, amount):
        today = date.today()

        if (self.year, self.month) < (today.year, today.month):
            print("Ошибка: срок действия карты истёк!")
        else:
            print("Оплата картой прошла успешно!")
            print("Списано:", amount, "сом")


class CashPayment(PaymentStrategy):
    def collectPayment(self, amount):
        print("Оплата наличными!")
        print("К оплате:", amount, "сом")


# ===== ПРОВЕРКА ПРОГРАММЫ =====

pizza = Pizza("Пепперони", 500, "large")
drink = Drink("Кола", 100, True)
water = Drink("Вода", 50, False)

combo = ComboSet("Комбо", [pizza, drink])

order = Order()

order.addItem(pizza)
order.addItem(drink)
order.addItem(water)
order.addItem(combo)

order.showOrder()

print("\nВыберите способ оплаты:")
print("1 - Карта")
print("2 - Наличные")

choice = input("Ваш выбор: ")

if choice == "1":
    payment = CardPayment(12, 2027)
    order.pay(payment)
elif choice == "2":
    payment = CashPayment()
    order.pay(payment)
else:
    print("Неверный выбор!")

print("\nИзменение статуса заказа:")
order.nextStep()
order.nextStep()

order.showOrder()
