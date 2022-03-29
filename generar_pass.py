import random

def generar_pass():
    mayusculas = ['A','B','C','D','E','F','G','H','I',
    'J','K','L','M','N','O','P','Q','R',
    'S','T','U','V','W','X','Y','Z']
    minusculas = ['a','b','c','d','e','f','g','h','i',
    'j','k','l','m','n','o','p','q','r',
    's','t','u','v','w','x','y','z']
    simbolos = ['!','#','$','%','&','/','(',')','=',
    '?','+','*','}',']','{','[',';',':',
    '.','-','°','|','~','@']
    numeros = ['1','2','3','4','5','6','7','8','9','0']

    caracteres = mayusculas + minusculas + simbolos + numeros
    variable_pass = []

    for i in range(15):
        caracter_random = random.choice(caracteres)
        variable_pass.append(caracter_random)
    variable_pass = ''.join(variable_pass)
    return variable_pass

def run():
    variable_pass = generar_pass()
    print('Contraseña generada exitosamente!')
    print(f'Tu contraseña aleatoria es: {variable_pass}')

if __name__ == '__main__':
    run()
