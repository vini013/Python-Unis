import math

a = int(input('Coloque o lado A do triangulo: '))
b = int(input('Coloque o lado B do triangulo: '))
c = int(input('Coloque o lado C do triangulo: '))

if a > b + c:
    print(str(a) + ' ' + str(b) + ' ' + str(c) + ' nao formam um triangulo')
else: 
  semiPerimetro = (a + b + c) // 2
  area = math.sqrt(semiPerimetro * ((semiPerimetro - a) * (semiPerimetro - b) * (semiPerimetro - c)))

  print('Area do triangulo é: ' + str(area))

