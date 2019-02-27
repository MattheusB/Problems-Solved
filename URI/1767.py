# https://www.urionlinejudge.com.br/judge/pt/problems/view/1767

def captura_peso(matrix):
    w = 50
    while(matrix[len(matrix)-1][w] == matrix[len(matrix)-1][w-1]):
        w -= 1

    return w

def itens_picados(matrix_f,pac):
    qtd_itens = len(pac)
    w = 50
    qtd_itens_usados = 0
    while(qtd_itens > 0):
        if(matrix_f[qtd_itens][w]):
            w -= pac[qtd_itens-1][1]
            qtd_itens_usados += 1
        qtd_itens -= 1

    return qtd_itens_usados


def preenche_matrix(pac):
    w = 50
    matrix = []
    matrix_f = [] # matrix com flag de itens picados
    for i in xrange(len(pacotes)+1):
        matrix.append([])
        matrix_f.append([])
        for j in xrange(w+1):
            if(i==0):
                matrix[i].append(0)
                matrix_f[i].append(False)
            elif(j==0):
                matrix[i].append(0)
                matrix_f[i].append(False)
            elif(j >= pac[i-1][1] and # matrix[i-1][j-pacotes[i-1]] == bolsa sem o peso deste item
                    matrix[i-1][j - pac[i-1][1]] + pac[i-1][0] >= matrix[i-1][j]):
                    # fazer isso para verificar se o item foi incluso ate o final da lista.
                matrix[i].append(matrix[i-1][j - pac[i-1][1]] + pac[i-1][0])
                matrix_f[i].append(True)
            else:
                matrix[i].append(matrix[i-1][j])
                matrix_f[i].append(False)

    print '%d brinquedos' % matrix[len(matrix)-1][w]
    print 'Peso: %d kg' % captura_peso(matrix)
    print 'sobra(m) %d pacote(s)' % (len(pac) - itens_picados(matrix_f,pac))

    return

qtd = int(raw_input())

for i in xrange(qtd):
    pcts = int(raw_input())
    pacotes = []
    for i in xrange(pcts):
        pct = map(int, raw_input().split()) # quantidade peso
        pacotes.append(pct)
    
    preenche_matrix(pacotes)
    print ''
