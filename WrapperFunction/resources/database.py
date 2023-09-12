from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_PATH = 'sqlite:///./datalytics.db'

engine = create_engine(
    SQLALCHEMY_DATABASE_PATH,
    connect_args={
        'check_same_thread': False
    }
)

localsession = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

def get_db():
    db = localsession()
    try:
        yield db
    finally:
        db.close()

Base = declarative_base()
