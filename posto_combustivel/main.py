from database.conexao import criar_tabelas
from gui.app import App

if __name__ == "__main__":
    criar_tabelas()
    App().executar()