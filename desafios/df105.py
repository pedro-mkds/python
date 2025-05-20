def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar situação.
    :return: dicionário com várias informações da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = round(sum(n)/len(n), 2)

    if sit:
        if r['media'] >= 7:
            r['sit'] = 'BOA'
        elif r['media'] >= 5:
            r['sit'] = 'RAZOÁVEL'
        else:
            r['sit'] = 'RUIM'
    return r

resp = notas(5.6, 7.3, 3.9, 5, 10, 8, sit=True)
print(resp)