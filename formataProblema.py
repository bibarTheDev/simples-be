def __formataObjetivo(objetivo):
    #TODO: remover
    objetivo = objetivo.replace(' ', '')

    result = {}

    # separa em termos
    for termo in objetivo.split('+'):
        # separa cada termo em variavel e coef
        termo = termo.split('*')
        result[termo[1]] = float(termo[0])

    return result


def __formataRestricao(restricao):
    #TODO: remover
    restricao = restricao.replace(' ', '')

    result = {
        'termos': {},
        'sinal': '',
        'termoIndependente': ''
    }

    # separa o sinal
    for sinal in ['<=', '>=', '=']:
        # quando encontra o sinal certo
        if sinal in restricao:
            restricao = restricao.split(sinal)

            # separa elementos
            result['sinal'] = sinal
            termos = restricao[0]
            result['termoIndependente'] = float(restricao[1])

            break

    # separa em termos
    for termo in termos.split('+'):
        # separa cada termo em variavel e coef
        termo = termo.split('*')
        result['termos'][termo[1]] = float(termo[0])

    return result


def __formataRestricaoVar(restricao):
    #TODO: remover
    return restricao.replace(' ', '')


def formataProblema(problema):
    problema['objetivo'] = __formataObjetivo(problema['objetivo'])
    problema['restricoes'] = [__formataRestricao(r) for r in problema['restricoes']]
    problema['restricoesVars'] = [__formataRestricaoVar(r) for r in problema['restricoesVars']]