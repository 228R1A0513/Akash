from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Students(Base):
    _tablename_ = 'students'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    Rollno = Column(String)
    Section = Column(String)

engine = create_engine("sqlite:///mydb.db")

Base.metadata.create_all(engine)

Session = sessionmaker(bind=True)
s = Session()
s.commit()