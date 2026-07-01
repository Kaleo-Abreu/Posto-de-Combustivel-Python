# ⛽ Sistema de Gerenciamento de Posto de Combustível

Sistema desenvolvido em **Python**, utilizando **Programação Orientada a Objetos (POO)**, **Tkinter** para a interface gráfica e **SQLite** para persistência dos dados.

O objetivo do projeto é simular o funcionamento de um posto de combustível, permitindo o gerenciamento de combustíveis, bombas e abastecimentos de forma simples, organizada e intuitiva.

## 📋 Funcionalidades

### 🚗 Gerenciamento de Combustíveis

* Cadastro de combustíveis:

  * Gasolina (Comum e Aditivada)
  * Diesel (Comum e Aditivado)
  * Etanol (Cana e Milho)
* Cálculo automático do preço conforme o tipo de combustível.
* Listagem dos combustíveis cadastrados.
* Remoção de combustíveis.

### ⛽ Gerenciamento de Bombas

* Cadastro de bombas de combustível.
* Associação de um combustível à bomba.
* Visualização do combustível associado.
* Identificação das bombas por ID e número.

### 🚙 Abastecimento

* Seleção da bomba utilizada.
* Informar a quantidade de litros.
* Cálculo automático do valor total do abastecimento.
* Confirmação antes do registro.
* Armazenamento do abastecimento no banco de dados.

### 📜 Histórico de Abastecimentos

Visualização de todos os abastecimentos registrados contendo:

* Bomba utilizada;
* Combustível;
* Quantidade de litros;
* Valor pago;
* Data e hora.

## 🏗️ Arquitetura do Projeto

O sistema foi desenvolvido utilizando Programação Orientada a Objetos (POO) e está organizado em três camadas principais.

### Models

Responsável pelas regras de negócio.

Classes implementadas:

* `Combustivel` (classe base)
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

Desenvolvida com Tkinter, composta pelas seguintes telas:

* Cadastro de Combustíveis;
* Cadastro de Bombas;
* Abastecimento;
* Histórico de Abastecimentos.

## ⚙️ Regras de Negócio

* Gasolina aditivada possui acréscimo no preço.
* Diesel aditivado possui preço diferenciado.
* O preço do etanol varia conforme sua origem:

  * Cana;
  * Milho.
* Um abastecimento só pode ser realizado se a bomba possuir um combustível associado.

## 🗄️ Banco de Dados

O sistema utiliza **SQLite** e cria automaticamente as seguintes tabelas:

* `combustiveis`
* `bombas`
* `abastecimentos`

Os relacionamentos entre as entidades são mantidos por meio de **chaves estrangeiras (Foreign Keys)**.

## 🛠️ Tecnologias Utilizadas

* Python 3
* Tkinter
* SQLite
* Programação Orientada a Objetos (POO)

## 🚀 Como Executar

1. Clone este repositório:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```

2. Acesse a pasta do projeto:

```bash
cd seu-repositorio
```

3. Execute o sistema:

```bash
python main.py
```

## 📁 Estrutura do Projeto

```text
📦 projeto
├── database/
├── models/
├── views/
├── main.py
└── README.md
```

## 🎯 Objetivo

Este projeto foi desenvolvido com fins acadêmicos para aplicar conceitos de:

* Programação Orientada a Objetos (POO);
* Herança e Polimorfismo;
* Interface gráfica com Tkinter;
* Persistência de dados com SQLite;
* Organização em camadas;
* Boas práticas de desenvolvimento em Python.
