import tkinter as tk
from tkinter import ttk, messagebox

from database.repo_bomba import RepositorioBomba
from database.repo_abastecimento import RepositorioAbastecimento
from models.combustivel import Gasolina, Diesel, Etanol
from models.abastecimento import Abastecimento


class TelaAbastecimento:

    def __init__(self):
        self.repo_bomba = RepositorioBomba()
        self.repo_abast = RepositorioAbastecimento()

        self.janela = tk.Toplevel()
        self.janela.title("Abastecimento")
        self.janela.geometry("520x420")

        tk.Label(self.janela, text="ABASTECIMENTO", font=("Arial", 16, "bold")).pack(pady=10)

        self.combo_bombas = ttk.Combobox(self.janela, state="readonly")
        self.combo_bombas.pack(pady=5)

        self.litros = tk.Entry(self.janela)
        self.litros.pack(pady=5)

        self.valor_label = tk.Label(self.janela, text="Valor: R$ 0.00", font=("Arial", 12, "bold"))
        self.valor_label.pack(pady=10)

        tk.Button(self.janela, text="CALCULAR", command=self.calcular).pack(pady=5)
        tk.Button(self.janela, text="CONFIRMAR", command=self.confirmar).pack(pady=5)

        self.carregar()

    def carregar(self):
        bombas = self.repo_bomba.listar()

        self.map_bombas = {f"Bomba {b[1]}": b[0] for b in bombas}
        self.combo_bombas["values"] = list(self.map_bombas.keys())

    def obter_combustivel(self, bomba_id):
        dados = self.repo_bomba.buscar_por_id(bomba_id)

        if not dados or not dados[2]:
            return None

        tipo = dados[5]
        preco = dados[4]

        if tipo == "Gasolina":
            return Gasolina(preco, bool(dados[6]))

        if tipo == "Diesel":
            return Diesel(preco, bool(dados[6]))

        return Etanol(preco, dados[7] or "cana")

    def calcular(self):
        try:
            if not self.combo_bombas.get():
                raise ValueError("Selecione uma bomba")

            litros = float(self.litros.get())

            if litros <= 0:
                raise ValueError("Litros inválidos")

            bomba_id = self.map_bombas[self.combo_bombas.get()]
            combustivel = self.obter_combustivel(bomba_id)

            if not combustivel:
                raise ValueError("Bomba sem combustível associado")

            self.valor = combustivel.calcular_valor(litros)

            self.valor_label.config(text=f"Valor: R$ {self.valor:.2f}")

        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def confirmar(self):
        try:
            if not hasattr(self, "valor"):
                raise ValueError("Clique em CALCULAR primeiro")

            if not self.combo_bombas.get():
                raise ValueError("Selecione uma bomba")

            bomba_id = self.map_bombas[self.combo_bombas.get()]
            litros = float(self.litros.get())

            dados = self.repo_bomba.buscar_por_id(bomba_id)

            if not dados or not dados[2]:
                raise ValueError("Bomba sem combustível associado")

            combustivel_id = dados[2]

            ab = Abastecimento(
                bomba_id,
                combustivel_id,
                litros,
                self.valor
            )

            self.repo_abast.inserir(ab)

            messagebox.showinfo("OK", f"R$ {self.valor:.2f}")

            self.litros.delete(0, tk.END)
            self.valor_label.config(text="Valor: R$ 0.00")

            del self.valor

        except Exception as e:
            messagebox.showerror("Erro", str(e))