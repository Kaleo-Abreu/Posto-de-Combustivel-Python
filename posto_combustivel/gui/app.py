import tkinter as tk
from gui.tela_bombas import TelaBombas
from gui.tela_combustiveis import TelaCombustiveis
from gui.tela_abastecimento import TelaAbastecimento
from gui.tela_historico import TelaHistorico


class App:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("POSTO DE COMBUSTÍVEL")
        self.root.geometry("420x320")
        self.root.configure(bg="#1e1e1e")

        tk.Label(
            self.root,
            text="SISTEMA POSTO",
            font=("Arial", 18, "bold"),
            fg="white",
            bg="#1e1e1e"
        ).pack(pady=20)

        tk.Button(self.root, text="Bombas", width=25, command=TelaBombas).pack(pady=5)
        tk.Button(self.root, text="Combustíveis", width=25, command=TelaCombustiveis).pack(pady=5)
        tk.Button(self.root, text="Abastecimento", width=25, command=TelaAbastecimento).pack(pady=5)
        tk.Button(self.root, text="Histórico", width=25, command=TelaHistorico).pack(pady=5)

    def executar(self):
        self.root.mainloop()