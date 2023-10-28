def formatar(req):
    data = str(req)
    dic = data[2:-1].split('&')
    infos = {}

    for dados in dic:
        key, value = dados.split('=')
        infos[key] = value

    return infos

def comparar_petshops(petshops):
        
        menor_valor = float('inf')
        petshop_key = None
        petshop_repetido = []
        petshop_escolhido = None
        distancias = []

        valores = set()
        valores_repetidos = set()

        for petshop in petshops:
            val = petshops[petshop]['valor_dia']
            if val < menor_valor:
                menor_valor = val
                petshop_key = petshop
            if val in valores:
                valores_repetidos.add(val)
                petshop_repetido.append(petshop)
                distancias.append(petshops[petshop]['distancia'])
            else:
                valores.add(val)

        if not valores_repetidos:
            petshop_escolhido = petshop_key
        else:
            i_menor = distancias.index(min(distancias))
            petshop_escolhido = petshop_repetido[i_menor]

        return petshop_escolhido