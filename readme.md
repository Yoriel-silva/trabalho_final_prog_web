# Projeto FastAPI com Docker

Este é um exemplo simples de como configurar um projeto utilizando FastAPI com Docker, incluindo integração com SQLAlchemy para acesso ao banco de dados e Jinja2 para templates HTML.

## Pré-requisitos

Certifique-se de ter o Docker instalado e configurado na sua máquina.

- [Docker](https://docs.docker.com/get-docker/)
- [DockerCompose](https://docs.docker.com/compose/install/)

## Configuração

### Clonar o Repositório

Clone este repositório para sua máquina local:

```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
```

### Construit a imagem docker

Construa a imagem Docker usando o Dockerfile fornecido:

```bash
docker build -t nome_da_imagem .
```

### Executar o Contêiner Docker

Inicie o contêiner Docker usando o docker-compose:

```bash
docker-compose up
```

O servidor FastAPI será iniciado e estará acessível em http://localhost:8000.

### Acessar o Projeto

Index: http://localhost:8000/
Cadastro: http://localhost:8000/cadastro
Login: http://localhost:8000/login
Perfil: http://localhost:8000/perfil

## Estrutura do Projeto
app/
main.py: Configuração do FastAPI, definição de rotas e inicialização do servidor.
Models/: Definição dos modelos de dados utilizando SQLAlchemy.
CRUD/: Operações de criação, leitura, atualização e exclusão (CRUD) no banco de dados.
Templates/: Templates HTML usando Jinja2 para renderização dinâmica.
static/: Arquivos estáticos como CSS, imagens, etc.
requirements.txt: Lista de dependências Python necessárias para o projeto.
Dockerfile: Arquivo de configuração do Docker para construir a imagem do contêiner.
docker-compose.yaml: Arquivo de configuração do Docker Compose para gerenciar múltiplos serviços.

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para enviar pull requests ou abrir issues para discutir recursos, problemas ou melhorias.