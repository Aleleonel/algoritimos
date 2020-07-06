unidades = {
    '0': ' ',
    '1': 'Um ',
    '2': 'Dois',
    '3': 'Tres',
    '4': 'Quatro',
    '5': 'Cinco',
    '6': 'Seis',
    '7': 'Sete',
    '8': 'Oito',
    '9': 'Nove',
    }

dezenas = {
    '1': 'Dez',
    '2': 'Vinte',
    '3': 'Trinta',
    '4': 'Quarenta',
    '5': 'Cinquenta',
    '6': 'Sessenta',
    '7': 'Setenta',
    '8': 'Oitenta',
    '9': 'Noventa',
    }

centenas = {
    '1': 'Cento',
    '2': 'Duzentos',
    '3': 'Trezentos',
    '4': 'Quatrocentos',
    '5': 'Quinhentos',
    '6': 'Seiscentos',
    '7': 'Setecentos',
    '8': 'Oitocentos',
    '9': 'Novecentos',
    }
milhar = {
    '1': 'Mil',
    '2': 'Dois Mil',
    '3': 'Tres Mil',
    '4': 'Quatro Mil',
    '5': 'Cinco Mil',
    '6': 'Seis Mil',
    '7': 'Sete Mil',
    '8': 'Oito Mil',
    '9': 'Nove Mil',
    }

lista = ''
lista2 = ''
lista3 = ''
cont = 0
idx = 0
spell =[]

numero = (input('digite um numero Entre 1 e 2000: '))
tamanho = int(len(numero))

# Caso Milhar então Milhar indx 0:3 cont == 0
if tamanho == 4:
    for k, v in milhar.items():
        milhares = k
        for lm in milhares:
            for n in numero:
                if lm == numero[0] and cont == 0:
                    spell.append(v)
                    cont += 1
                    tamanho -= 1

# Caso Milhar então Centena indx 1:3 cont == 1
if tamanho == 3 and cont == 1:
    for k, v in centenas.items():
        centes = k
        for lc in centes:
            for n in numero:
                if lc == numero[1] and cont == 1:
                    spell.append(v)
                    cont += 1
                    tamanho -= 1

# Caso Centena então indx 0:2 cont == 0
elif tamanho == 3:
    for k, v in centenas.items():
        centes = k
        for lc in centes:
            for n in numero:
                if lc == numero[0] and cont == 0:
                    spell.append(v)
                    cont += 1
                    tamanho -= 1

# Caso Milhar então Dezena indx 2:3 cont == 2
if tamanho == 2 and cont == 2:
    for k, v in dezenas.items():
        dezen = k
        for ld in dezen:
            for n in numero:
                if ld == numero[2] and cont == 2:
                    spell.append(' e ')
                    spell.append(v)
                    cont += 1
                    tamanho -= 1

# Caso Centena então indx 1:2 cont == 1
elif tamanho == 2:
    for k, v in dezenas.items():
        dezen = k
        for l2 in dezen:
            for n in numero:
                if l2 == numero[1] and cont == 1:
                    spell.append(' e ')
                    spell.append(v)
                    cont += 1
                    tamanho -= 1

# Caso Milhar então Dezena indx 3:3 cont == 3
if tamanho == 1 and cont == 3:
    for k, v in unidades.items():
        unida = k
        for lu in unida:
            for n in numero:
                if lu == numero[3] and cont == 3:
                    spell.append(' e ')
                    spell.append(v)
                    cont += 1
                    tamanho -= 1

# Caso Centena então indx 2:2 cont == 2
if tamanho == 1:
    for k, v in unidades.items():
        unida = k
        for lu in unida:
            for n in numero:
                if lu == numero[2] and cont == 2:
                    spell.append(' e ')
                    spell.append(v)
                    cont += 1
                    tamanho -= 1



print(spell)

