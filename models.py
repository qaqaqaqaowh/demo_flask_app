import os
import peewee as pw
from playhouse.postgres_ext import PostgresqlExtDatabase

db = PostgresqlExtDatabase(os.environ["DATABASE_NAME"])

class Base(pw.Model):
    class Meta:
        database = db
        legacy_table_names = False

class Todo(Base):
    task = pw.CharField()
    completion = pw.BooleanField(default=False)