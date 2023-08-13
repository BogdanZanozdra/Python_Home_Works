# Решить задачи, которые не успели решить на семинаре.
# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
#
# Задача: Расчет финансовых показателей портфеля акций:
# Вы являетесь инвестором и хотите создать программу для расчета нескольких финансовых показателей вашего портфеля акций. Создайте модуль Python
# под названием "portfolio.py", который будет содержать функции для выполнения следующих операций:
# 1. Расчет общей стоимости портфеля акций: Функция calculate_portfolio_value(stocks: dict, prices: dict) -> float принимает два аргумента:
# stocks - словарь, где ключами являются символы акций (например, "AAPL" для Apple Inc.), и значениями - количество акций каждого символа.
# prices - словарь, где ключами являются символы акций, а значениями - текущая цена каждой акции. Функция должна вернуть общую стоимость портфеля
# акций на основе количества акций и их текущих цен.
# Пример: Пришло
# stocks = {"AAPL": 10, "GOOGL": 5, "MSFT": 8}
# prices = {"AAPL": 150.25, "GOOGL": 2500.75, "MSFT": 300.50}
# Вышло: 16410,25
#
# 2. Расчет доходности портфеля: Функция calculate_portfolio_return(initial_value: float, current_value: float) -> float принимает два аргумента:
# initial_value - начальная стоимость портфеля акций. current_value - текущая стоимость портфеля акций. Функция должна вернуть процентную
# доходность портфеля. Пример:
# Пришло: 10000.0
#         15000.0
# Вышло:  50%
#
# 3. Определение наиболее прибыльной акции: Функция get_most_profitable_stock(stocks: dict, prices: dict) -> str принимает два аргумента:
# stocks - словарь с акциями и их количеством. prices - словарь с акциями и их текущими ценами. Функция должна вернуть символ акции (ключ),
# которая имеет наибольшую прибыль по сравнению с ее начальной стоимостью. Начальная стоимость - первый вызов calculate_portfolio_value,
# данные из этого вызова следует сохранить в защищенную переменную на уровне модуля.
# Пример: Пришло:
#         stocks = {"AAPL": 10, "GOOGL": 5, "MSFT": 8}
#         prices = {"AAPL": 155.25, "GOOGL": 2600.75, "MSFT": 800.50}
# Вышло:  MSFT
#
# Тестирование модуля:
# Напишите небольшую программу, которая импортирует модуль "portfolio.py" и демонстрирует использование всех трех функций.
# Создайте словари для акций и цен, запустите функции и выведите результаты.
# Примечание:
# В реальном мире вы можете использовать API для получения актуальных данных о ценах акций. В данной задаче можно использовать фиктивные данные
# для тестирования и обучения.


def calculate_portfolio_value(stocks: dict, prices: dict) -> float:
    global _init_prices
    _init_prices = prices
    res = {key: value * prices[key] for key, value in stocks.items()}
    return sum(res.values())


def calculate_portfolio_return(initial_value: float, current_value: float) -> float:
    return (current_value - initial_value) / initial_value * 100


def get_most_profitable_stock(stocks: dict, prices: dict) -> str:
    profit_stock_dict = {}
    for key, value in prices.items():
        profit_stock_dict.setdefault(key, (value - _init_prices[key]))
    key_list = list(profit_stock_dict.keys())
    value_list = list(profit_stock_dict.values())
    pos = value_list.index(max(profit_stock_dict.values()))
    return key_list[pos]


_init_prices = {}
stocks = {"AAPL": 10, "GOOGLE": 5, "MSFT": 8}
prices = {"AAPL": 150.25, "GOOGLE": 2500.75, "MSFT": 360.50}

if __name__ == '__main__':
    print(calculate_portfolio_value(stocks, prices))
    stocks = {"AAPL": 10, "GOOGLE": 5, "MSFT": 8}
    prices = {"AAPL": 160.25, "GOOGLE": 2600.75, "MSFT": 350.50}
    print(get_most_profitable_stock(stocks, prices))
    print(calculate_portfolio_return(100, 150))




