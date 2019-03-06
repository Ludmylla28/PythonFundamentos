##modulos e pacotes
import math
#verificando todos os metodos do modulo 
dir(math)

#usando um metodo do modulo
math.sqrt(25)

from math import sqrt

sqrt(9)

#entendendo para que serve aquele metodo
help(sqrt)

print("-" *100) 

import random

random.choice(['maça','banana','pera'])

random.sample(range(100),10)

print("-" *100)

import statistics

dados = [2.75, 1.20, 3.5, 6.8, 7.6]

statistics.mean(dados)
statistics.median(dados)

print("-" *100)

import os 

os.getcwd()

print(dir(os))

print("-" *100)

import sys 
sys.stdout.write('Teste')

sys.version

print(dir(sys))

print("-" *100)

import urllib.request

resposta = urllib.request.urlopen('http://python.org')
print(resposta)

#lendo html
html = resposta.read()
print(html)

