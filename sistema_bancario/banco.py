import oracledb

def get_conexao():
    con = oracledb.connect(user="pf0313", password="professor#23", dsn="oracle.fiap.com.br/orcl")
    return con

def recupera_contas() -> list:
    with get_conexao() as con:
        with con.cursor() as cur:
            sql = "SELECT id, numero, agencia, cliente, saldo FROM tr_conta ORDER by cliente"

            cur.execute(sql)
            resultados = cur.fetchall()
    return resultados

def insere_lancamento(lancamento: dict):
    with get_conexao() as con:
        with con.cursor() as cur:
            sql = "INSERT into tr_lancamento(tipo, data, observacao, valor, conta_id) VALUES(:tipo, sysdate, :observacao, :valor, :conta_id)"

            cur.execute(sql, lancamento)
        con.commit()

def recupera_lancamentos(conta_id) -> list:
    with get_conexao() as con:
        with con.cursor() as cur:   
            sql = "SELECT tipo, data, observacao, valor FROM tr_lancamento WHERE conta_id= :conta_id ORDER BY data DESC"

            param = {"conta_id": conta_id}
            cur.execute(sql, param)
            
            resultados = cur.fetchall()
    return resultados


def atualiza_saldo(info: dict):
    with get_conexao() as con:
        with con.cursor() as cur:   
            sql = "UPDATE tr_conta SET saldo = saldo + :valor WHERE id=:id"

            cur.execute(sql, info)
        con.commit()