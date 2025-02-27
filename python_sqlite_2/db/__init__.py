from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_URL = "sqlite:///job.db"

engine = create_engine(DB_URL)
Session = sessionmaker(bind=engine)
