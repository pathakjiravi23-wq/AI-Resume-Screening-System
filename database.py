import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# ==========================================
# 1. DATABASE CONNECTION SETUP
# ==========================================
# Format: postgresql+psycopg2://<username>:<password>@<host>:<port>/<database_name>
DATABASE_URL = "postgresql+psycopg2://postgres:Ravi123@localhost:5432/practice_db"
# create_engine manages the live connection pool to PostgreSQL
# echo=True prints the generated SQL queries to your terminal (great for learning!)
engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()
