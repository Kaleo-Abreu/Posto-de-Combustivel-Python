from database.conexao import conectar

class RepositorioBomba:

    def inserir(self, bomba):
        conn = conectar()
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO bombas (numero, combustivel_id) VALUES (?, ?)",
            (bomba.numero, None)
        )

        conn.commit()
        conn.close()

    def listar(self):
        conn = conectar()
        cur = conn.cursor()

        cur.execute("""
            SELECT b.id, b.numero, c.id, c.nome, c.preco
            FROM bombas b
            LEFT JOIN combustiveis c ON c.id = b.combustivel_id
        """)

        data = cur.fetchall()
        conn.close()
        return data

    def associar(self, bomba_id, combustivel_id):
        conn = conectar()
        cur = conn.cursor()

        cur.execute("""
            UPDATE bombas
            SET combustivel_id = ?
            WHERE id = ?
        """, (combustivel_id, bomba_id))

        conn.commit()
        conn.close()

    def buscar_por_id(self, id):
        conn = conectar()
        cur = conn.cursor()

        cur.execute("""
            SELECT 
                b.id,
                b.numero,
                c.id,
                c.nome,
                c.preco,
                c.tipo,
                c.aditivada,
                c.origem
            FROM bombas b
            LEFT JOIN combustiveis c ON c.id = b.combustivel_id
            WHERE b.id = ?
        """, (id,))

        dado = cur.fetchone()
        conn.close()
        return dado
    
    def associar_combustivel(self, bomba_id, combustivel_id):
        conn = conectar()
        cur = conn.cursor()

        cur.execute("""
            UPDATE bombas
            SET combustivel_id = ?
            WHERE id = ?
        """, (combustivel_id, bomba_id))

        conn.commit()
        conn.close()

    def buscar_por_id(self, id):
        conn = conectar()
        cur = conn.cursor()

        cur.execute("""
            SELECT b.id, b.numero, c.id, c.nome, c.preco, c.tipo, c.aditivada, c.origem
            FROM bombas b
            LEFT JOIN combustiveis c ON c.id = b.combustivel_id
            WHERE b.id = ?
        """, (id,))

        resultado = cur.fetchone()
        conn.close()
        return resultado