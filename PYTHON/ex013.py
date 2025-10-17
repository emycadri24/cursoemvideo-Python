salario = float(input('Qual é o salario do funcionario?'))
novo = salario + (salario * 2 / 100)
print('UM FUNCIONARIO QUE GANHAVA R%{:.2f}, COM 2% DE AUMENTO, PASSA A RECEBER R${:.2f})'.format(salario, novo))