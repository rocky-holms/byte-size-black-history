import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

try:
    DB_URL = os.environ["DB_URL"]
except Exception:
    raise Exception('MUST SET "DB_URL" ENVIRONMENT VARIABLE')


engine = create_engine(DB_URL, echo=True)

Base = declarative_base()

Session = sessionmaker(bind=engine)
db_session = Session()
