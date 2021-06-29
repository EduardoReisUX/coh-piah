import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentença'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

################
def separa_caracteres(palavras):
    '''A função recebe uma palavra e devolve uma lista de todas letras dentro dela'''
    return list(palavras)
    
###############
def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    
    novas_frases = []
    novas_palavras = []
    caracteres = []
    sentencas = separa_sentencas(texto)

    soma_car_sentencas = 0
    
    for sent in sentencas:
        novas_frases += separa_frases(sent)
    for frases in novas_frases:    
        novas_palavras += separa_palavras(frases)
    for palavras in novas_palavras:
        caracteres += (separa_caracteres(palavras))

    frases = []
    num_sentencas = 0
    for i in range(len(sentencas)):
        frase_aux = separa_frases(sentencas[i])
        frases.append(frase_aux)
        num_sentencas += 1
        soma_car_sentencas = soma_car_sentencas + len(sentencas[i])

    palavras = []
    soma_car_frases = 0
    for linha in range(len(frases)):
        for coluna in range(len(frases[linha])):
            palavras_aux = separa_palavras(frases[linha][coluna])
            palavras.append(palavras_aux)
            soma_car_frases += len(frases[linha][coluna])


    tamanho_médio_palavras = len(caracteres) / len(novas_palavras)
    type_token = n_palavras_diferentes(novas_palavras) / len(novas_palavras)
    hapax_legomana = n_palavras_unicas(novas_palavras) / len(novas_palavras)

    tamanho_médio_sentencas = soma_car_sentencas / len(sentencas)
    complexidade_sentencas = len(novas_frases) / len(sentencas)
    tamanho_médio_frases = soma_car_frases / len(novas_frases)

    return [tamanho_médio_palavras, type_token, hapax_legomana, tamanho_médio_sentencas, complexidade_sentencas, tamanho_médio_frases]

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''

    diferenca = 0
    for i in range(len(as_a)):
        diferenca += abs(as_a[i] - as_b[i])
    
    similaridade_assinatura = diferenca / 6
    if (similaridade_assinatura < 0): similaridade_assinatura *= (-1) 

    return similaridade_assinatura

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''

    ass_cp_aux = ass_cp
    similaridade_menor_grau = 99999
    contador = 0

    for texto in textos:  
        assinatura_atual = calcula_assinatura(texto)
        similaridade = compara_assinatura(assinatura_atual, ass_cp_aux)
        contador += 1

        if similaridade < similaridade_menor_grau:
            similaridade_menor_grau = similaridade
            texto_infectado = contador
            
    return texto_infectado