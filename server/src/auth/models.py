import sqlalchemy as sql
import datetime as dt

metadata = sql.MetaData()

user = sql.Table(
    'user',
    metadata,
    sql.Column('id', sql.Integer, primary_key=True, index=True, unique=True),
    sql.Column('email', sql.String(320), nullable=False, unique=True),
    sql.Column('hashed_password', sql.String(1024), nullable=False),
    sql.Column('username', sql.String(500), nullable=False),
    sql.Column('is_active', sql.Boolean, default=True, nullable=False),
    sql.Column('is_superuser', sql.Boolean, default=False, nullable=False),
    sql.Column('is_verified', sql.Boolean, default=False, nullable=False),
    sql.Column('create_date', sql.DateTime, default=dt.datetime.utcnow)
)
