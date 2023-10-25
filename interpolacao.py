email_tmp = """
Olá, %(nome)s.
Tem interesse em comprar %(produto)s?
Este produto é ótimo para %(texto)s
Clique em %(link)s para comprar.
Restão só %(quantidade)d unidades
Preço promocional, apenas %(preco).2f reais.
"""

clientes = ["Maria","João","Lucas"]

for cliente in clientes:
    print(
        email_tmp %{
            "nome":clientes,
            "produto":"caneta",
            "texto":"Escrever lindos textos",
            "link":"https://canetaslegais.com",
            "quantidade":1,
            "preco":10.0
        }
    )