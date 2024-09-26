from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import scoped_session, sessionmaker

# Inicializa o SQLAlchemy
db = SQLAlchemy()

# Função para obter a sessão do banco de dados
def get_db():
    # Cria uma sessão escopada para garantir que cada thread tenha sua própria sessão
    Session = scoped_session(sessionmaker(bind=db.engine))
    try:
        yield Session()
    finally:
        Session.remove()