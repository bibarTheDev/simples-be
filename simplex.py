from formataProblema import formataProblema
from normalizaProblema import normalizaProblema

def simplex(problema):
    print(problema)
    formataProblema(problema)
    print(problema)
    normalizaProblema(problema)
    print(problema)

    return problema