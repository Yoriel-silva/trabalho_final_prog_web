# Projeto FastAPI

Este é um simples projeto utilizando FastAPI, com uma temática do mundo avatar, que posui um sistema de crud. Ele é conectado a um banco de dados usandoo SQLAlchemy para acesso, além de usar o Jinja2 para templates HTML.

## Pré-requisitos

Certifique-se de ter o Pytho instalado, as bibliotecas necessária e configurado na sua máquina.

[python](https://www.python.org/downloads/)

Para Instalar as bibliotecas necessárias, use o seguinte comando ápos fazer o clone do repositório para sua máquina

```bash
pip install -r requirements.txt
```

## Configuração

### Clonar o Repositório

Clone este repositório para sua máquina local:

```bash
git clone https://github.com/Yoriel-silva/trabalho_final_prog_web
cd trabalho_final_prog_web
```

### Execute o app.py
```bash
python app.py
```

O servidor FastAPI será iniciado e estará acessível em http://localhost:8000.

### Acessar o Projeto

Index: http://localhost:8000/

Cadastro: http://localhost:8000/cadastro

Login: http://localhost:8000/login

Perfil: http://localhost:8000/perfil

## Estrutura do Projeto
main.py: Configuração do FastAPI, definição de rotas e inicialização do servidor.

Models/: Definição dos modelos de dados utilizando SQLAlchemy.

CRUD/: Operações de criação, leitura, atualização e exclusão (CRUD) no banco de dados.

Templates/: Templates HTML usando Jinja2 para renderização dinâmica.

static/: Arquivos estáticos como CSS, imagens, etc.

requirements.txt: Lista de dependências Python necessárias para o projeto.

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para enviar pull requests ou abrir issues para discutir recursos, problemas ou melhorias.
