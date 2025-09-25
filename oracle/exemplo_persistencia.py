#instalar driver do oracle
#pip install oracledb

import oracledb

def get_conexao() -> oracledb.Connection:
    con = oracledb.connect(user="pf0313", password="professor#23", dsn="oracle.fiap.com.br:1521/orcl")
    return con

def altera_pessoa(id, nome):
    with get_conexao() as con:
        with con.cursor() as cursor:
            sql = f"update tb_pessoa set nome='{nome}' where id={id}"
            cursor.execute(sql)
        con.commit()
    



def insere_jogo(jogo: dict) -> None:
    with get_conexao() as con:
        with con.cursor() as cursor:
            sql = "insert into jogo (nome, plataforma, genero, classificacao, desenvolvedor) values (:nome, :plataforma, :genero, :classificacao, :desenvolvedor)"
            cursor.execute(sql, jogo)
        con.commit()


def altera_jogo(jogo: dict) -> None:
    with get_conexao() as con:
        with con.cursor() as cursor:
            sql = "update jogo set nome=:nome, plataforma=:plataforma, genero=:genero, classificacao=:classificacao, desenvolvedor=:desenvolvedor where id=:id"
            cursor.execute(sql, jogo)
        con.commit()

def recupera() -> list:
    jogos = []
    with get_conexao() as con:
        with con.cursor() as cursor:
            sql = "SELECT id, nome, plataforma, genero, classificacao, desenvolvedor FROM jogo ORDER BY nome"
            cursor.execute(sql)
            for linha in cursor:
                jogo = {
                    "id": linha[0],
                    "nome": linha[1],
                    "plataforma": linha[2],
                    "genero": linha[3],
                    "classificacao": linha[4],
                    "desenvolvedor": linha[5]
                }
                jogos.append(jogo)
    return jogos


if __name__ == "__main__":

    nome = input("Digite o nome: ")
    id = input("Digite o id: ")

    altera_pessoa(id, nome)




'''game = {
        "nome": "River Raid",
        "plataforma": "Atari",
        "genero": "Guerra",
        "classificacao": 10,
        "desenvolvedor": "Activision" 
    }
    insere_jogo(game)
    print("Jogo inserido com sucesso!")

    resultados = recupera()
    for jogo in resultados:
        print(jogo)
'''