#~/user-service/app/api/db.py

import os
from sqlalchemy import (Column, Integer, MetaData, String, Table,
                        create_engine, Boolean, and_)

from databases import Database

DATABASE_URL = os.getenv('DATABASE_URI')

engine = create_engine(DATABASE_URL)
metadata = MetaData()

users = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('username', String(15)),
    Column('hashed_password', String(250)),
    Column('email', String(50)),
    Column('name', String(250)),
    Column('disabled', Boolean)
)

database = Database(DATABASE_URL)