import oracledb

def get_conexao():
    return oracledb.connect(user="pf0313", password='professor#23', dsn="oracle.fiap.com.br/orcl")

def consulta_carros():
    with get_conexao() as conn:
        with conn.cursor() as cur:
            sql = "SELECT id, montadora, modelo, ano, placa FROM carro order by montadora"
            cur.execute(sql)
            dados = cur.fetchall()
            resp = []
            for reg in dados:    
                info = {
                    "id": reg[0],
                    "montadora": reg[1],
                    "modelo": reg[2],
                    "ano": reg[3],
                    "placa": reg[4]
                }
                resp.append(info)
            return resp


if __name__ == "__main__":
    dados = consulta_carros()
    for reg in dados:
        print(reg)            