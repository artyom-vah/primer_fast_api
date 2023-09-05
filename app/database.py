from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

DB_HOST = "localhost"
DB_PORT = 5432
DB_USER = "postgres"
DB_PASS = "postgres"
DB_NAME = "postgres"

# Подключаемся к базе данных и создаем переменную async_session_maker которую можно будет использоавть
# для работы с этой бд, сначала генерируем юрл DATABASE_URL - который позволяет алхимии понять где находится база данных
# и передаем ее при создании асинхронного движка engine, движек используется для создания сессий (небольших транзакций)
# создаем класс Base, мы будем наследоваться от него при создании моделей и в переменной Base собираться данные о всех таблицах
DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_async_engine(url=DATABASE_URL)

async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

class Base(DeclarativeBase):
    pass