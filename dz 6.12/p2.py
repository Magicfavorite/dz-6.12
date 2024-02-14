osnova = float(input("Введите зарплату за месяц: "))
credit = float(input("Введите сумму месячного платежа по кредиту: "))
utilities_debt = float(input("Введите задолженность за коммунальные услуги: "))

balance = osnova - credit - utilities_debt

print("Остаток после выплат:", balance)
