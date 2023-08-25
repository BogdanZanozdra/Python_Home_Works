# Напишите программу банкомат.
#
# Начальная сумма равна нулю
# Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия кратны 50 у.е.
# Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третей операции пополнения или снятия начисляются проценты - 3%
# Нельзя снять больше, чем на счёте
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# Любое действие выводит сумму денег


def get_amount() -> int:
    return int(input('Введите сумму:'))


def count_transactions(amount_to_calculate) -> int:
    global count
    count += 1
    if count == COUNT_TRANSACTIONS:
        print(f'Мы начислили {amount_to_calculate * AMOUNT_CALCULATION_PERCENTAGE / 100} за каждую третью операцию.')
        amount_to_calculate = amount_to_calculate + amount_to_calculate * AMOUNT_CALCULATION_PERCENTAGE / 100
        count = 0
    return amount_to_calculate


def withdraw(current_amount: float):
    global count
    global my_amount
    withdraw_amount = get_amount()
    if current_amount > RICH_POINT:
        current_amount = current_amount - current_amount * WEALTH_TAX / 100
        if withdraw_amount % MIN_WITHDRAW != 0 or withdraw_amount > current_amount:
            my_amount = current_amount
            return (
                f'Минимальная купюра для снятия {MIN_WITHDRAW}, также сумма не может превышать остаток на счете! На '
                f'вашем счете {my_amount}, и мы сняли налог на богатство!')
        current_amount = take_money(current_amount, withdraw_amount)
        my_amount = count_transactions(current_amount)
        return f'Успех! Теперь на вашем счете {current_amount} и мы сняли налог на богатство!'
    elif current_amount <= RICH_POINT:
        if withdraw_amount % MIN_WITHDRAW != 0 or withdraw_amount > current_amount:
            return (
                f'Минимальная купюра для снятия {MIN_WITHDRAW}, также сумма не может превышать остаток на счете! На '
                f'вашем счете {current_amount}')
        current_amount = take_money(current_amount, withdraw_amount)
        my_amount = count_transactions(current_amount)
        return f'Успех! Теперь на вашем счете {my_amount}'


def put_money(current_amount: float):
    global count
    global my_amount
    put_amount = get_amount()
    if current_amount > RICH_POINT:
        current_amount = current_amount - current_amount * WEALTH_TAX / 100
        if put_amount % MIN_WITHDRAW != 0:
            my_amount = current_amount
            return (
                f'Минимальная купюра для пополнения {MIN_WITHDRAW}. На вашем счете {my_amount}, и мы сняли налог '
                f'на богатство!')
        current_amount += put_amount
        my_amount = count_transactions(current_amount)
        return f'Успех! Теперь на вашем счете {my_amount} и мы сняли налог на богатство!'
    elif current_amount <= RICH_POINT:
        if put_amount % MIN_WITHDRAW != 0:
            return (
                f'Сумма пополнения должна быть кратна {MIN_WITHDRAW}. На вашем счете {current_amount}')
        current_amount += put_amount
        my_amount = count_transactions(current_amount)
        return f'Успех! Теперь на вашем счете {my_amount}!'


def take_money(input_amount: float, withdraw_amount: int):
    amount_percent = withdraw_amount * WITHDRAWAL_PERCENTAGE / 100
    if amount_percent < MIN_SUM_PERCENTAGE:
        amount_percent = MIN_SUM_PERCENTAGE
    elif amount_percent > MAX_SUM_PERCENTAGE:
        amount_percent = MAX_SUM_PERCENTAGE
    input_amount = input_amount - withdraw_amount - amount_percent
    return input_amount


my_amount = 10000000
MIN_WITHDRAW = 50
WITHDRAWAL_PERCENTAGE = 1.5
MIN_SUM_PERCENTAGE = 30
MAX_SUM_PERCENTAGE = 600
AMOUNT_CALCULATION_PERCENTAGE = 3
RICH_POINT = 5_000_000
WEALTH_TAX = 10
COUNT_TRANSACTIONS = 3
count = 0

while True:
    choice = int(input('Это банкомат, Вы можете:\n'
                       '\t1.Пополнить \n'
                       '\t2.Снять \n'
                       '\t3.Выйти \n'
                       'Сделайте свой выбор:\n'))
    if choice == 1:
        print(put_money(my_amount))
    elif choice == 2:
        print(withdraw(my_amount))
    elif choice == 3:
        print('Гудбай!')
        break
    else:
        print('Введите число от 1 до 3:')

print(my_amount)
