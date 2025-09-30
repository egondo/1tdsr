import oracledb

def get_conexao():
    con = oracledb.connect(user="pf0313", password="professor#23", dsn="oracle.fiap.com.br/orcl")
    return con


def insere_cliente(cliente: dict):
    sql = "INSERT INTO t_cliente(nome, email, documento) VALUES(:nome, :email, :documento) RETURNING id into :id"
    with get_conexao() as con:
        with con.cursor() as cur:
            new_var = cur.var(oracledb.NUMBER)
            cliente['id'] = new_var
            cur.execute(sql, cliente)
            cliente['id'] = new_var.getvalue()[0]
        con.commit()

def insere_venda(venda: dict):
    sql = "INSERT INTO t_venda(valor, data, id_cliente) VALUES(:valor, to_date(:data, 'yyyy-mm-dd'), :id_cliente) RETURNING id into :id"
    with get_conexao() as con:
        with con.cursor() as cur:
            new_var = cur.var(oracledb.NUMBER)
            venda['id'] = new_var
            cur.execute(sql, venda)
            venda['id'] = new_var.getvalue()[0]
        con.commit()
        

def insere_itemvenda(itemvenda: dict):
    sql = "INSERT INTO t_itemvenda(valor, produto, quantidade, id_venda) VALUES(:valor, :produto, :quantidade, :id_venda)"
    with get_conexao() as conn:
        with conn.cursor() as cur:    
            cur.execute(sql, itemvenda)
        conn.commit()