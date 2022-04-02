import numpy as np
import random

def inf_2_3aps():
    lista = []
    lista_3aps = []
    with open('Gerador de Ditados/verbos_inf.csv') as file:
        for l in file.readlines():
            lista.append(l[:-1].lstrip())
                
    for x in lista:
        if x[-2:] == 'ar':
            final = 'a'
        elif x[-2:] == 'er' or x[-2:] == 'ir':
            final = 'e'
        lista_3aps.append(x[:-2] + final)
    return lista_3aps

def grava3aps(lista):       
    with open('Gerador de Ditados/verb_3ap.csv', 'w') as file:
        for w in lista:
            file.write(f'{w}, ')

def listador(file_name):
    with open(file_name) as file:
        lista = np.loadtxt(file, delimiter=',', dtype=str)
    for i, w in enumerate(lista):
        lista[i] = w.lstrip().lower()
        
    return lista

if __name__ == '__main__':
    #grava3aps(inf_2_3aps()) #Desmarque e execute para atualizar a 'lista verb_3ap.csv' com base na 'verbos_inf.csv'

    d = int(input('Quantos ditados deseja?\n-'))

    for x in range(d):
        l_animais = random.choice(listador('Gerador de Ditados/animais.csv'))
        l_adjetivos = random.choice(listador('Gerador de Ditados/adjetivos.csv'))
        l_verbos = random.choice(listador('Gerador de Ditados/verb_3ap.csv'))

        if l_animais[-1] == "a" and l_adjetivos[-1] == "o":
            l_adjetivos = l_adjetivos[:-1] + "a"
        elif l_animais[-1] == "a" and l_adjetivos[-2:] == "or":
            l_adjetivos = l_adjetivos[:-1] + "a"
            
        print(l_animais, l_adjetivos, 'não', l_verbos)


    

