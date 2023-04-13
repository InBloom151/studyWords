import sqlalchemy as sql
import datetime as dt

from src.auth.models import user

metadata = sql.MetaData()

dictionary = sql.Table(
    'dictionary',
    metadata,
    sql.Column('id', sql.Integer, primary_key=True, index=True),
    sql.Column('user_id', sql.Integer, sql.ForeignKey(user.c.id)),
    sql.Column('name', sql.String(250), nullable=False),
    sql.Column('create_date', sql.DateTime, default=dt.datetime.utcnow)
)
