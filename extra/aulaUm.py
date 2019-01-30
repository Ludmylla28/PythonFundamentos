numUm = int(input('Escolha um numero '))
numDois = int(input('Escolha outro numero '))
s = numUm + numDois
m = numUm * numDois
d = numUm / numDois
di = numUm // numDois
e = numUm ** numDois
print('O valor escolhido foi {} e {}, a soma desses valores é {}, a multiplicação é {} e a divisão é {:.3f}'.format(numUm, numDois, s, m, d))
print('A divisão inteira é {} e a potência é {}'.format(di,e))