import tkinter as tk
from tkinter import ttk

from database.repo_abastecimento import RepositorioAbastecimento


class TelaHistorico:

    def __init__(self):
        self.repo = RepositorioAbastecimento()

        self.janela = tk.Toplevel()
        self.janela.title("Histórico")
        self.janela.geometry("600x400")

        tk.Label(self.janela, text="HISTÓRICO DE ABASTECIMENTOS", font=("Arial", 14, "bold")).pack(pady=10)

        self.lista = ttk.Treeview(
            self.janela,
            columns=("ID", "BOMBA", "COMBUSTIVEL", "LITROS", "VALOR", "DATA"),
            show="headings"
        )

        self.lista.heading("ID", text="ID")
        self.lista.heading("BOMBA", text="Bomba")
        self.lista.heading("COMBUSTIVEL", text="Combustível")
        self.lista.heading("LITROS", text="Litros")
        self.lista.heading("VALOR", text="Valor")
        self.lista.heading("DATA", text="Data")

        self.lista.pack(fill="both", expand=True)

        self.carregar()

    def carregar(self):
        for i in self.lista.get_children():
            self.lista.delete(i)

        dados = self.repo.listar()

        for d in dados:
            self.lista.insert("", "end", values=d)