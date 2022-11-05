number = int(input("Digite um numero de 1 a 100: "))
isPrime = True

if number < 1 or number > 100:
    print("Numero invalido")

if number > 1:
    for num in range(2, number):
        if (number % num) == 0:
            isPrime = False
            break

if isPrime == False:
    print("O numero não é primo")
else:
    print("O numero é primo")