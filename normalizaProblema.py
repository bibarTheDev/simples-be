BIGVALUE = 9999999.0

def __addVarAux(problema, coef, restr):
    problema['variaveis'] += 1

    var = 'x' + str(problema['variaveis'])

    # add var ao objetivo
    problema['objetivo'][var] = 0

    # add var as restricoes
    for r in problema['restricoes']:
        # restricao que utiliza a var aux
        if r is restr:
            r['termos'][var] = coef
        # outras restricoes
        else:
            r['termos'][var] = 0


def __addVarArt(problema, coef, restr):
    problema['variaveis'] += 1

    var = 'x' + str(problema['variaveis'])

    # add var ao objetivo
    problema['objetivo'][var] = BIGVALUE

    # add var as restricoes
    for r in problema['restricoes']:
        # restricao que utiliza a var aux
        if r is restr:
            r['termos'][var] = coef
        # outras restricoes
        else:
            r['termos'][var] = 0


def normalizaProblema(problema):
    # prepara variaveis auxiliares
    problema['variaveis'] = len(problema['objetivo'])
    problema['variaveisNaturais'] = problema['variaveis']

    # adiciona variaveis auxiliares
    for r in problema['restricoes']:
        if r['sinal'] == '<=':
            # add var de folga
            __addVarAux(problema, 1, r)

        elif r['sinal'] == '>=':
            # add var de falta (negativa)
            __addVarAux(problema, -1, r)

            # add var art
            __addVarArt(problema, 1, r)

        elif r['sinal'] == '=':
            # add var art
            __addVarArt(problema, 1, r)

    # normaliza objetivo
    if not problema['minimizar']:
        for k, v in problema['objetivo'].items():
            problema['objetivo'][k] *= -1