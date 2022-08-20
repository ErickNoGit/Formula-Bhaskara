import math

print("Se for digitar um número real coloque ponto. exemplo : 1.0 ao invés de 1,0")
print("O operador do código aceita números negativos")
# entrada de dados
a = float(input("digite o valor de A: "))
b = float(input("digite o valor de B: "))
c = float(input("digite o valor de C: "))
# fórmula de delta
delta = (b)**2 - 4*(a)*(c)
print('delta é :')
print(delta)
if delta == 0:
    print("Quando o discriminante é igual à zero a equação de 2º grau apresenta duas raízes reais iguais")
    print("calculamos X1 primeiro, que opera a fórmula de Bhaskar positivamente e X2 que opera negativamente")
    # operador de radiação da biblioteca math
    r = math.sqrt(delta)
    x_um_positivo = (-b + r)/(2*a)
    x_um_negativo = (-b - r)/(2*a)
    print('X1 é :')
    print(x_um_positivo)
    print('X2 é :')
    print(x_um_negativo)
else:
    if delta > 0:
        print("Quando o valor do discriminante é maior que zero, a equação apresenta duas raízes reais diferentes.")
        print("calculamos X1 primeiro, que opera a fórmula de Bhaskara positivamente e X2 que opera negativamente")
        # operador de radiação da biblioteca math
        r = math.sqrt(delta)
        x_um_positivo = (-b + r)/(2*a)
        x_um_negativo = (-b - r)/(2*a)
        print('X1 é :')
        print(x_um_positivo)
        print('X2 é :')
        print(x_um_negativo)
    else:
        if delta < 0:
            print("Quando o discriminante é menor que zero, não existem raízes reais na radiação")