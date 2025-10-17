dias = int(input('QUANTOS DIAS ALUGADOS?:'))
km = float(input('QUANTOS KM RODADOS?:'))
pago = (dias * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(pago))
