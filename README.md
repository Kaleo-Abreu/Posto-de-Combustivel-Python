# ⛽ Sistema de Gerenciamento de Posto de Combustível

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?logo=sqlite)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green)

Sistema desenvolvido em **Python**, utilizando **Programação Orientada a Objetos (POO)**, **Tkinter** para a interface gráfica e **SQLite** para persistência dos dados.

O projeto simula o funcionamento de um posto de combustível, permitindo o gerenciamento de combustíveis, bombas e abastecimentos de forma prática e organizada.

---

## 🚀 Funcionalidades

### ⛽ Gerenciamento de Combustíveis

* Cadastro de combustíveis:

  * Gasolina (Comum e Aditivada)
  * Diesel (Comum e Aditivado)
  * Etanol (Cana e Milho)
* Cálculo automático do preço conforme o tipo de combustível.
* Listagem dos combustíveis cadastrados.
* Remoção de combustíveis.

### 🚗 Gerenciamento de Bombas

* Cadastro de bombas de combustível.
* Associação de um combustível à bomba.
* Visualização do combustível associado.
* Identificação das bombas por número e ID.

### 🚙 Abastecimento

* Seleção da bomba.
* Informar a quantidade de litros.
* Cálculo automático do valor total.
* Confirmação antes do registro.
* Armazenamento do abastecimento no banco de dados.

### 📜 Histórico de Abastecimentos

Consulta de todos os abastecimentos realizados, exibindo:

* Bomba utilizada;
* Combustível;
* Quantidade de litros;
* Valor pago;
* Data e hora do abastecimento.

---

## 🏗️ Arquitetura do Projeto

O sistema foi desenvolvido utilizando os princípios da **Programação Orientada a Objetos (POO)** e está organizado em três camadas principais.

### Models

Responsável pelas regras de negócio.

Classes implementadas:

* `Combustivel`
* `Gasolina`
* `Diesel`
* `Etanol`
* `Bomba`
* `Abastecimento`

### Database

Responsável pela persistência dos dados utilizando SQLite.

Contém:

* Conexão com o banco de dados;
* Repositório de Combustíveis;
* Repositório de Bombas;
* Repositório de Abastecimentos.

### Interface Gráfica (GUI)

Desenvolvida com Tkinter.

Telas disponíveis:

* Cadastro de Combustíveis;
* Cadastro de Bombas;
* Abastecimento;
* Histórico de Abastecimentos.

---

## ⚙️ Regras de Negócio

* Gasolina aditivada possui acréscimo no preço.
* Diesel aditivado possui preço diferenciado.
* O preço do etanol varia conforme sua origem (Cana ou Milho).
* Um abastecimento só pode ser realizado caso a bomba possua um combustível associado.

---

## 🗄️ Banco de Dados

O sistema utiliza **SQLite** para armazenar os dados e cria automaticamente as seguintes tabelas:

* `combustiveis`
* `bombas`
* `abastecimentos`

Os relacionamentos entre as tabelas são mantidos por meio de **chaves estrangeiras (Foreign Keys)**.

---

## 🛠️ Tecnologias Utilizadas

* Python 3
* Tkinter
* SQLite
* Programação Orientada a Objetos (POO)

---

## 📂 Estrutura do Projeto

```text
Posto-de-Combustivel-Python/
│
├── database/
│   ├── conexao.py
│   ├── repo_abastecimento.py
│   ├── repo_bomba.py
│   └── repo_combustivel.py
│
├── gui/
│   ├── app.py
│   ├── tela_abastecimento.py
│   ├── tela_bombas.py
│   ├── tela_combustiveis.py
│   └── tela_historico.py
│
├── models/
│   ├── abastecimento.py
│   ├── bomba.py
│   └── combustivel.py
│
├── tests/
│
├── main.py
└── posto.db
```

---

## ▶️ Como Executar

### 1. Clone o repositório

```bash
git clone https://github.com/Kaleo-Abreu/Posto-de-Combustivel-Python.git
```

### 2. Acesse a pasta do projeto

```bash
cd Posto-de-Combustivel-Python
```

### 3. Execute o sistema

```bash
python main.py
```

---

## 🎯 Objetivo

Este projeto foi desenvolvido com fins acadêmicos para aplicar conceitos de:

* Programação Orientada a Objetos (POO);
* Herança e Polimorfismo;
* Interface gráfica com Tkinter;
* Persistência de dados utilizando SQLite;
* Organização do código em camadas;
* Boas práticas de desenvolvimento em Python.
