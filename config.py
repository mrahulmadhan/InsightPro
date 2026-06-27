import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'super-secret-key-for-insightpro'
    DATABASE_PATH = os.path.join(BASE_DIR, 'database', 'insightpro.db')
    SCHEMA_PATH = os.path.join(BASE_DIR, 'database', 'schema.sql')
    DEBUG = True
