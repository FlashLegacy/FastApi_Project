DB_HOST = "localhost"
DB_PORT = 5432
DB_USER = "postgres"
DB_NAME = "postgres" 
DB_PASS = 11545663

DB_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"