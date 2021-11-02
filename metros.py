d =float(input('Digite uma distancia em metros:'))
km = d/1000
hm = d/100
dam = d/10
dm = d*10
cm = d*100
mm = d*1000

print(' A distância em km é {}km \n A distância em hm é {}hm \n A distância em dam é {}dam \n A distância em dm é {:.0f}dm \n A distância em cm é {:.0f}cm \n A distância em mm é {:.0f}mm'.format(km,hm,dam,dm,cm,mm))