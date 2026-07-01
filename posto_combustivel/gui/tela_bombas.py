import tkinter as tk
from tkinter import ttk, messagebox

from database.repo_bomba import RepositorioBomba
from database.repo_combustivel import RepositorioCombustivel


class TelaBombas:

    def __init__(self):
        self.repo = RepositorioBomba()
        self.repo_comb = RepositorioCombustivel()

        self.janela = tk.Toplevel()
        self.janela.title("Cadastro de Bombas")
        self.janela.geometry("650x500")

        tk.Label(
            self.janela,
            text="GERENCIAMENTO DE BOMBAS",
            font=("Arial", 14, "bold")
        ).pack(pady=10)

        frame = tk.Frame(self.janela)
        frame.pack(pady=10)

        tk.Label(frame, text="Número da Bomba:").grid(row=0, column=0)
        self.numero_entry = tk.Entry(frame)
        self.numero_entry.grid(row=0, column=1)

        tk.Button(
            frame,
            text="Cadastrar Bomba",
            command=self.cadastrar
        ).grid(row=1, column=0, columnspan=2, pady=5)

        tk.Label(frame, text="Combustível:").grid(row=2, column=0)
        self.combo_comb = ttk.Combobox(frame, state="readonly")
        self.combo_comb.grid(row=2, column=1)

        tk.Button(
            frame,
            text="Associar Combustível",
            command=self.associar
        ).grid(row=3, column=0, columnspan=2, pady=5)

        self.lista = ttk.Treeview(
            self.janela,
            columns=("ID", "NUMERO", "COMBUSTIVEL"),
            show="headings"
        )

        self.lista.heading("ID", text="ID")
        self.lista.heading("NUMERO", text="Número")
        self.lista.heading("COMBUSTIVEL", text="Combustível")

        self.lista.column("ID", width=60)
        self.lista.column("NUMERO", width=120)
        self.lista.column("COMBUSTIVEL", width=300)

        self.lista.pack(fill="both", expand=True, pady=10)

        tk.Button(
            self.janela,
            text="Selecionar Bomba",
            command=self.selecionar
        ).pack(pady=5)

        self.carregar_combustiveis()
        self.carregar()

    def carregar_combustiveis(self):
        dados = self.repo_comb.listar()

        self.map_comb = {}
        valores = []

        for c in dados:
            tipo = c[1]
            preco = c[2]

            if tipo == "Gasolina":
                nome = "Gasolina Aditivada" if c[3] else "Gasolina Comum"
            elif tipo == "Diesel":
                nome = "Diesel Aditivado" if c[3] else "Diesel Comum"
            elif tipo == "Etanol":
                nome = "Etanol Milho" if c[4] == "milho" else "Etanol Cana"
            else:
                nome = tipo

            texto = f"{nome} - R$ {preco}"

            self.map_comb[texto] = c[0]
            valores.append(texto)

        self.combo_comb["values"] = valores

    def cadastrar(self):
        try:
            numero = int(self.numero_entry.get())

            if numero <= 0:
                raise ValueError("Número inválido")

            bomba = type("B", (), {"numero": numero, "combustivel": None})

            self.repo.inserir(bomba)

            self.numero_entry.delete(0, tk.END)

            self.carregar()

            messagebox.showinfo("OK", "Bomba cadastrada")

        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def associar(self):
        try:
            selecionado = self.lista.focus()

            if not selecionado:
                raise ValueError("Selecione uma bomba")

            dados = self.lista.item(selecionado)["values"]
            bomba_id = dados[0]

            comb_nome = self.combo_comb.get()

            if not comb_nome:
                raise ValueError("Selecione um combustível")

            combustivel_id = self.map_comb[comb_nome]

            self.repo.associar_combustivel(bomba_id, combustivel_id)

            self.carregar()

            messagebox.showinfo("OK", "Combustível associado")

        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def carregar(self):
        for item in self.lista.get_children():
            self.lista.delete(item)

        bombas = self.repo.listar()

        for b in bombas:

            combustivel = "SEM COMBUSTÍVEL"

            if len(b) > 2 and b[2]:

                tipo = b[5] if len(b) > 5 else None
                aditivado = b[6] if len(b) > 6 else None
                origem = b[7] if len(b) > 7 else None

                if tipo == "Gasolina":
                    combustivel = "Gasolina Aditivada" if aditivado else "Gasolina Comum"
                elif tipo == "Diesel":
                    combustivel = "Diesel Aditivado" if aditivado else "Diesel Comum"
                elif tipo == "Etanol":
                    combustivel = "Etanol Milho" if origem == "milho" else "Etanol Cana"
                else:
                    combustivel = tipo

            self.lista.insert("", "end", values=(b[0], b[1], combustivel))

    def selecionar(self):
        selecionado = self.lista.focus()

        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione uma bomba")
            return

        dados = self.lista.item(selecionado)["values"]

        messagebox.showinfo(
            "Bomba Selecionada",
            f"ID: {dados[0]}\nNúmero: {dados[1]}\nCombustível: {dados[2]}"
        )