medida = float(input('Digite uma medida em metros '))
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print('Sua medida é {} m, que pode ser {} km, {} hm, {} dam, {} dm, {} cm, {} mm'.format(medida,km,hm,dam,dm,cm,mm))