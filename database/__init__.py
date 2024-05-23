from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# SQLACHEMY_DATABASE_URI = 'sqlite:///data.db'
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:muxtar15ovchar@localhost/quiz"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        #any work of except close the project
        db.close()

