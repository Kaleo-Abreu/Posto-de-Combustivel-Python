from database.conexao import conectar

class RepositorioCombustivel:

    def inserir(self, c):
        conn = conectar()
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO combustiveis (nome, preco, tipo, aditivada, origem)
            VALUES (?, ?, ?, ?, ?)
        """, (
            c.nome,
            c.preco_litro,
            type(c).__name__,
            getattr(c, "aditivada", None),
            getattr(c, "origem", None)
        ))

        conn.commit()
        conn.close()

    def listar(self):
        conn = conectar()
        cur = conn.cursor()

        cur.execute("SELECT * FROM combustiveis")
        rows = cur.fetchall()

        conn.close()
        return rows
    
    def remover(self, id):
        conn = conectar()
        cur = conn.cursor()

        cur.execute("DELETE FROM combustiveis WHERE id = ?", (id,))

        conn.commit()
        conn.close()