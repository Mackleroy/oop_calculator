import datetime as dt
from datetime import timedelta


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []
        self.now = dt.datetime.now()

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        sum = 0
        today = dt.datetime.date(self.now)
        for record in calc.records:
            date_of_record = dt.datetime.date(record.date)
            if date_of_record == today:
                sum += record.amount
        return sum

    def show_today_stats(self):
        result = self.get_today_stats()
        print('За сегодня потрачено {0}'.format(result))

    def get_week_stats(self):
        week = timedelta(7)
        week_ago = dt.datetime.date(self.now - week)
        week_sum = 0
        today = dt.datetime.date(self.now)
        for record in self.records:
            date_of_record = dt.datetime.date(record.date)
            if week_ago <= date_of_record <= today:
                week_sum += record.amount
        return week_sum

    def show_week_stats(self):
        result = self.get_week_stats()
        print('За неделю потрачено {0}'.format(result))

    def get_whole_life_spend(self):
        life_sum = 0
        for record in self.records:
            life_sum += record.amount
        return life_sum

    def show_whole_life_spend(self):
        result = self.get_whole_life_spend()
        print('За всю жизнь потрачено {0}'.format(result))


class CaloriesCalculator(Calculator):
    def __init__(self, limit):
        super().__init__(limit)

    def get_calories_remained(self):
        today_spend = self.get_today_stats()
        balance = self.limit - today_spend
        if self.limit > today_spend:
            print('Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {0} кКал'.format(balance))
        else:
            print('Хватит есть!')


class CashCalculator(Calculator):
    def __init__(self, limit):
        super().__init__(limit)

    def get_today_cash_remained(self, currency):
        today_spend = self.get_today_stats()
        balance = self.limit - today_spend
        eur_rub = 88.59
        usd_rub = 74.35
        if currency == 'eur':
            balance = round((balance / eur_rub), 3)
            balance = str(balance) + " EUR"
        elif currency == 'usd':
            balance = round((balance / usd_rub), 3)
            balance = str(balance) + " USD"
        elif currency == 'rub':
            balance = str(balance) + " RUB"
        elif currency != 'rub':
            return print('Enter valid currency')

        if self.limit > today_spend:
            print('На сегодня осталось {0}'.format(balance))
        elif self.limit == today_spend:
            print('Денег нет, держись!')
        elif self.limit < today_spend:
            balance.replace('-', '')
            print('Денег нет, держись: твой долг {0}'.format(balance))


class Record:
    def __init__(self, amount, date='', comment=''):
        self.amount = amount
        self.comment = comment
        if date == '':
            self.date = dt.datetime.now()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%y')


# Функция для инициации трат
def add_stat(amount, date='', comment=''):
    calc.add_record(Record(amount, date=date, comment=comment))


# Лимит общий для калькулятора
calc_limit = 2000

calc = Calculator(calc_limit)
cash = CashCalculator(calc_limit)
calories = CaloriesCalculator(calc_limit)

# задание трат
add_stat(99, comment='Бутеры')
add_stat(1000, comment='Чай')
add_stat(900, comment='Сок')
add_stat(1123, date='01.03.21', comment='Обед')
add_stat(10000, date='04.03.21', comment=' Телефон')
add_stat(1000000, date='20.02.98', comment='Машина')

# Вызов функций проверки и показа статистики
calc.show_today_stats()
calc.show_week_stats()
calc.show_whole_life_spend()

# Вызов функции подсчета баланса
calories.get_calories_remained()
# Различные виды валют, последний с ошибкой
cash.get_today_cash_remained('rub')
cash.get_today_cash_remained('usd')
cash.get_today_cash_remained('eur')
cash.get_today_cash_remained('rab')

# Вывод всего списка
# for i in calc.records:
#     print(i.amount, i.date, i.comment)
