from database.conexao import conectar


class RepositorioAbastecimento:

    def inserir(self, ab):
        conn = conectar()
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO abastecimentos (bomba_id, combustivel_id, litros, valor, data)
            VALUES (?, ?, ?, ?, ?)
        """, (
            ab.bomba,
            ab.combustivel,
            ab.litros,
            ab.valor,
            ab.data
        ))

        conn.commit()
        conn.close()

    def listar(self):
        conn = conectar()
        cur = conn.cursor()

        cur.execute("""
            SELECT 
                a.id,
                b.numero,
                c.nome,
                a.litros,
                a.valor,
                a.data
            FROM abastecimentos a
            JOIN bombas b ON b.id = a.bomba_id
            JOIN combustiveis c ON c.id = a.combustivel_id
            ORDER BY a.id DESC
        """)

        dados = cur.fetchall()
        conn.close()
        return dados