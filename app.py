#Importações necessárias - bibliotecas
import uvicorn

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
#Importações necessárias - arquivos internos
from Models.models import Usuario
from CRUD.crud import create, read, update, delete

#Conexão com Base de dados
db = create_engine("sqlite:///base.db", echo=True)

#Criar sessão
Session = sessionmaker(bind=db)

#Definição FastAPI
api = FastAPI()

#Token para validações de usuário - extra
SECRET_KEY = "12345"
api.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)

#Uso de templetas HTML
templates = Jinja2Templates(directory="Templates")

#Conexão com arquivos necessários
api.mount("/static", StaticFiles(directory="static"), name="static")

#Rotas da API
#Rota Pagina Index
@api.get('/index', response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request,})
 
#Rota Pagina de Cadastro
@api.get('/cadastro', response_class=HTMLResponse)
def cadastro(request: Request, elemento: str = ''):
    message = request.session.pop('message', None) #Recupera uma mensagem armazenada na sessão e remove essa mensagem da sessão
    return templates.TemplateResponse("cadastro.html", {"request": request, "message": message, "elemento": elemento})

#Rota de Post de Cadastro
@api.post('/cadastro/enviar', response_class=HTMLResponse)
def cadastro(request: Request, nome:str = Form(...), elemento: str = Form(...), email: str = Form(...), senha: str = Form(...)):
    user = read(email)
    if user:
        request.session['message'] = "Este e-mail já está cadastrado. Por favor, use outro e-mail."
        return RedirectResponse(url="/cadastro", status_code=303)

    usuario = [Usuario(nome=nome,elemento=elemento,email=email,senha=senha)]
    create(usuario)
    return RedirectResponse(url=f"/login", status_code=303)

#Rota Pagina de Login
@api.get('/login')
def login(request: Request):
    message = request.session.pop('message', None) #Recupera uma mensagem armazenada na sessão e remove essa mensagem da sessão
    return templates.TemplateResponse("login.html", {"request": request, "message": message})

#Rota de Pot de Login
@api.post("/login/enviar", response_class=HTMLResponse)
def login(request: Request, email: str = Form(...), senha: str = Form(...)):
    user = read(email)
    #Serve para validar se o usuario existe no db e se a senha está certa
    if not user or user.senha != senha:
        request.session['message'] = "Credenciais inválidas. Por favor, tente novamente."
        return RedirectResponse(url=f"/login", status_code=303)
    
    request.session['user_email'] = user.email #Faz com que o email do usurio seja o email da seção
    return RedirectResponse(url="/perfil", status_code=303)

#Rota de Logout
@api.get("/perfil/logout", response_class=HTMLResponse)
def logout(request: Request):
    request.session.pop('user_email', None) #Faz com que o email do usurio seja removida do email da seção
    return RedirectResponse(url="/login", status_code=303)

#Rota Pagina Perfil
@api.get('/perfil')
def perfil(request: Request):
    user_email = request.session.get('user_email') #Pegar o emial que está como email da seção
    user = read(user_email)
    #Validação para ver se o usario está logado, caso não impede ele de acessar a pagina de perfil
    if not user:
        request.session['message'] = "Você precisa estar logado para acessar a página de perfil."
        return RedirectResponse(url="/login", status_code=303) #Redireciona para a pagina de login, com uma informação de que foi redirecionado
    
    message = request.session.pop('message', None) #Recupera uma mensagem armazenada na sessão e remove essa mensagem da sessão
    return templates.TemplateResponse("perfil.html", {"request": request, "nome": user.nome, "elemento": user.elemento, "email": user.email, "senha": user.senha, "message": message})

#Rota Pagina Peril Update
@api.post('/perfil/editar', response_class=HTMLResponse)
def perfil_editar(request: Request,nome:str = Form(...), elemento: str = Form(...), email: str = Form(...), senha: str = Form(...)):
    user = read(email)
    session_email = request.session.get('user_email') #Pegar o email que está como email da seção
    if user and user.email != session_email:
        request.session['message'] = "Este e-mail já está cadastrado. Por favor, use outro e-mail."
        return RedirectResponse(url="/perfil", status_code=303)
    
    update(nome,elemento,email,senha,session_email)
    user = read(email)
    request.session['user_email'] = user.email #Faz com que o email do usurio seja o email da seção
    return RedirectResponse(url=f"/perfil", status_code=303)

#Rota Pagina Perfil Delete
@api.post("/perfil/deletar")
def deletar(request: Request):
    user_email = request.session.get('user_email')
    delete(user_email)
    return RedirectResponse(url=f"/perfil/logout", status_code=303)

#Rodar o servidor
uvicorn.run(app=api,port=7777)