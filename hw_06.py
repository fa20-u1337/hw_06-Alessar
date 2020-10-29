class Fib():
    """Число Фибоначчи.

    >>> start = Fib()
    >>> start
    0
    >>> start.next()
    1
    >>> start.next().next()
    1
    >>> start.next().next().next()
    2
    >>> start.next().next().next().next()
    3
    >>> start.next().next().next().next().next()
    5
    >>> start.next().next().next().next().next().next()
    8
    >>> start.next().next().next().next().next().next() # Проверка, что start не изменился
    8
    """

    def __init__(self, value=0):
        self.value = value

    def next(self):
        pass

    def __repr__(self):
        return str(self.value)

class VendingMachine:
    """Торговый автомат, продающий некоторый товар по некоторой цене.
    
    >>> v = VendingMachine('яблоко', 10)
    >>> v.vend()
    'Товара нет в наличии.'
    >>> v.restock(2)
    'Количество товара «яблоко»: 2'
    >>> v.vend()
    'Нужно дополнительно внести 10 ₽.'
    >>> v.deposit(7)
    'Доступно: 7 ₽'
    >>> v.vend()
    'Нужно дополнительно внести 3 ₽.'
    >>> v.deposit(5)
    'Доступно: 12 ₽'
    >>> v.vend()
    'Получите яблоко и сдачу 2 ₽.'
    >>> v.deposit(10)
    'Доступно: 10 ₽'
    >>> v.vend()
    'Получите яблоко.'
    >>> v.deposit(15)
    'Товара нет в наличии. Вот твои деньги — 15 ₽.'

    >>> w = VendingMachine('лимонад', 2)
    >>> w.restock(3)
    'Количество товара «лимонад»: 3'
    >>> w.restock(3)
    'Количество товара «лимонад»: 6'
    >>> w.deposit(2)
    'Доступно: 2 ₽'
    >>> w.vend()
    'Получите лимонад.'
    """
    def __init__(self, good, cost):
        self.good = good
        self.cost = cost
        self.count = 0
        self.money = 0

    def vend(self):
        if self.count == 0:
            return 'Товара нет в наличии.'
        if self.money < self.cost:
            return 'Нужно дополнительно внести {0} ₽.'.format(self.cost - self.money)
        self.money -= self.cost
        self.count -= 1
        if self.money > 0:
            self.money, money = 0, self.money
            return 'Получите {0} и сдачу {1} ₽.'.format(self.good, money)
        else:
            return 'Получите {0}.'.format(self.good)

    def restock(self, count):
        self.count += count
        return 'Количество товара «{0}»: {1}'.format(self.good, self.count)

    def deposit(self, money):
        self.money += money
        if self.count > 0:
            return 'Доступно: {0} ₽'.format(self.money)
        else:
            return 'Товара нет в наличии. Вот твои деньги — {0} ₽.'.format(self.money)
