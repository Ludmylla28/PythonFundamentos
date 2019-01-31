# loop while 
contador = 0
while contador < 5:
    print('contando {}'.format(contador))
    contador += 1

print("-" * 30)

#usando else para incerrar o while
x = 0
while x < 10:
    print('O valor de x nesta interação é: ', x)
    print('x ainda é menor que 10')
    x += 1

else:
    print('loop incerrado')

print("-" * 30)

#pass, break e continue 
# tambem é possivel usar condicionais como if dentro do loop

counter = 0

while counter < 100:
    if counter == 4:
        break
    else:
        pass
    print(counter)
    counter = counter + 1

print("-" * 30)

# usando continue no loop for
for verificador in "Python":
    if verificador == "h":
        continue
    print(verificador)

print("-" * 30)

## while e for juntos 
for i in range(2,30):
    j = 2
    counter = 0
    while j < i:
        if i % j == 0:
            counter = 1
            j += 1 
        else:
            j += 1
    if counter == 0:
        print(str(i) + " é um numero primo")
        counter = 0
    else:
        counter = 0