#Importações necessárias
from sqlalchemy import create_engine
from sqlalchemy.orm import (declarative_base, 
                            Mapped, 
                            mapped_column,
                            sessionmaker)
# Modelos de dados
Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False)
    senha: Mapped[str] = mapped_column(nullable=False)
    elemento: Mapped[str] = mapped_column(nullable=False)

# Conexão com Base de dados
db = create_engine("sqlite:///base.db", echo=True)

# Criar sessão para realizar operações de CRUD
Session = sessionmaker(bind=db)

# Criar tabelas da base
Base.metadata.create_all(db)