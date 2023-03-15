import re

def buildQuery(query : str, args : dict):
    if len(re.findall("{[a-z0-9]+}", query)) == len(args):
        return query.format_map(args)
    else:
        raise Exception("O número de argumentos informados e contidos na query está divergente")

def requestQueryArgs() -> dict:
    argsDict = dict()
    
    print("Escreva os pares chave-valor para alterar na query, separando a chave do valor por pipe (|)\ne os pares por espaço\nEx: teste1|1 teste2|2")
    argsInput = input("")

    for args in argsInput.split(" "):
        args = args.split("|")
        argsDict.update({args[0]: args[1]})

    return argsDict