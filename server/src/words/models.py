import sqlalchemy as sql

from src.auth.models import user
from src.dictionaries.models import dictionary

metadata = sql.MetaData()

word = sql.Table(
    'word',
    metadata,
    sql.Column('id', sql.Integer, primary_key=True, index=True),
    sql.Column('user_id', sql.Integer, sql.ForeignKey(user.c.id)),
    sql.Column('dict_id', sql.Integer, sql.ForeignKey(dictionary.c.id)),
    sql.Column('word', sql.String(250), nullable=False),
    sql.Column('translate', sql.JSON, nullable=False),
    sql.Column('selected_translate', sql.String(250)),
    sql.Column('meaning', sql.Text),
    sql.Column('custom_translate', sql.String(500)),
    sql.Column('use_custom', sql.Integer)
)
