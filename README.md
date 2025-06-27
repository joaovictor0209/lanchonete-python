# 🧾 Sistema de Gerenciamento de Lanchonete

Este projeto é um sistema de gerenciamento para uma lanchonete, desenvolvido com Python puro. Ele oferece funcionalidades tanto para **administradores** quanto para **operadores**, permitindo controle de produtos, vendas, estoque, cadastro de funcionários e mais.

---

## 🎯 Objetivo do Projeto

O objetivo é fornecer uma aplicação simples, funcional e modularizada para auxiliar no gerenciamento de uma lanchonete, sem a necessidade de banco de dados, utilizando arquivos `.txt` para persistência dos dados.

---

## ⚙️ Funcionalidades

### 👨‍💼 Administrador
- Cadastrar, editar e excluir produtos
- Cadastrar e editar operadores
- Visualizar produtos e operadores cadastrados
- Ativar/desativar produtos e operadores
- Acompanhar o estoque
- Acompanhar relatórios

### 🧑‍🍳 Operador
- Realizar vendas
- Visualizar histórico de vendas
- Acessar painel do operador
- Consultar dados dos produtos

### 📋 Listagens e Utilitários
- Formulários para entrada de dados
- Verificação de respostas e validações
- Geração de códigos únicos

---

## 🏗️ Estrutura do Projeto

```bash
lanchonete/
├── archive/                # Arquivos com histórico, produtos e membros
├── const/                  # (Reservado para constantes e configurações)
├── functions/              # Lógica principal dividida por domínio
│   ├── admin/              # Funções administrativas
│   ├── operator/           # Funções operacionais
│   └── lists/              # Listagens, formulários e entradas
├── music/                  # Música ambiente opcional
├── __APP__.py              # Arquivo principal do sistema
├── requirements.txt        # Bibliotecas necessárias
└── README.md               # Instruções e informações do projeto
```

---

## 🚀 Como Rodar o Projeto

### 1. Clone o repositório

```bash
git clone https://github.com/joaovictor0209/lanchonete.git
cd lanchonete
```

### 2. Instale as dependências

O projeto utiliza as seguintes bibliotecas externas:
- [questionary](https://github.com/tmbo/questionary) — para criação de interfaces interativas no terminal
- [pygame](https://www.pygame.org/) — para reprodução de música ambiente

Para instalar todas as dependências, execute:

```bash
pip install questionary pygame
```

Ou instale manualmente uma por uma:

```bash
pip install questionary
pip install pygame
```

### 3. Execute o sistema

```bash
python __app__.py
```

---

## 📄 Licença

Este projeto está sob a licença MIT. Sinta-se livre para usá-lo, modificar e distribuir.

---

## 🙋 Autor

Desenvolvido por **João Victor Alexandre Almeida**  
Entre em contato: joaov.alexandre23@gmail.com
