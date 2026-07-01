import tkinter as tk
from tkinter import ttk, messagebox

from database.repo_combustivel import RepositorioCombustivel
from models.combustivel import Gasolina, Diesel, Etanol


class TelaCombustiveis:

    def __init__(self):
        self.repo = RepositorioCombustivel()

        self.janela = tk.Toplevel()
        self.janela.title("Combustíveis")
        self.janela.geometry("600x500")

        tk.Label(
            self.janela,
            text="GERENCIAMENTO DE COMBUSTÍVEIS",
            font=("Arial", 14, "bold")
        ).pack(pady=10)

        frame = tk.Frame(self.janela)
        frame.pack(pady=10)

        tk.Label(frame, text="Tipo:").grid(row=0, column=0)
        self.tipo = ttk.Combobox(frame, values=["Gasolina", "Diesel", "Etanol"], state="readonly")
        self.tipo.grid(row=0, column=1)
        self.tipo.bind("<<ComboboxSelected>>", self.atualizar_opcoes)

        tk.Label(frame, text="Preço litro:").grid(row=1, column=0)
        self.preco = tk.Entry(frame)
        self.preco.grid(row=1, column=1)

        tk.Label(frame, text="Opção:").grid(row=2, column=0)
        self.opcao = ttk.Combobox(frame, state="readonly")
        self.opcao.grid(row=2, column=1)

        tk.Button(frame, text="Cadastrar", command=self.cadastrar).grid(
            row=3, column=0, columnspan=2, pady=5
        )

        tk.Button(frame, text="Remover Selecionado", command=self.remover).grid(
            row=4, column=0, columnspan=2, pady=5
        )

        self.lista = ttk.Treeview(
            self.janela,
            columns=("ID", "TIPO", "PREÇO"),
            show="headings"
        )

        self.lista.heading("ID", text="ID")
        self.lista.heading("TIPO", text="Tipo")
        self.lista.heading("PREÇO", text="Preço/L")

        self.lista.column("ID", width=80)
        self.lista.column("TIPO", width=200)
        self.lista.column("PREÇO", width=120)

        self.lista.pack(fill="both", expand=True, pady=10)

        self.carregar()

    def atualizar_opcoes(self, event=None):
        tipo = self.tipo.get()

        if tipo == "Gasolina":
            self.opcao["values"] = ["Comum", "Aditivada"]
            self.opcao.set("Comum")

        elif tipo == "Diesel":
            self.opcao["values"] = ["Comum", "Aditivado"]
            self.opcao.set("Comum")

        elif tipo == "Etanol":
            self.opcao["values"] = ["Cana", "Milho"]
            self.opcao.set("Cana")

    def cadastrar(self):
        try:
            tipo = self.tipo.get()
            opcao = self.opcao.get()

            valor = self.preco.get().strip()

            if not tipo:
                raise ValueError("Selecione o tipo")

            if not opcao:
                raise ValueError("Selecione a opção")

            if not valor:
                raise ValueError("Digite o preço")

            valor = valor.replace(",", ".")
            preco = float(valor)

            if preco <= 0:
                raise ValueError("Preço inválido")

            if tipo == "Gasolina":
                obj = Gasolina(preco, aditivada=(opcao == "Aditivada"))

            elif tipo == "Diesel":
                obj = Diesel(preco, aditivado=(opcao == "Aditivado"))

            elif tipo == "Etanol":
                obj = Etanol(preco, origem="milho" if opcao == "Milho" else "cana")

            else:
                raise ValueError("Tipo inválido")

            self.repo.inserir(obj)

            self.preco.delete(0, tk.END)
            self.tipo.set("")
            self.opcao.set("")

            self.carregar()

            messagebox.showinfo("OK", "Combustível cadastrado")

        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def remover(self):
        try:
            selecionado = self.lista.focus()

            if not selecionado:
                raise ValueError("Selecione um combustível")

            dados = self.lista.item(selecionado)["values"]
            combustivel_id = dados[0]

            self.repo.remover(combustivel_id)

            self.carregar()

            messagebox.showinfo("OK", "Removido com sucesso")

        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def carregar(self):
        for i in self.lista.get_children():
            self.lista.delete(i)

        dados = self.repo.listar()

        for c in dados:

            tipo = c[1]
            preco = c[2]

            if tipo == "Gasolina":
                tipo = "Gasolina Aditivada" if c[3] else "Gasolina Comum"

            elif tipo == "Diesel":
                tipo = "Diesel Aditivado" if c[3] else "Diesel Comum"

            elif tipo == "Etanol":
                tipo = "Etanol Milho" if c[4] == "milho" else "Etanol Cana"

            self.lista.insert("", "end", values=(c[0], tipo, preco))