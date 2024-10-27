money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

cur_budget = salary + money_capital
month = 0

while cur_budget >= spend:
    month +=1
    money_capital -= spend - salary
    spend += spend*increase
    cur_budget = salary + money_capital

print("Количество месяцев, которое можно протянуть без долгов:", month)
