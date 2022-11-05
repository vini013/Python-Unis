age = int(input("Coloque sua idade em dias: "))
years = age // 365
months = (age % 365) // 30
days = (age % 365) % 30
completeAge = 'Você tem: ' + str(years) + ' anos, ' + str(months) + ' meses e ' + str(days) + ' dias.'
print(completeAge)