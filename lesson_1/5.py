"""Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение.
Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника."""

revenue = int(input('Enter the revenue: '))
costs = int(input('Enter the costs: '))

profit = revenue - costs

print(f'Company works with {f"profit: {profit:.2f}" if profit > 0 else f"losses: {profit:.2f}"}')

if profit > 0:
    profitability = int(profit / revenue * 100)

    number_of_employees = int(input('Enter the number_of_employees: '))

    print(f'Profit is {profit:.2f}')
    print(f'Profitability is {profitability}%')
    print(f'Profit per employee: {profit / number_of_employees:.2f}')
