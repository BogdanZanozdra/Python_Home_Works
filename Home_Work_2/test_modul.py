import portfolio


stocks = {"AAPL": 10, "GOOGLE": 5, "MSFT": 8}
prices = {"AAPL": 150.25, "GOOGLE": 2500.75, "MSFT": 360.50}

print(f'Стоимость портфеля акций: {portfolio.calculate_portfolio_value(stocks, prices)}')

stocks = {"AAPL": 10, "GOOGLE": 5, "MSFT": 8}
prices = {"AAPL": 160.25, "GOOGLE": 2600.75, "MSFT": 350.50}

print(f'Процентная доходность портфеля: {portfolio.calculate_portfolio_return(100, 150)}%')
print(f'Акция, которая имеет наибольшую прибыль по сравнению с ее начальной стоимостью {portfolio.get_most_profitable_stock(stocks, prices)}')