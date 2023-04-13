from typing import AsyncGenerator

from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase
import sqlalchemy as sql
import sys
import os

sys.path.append(os.path.join(sys.path[0].replace('/src', '')))

import config as conf
import datetime as dt

DATABASE_URL = f"mysql+aiomysql://{conf.DB_USER}:{conf.DB_PASS}@{conf.DB_HOST}/{conf.DB_NAME}"


class Base(DeclarativeBase):
    pass


class User(SQLAlchemyBaseUserTable[int], Base):
    id = sql.Column(sql.Integer, primary_key=True, index=True, unique=True)
    email = sql.Column(sql.String(length=320), unique=True, nullable=False)
    hashed_password = sql.Column(sql.String(length=1024), nullable=False)
    username = sql.Column(sql.String(500), nullable=False)
    is_active = sql.Column(sql.Boolean, default=True, nullable=False)
    is_superuser = sql.Column(sql.Boolean, default=False, nullable=False)
    is_verified = sql.Column(sql.Boolean, default=False, nullable=False)
    create_date = sql.Column(sql.DateTime, default=dt.datetime.utcnow)


engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)
