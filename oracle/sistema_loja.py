import banco

def cadastra_venda(cliente: dict, venda: dict):
    banco.insere_cliente(cliente)
    
    venda['id_cliente'] = cliente['id']
    itens = venda['itens']
    venda.pop('itens')
    banco.insere_venda(venda)

    for reg in itens:
        reg['id_venda'] = venda['id']
        banco.insere_itemvenda(reg)
    


cliente = {
    "nome": "José Bonifácio",
    "documento": "824.928.092-66",
    "email": "boni@gmail.com"
}

venda = {
    "valor": 1212.50,
    "data": "2025-09-28",
    "itens": [
        {"produto": "mouse", "quantidade": 3, "valor": 186.90},
        {"produto": "nvme", "quantidade": 1, "valor": 250.80},
        {"produto": "memória", "quantidade": 2, "valor": 200.50}
    ]
}

cadastra_venda(cliente, venda)