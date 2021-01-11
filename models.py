import os
import peewee as pw
from playhouse.postgres_ext import PostgresqlExtDatabase

db = PostgresqlExtDatabase(os.environ["DATABASE_NAME"])

class Base(pw.Model):
    def save(self, *args, **kwargs):
        self.errors = []
        self.validate()

        if len(self.errors) == 0:
            return super().save(*args, **kwargs)
        else:
            return 0

    class Meta:
        database = db
        legacy_table_names = False

class Todo(Base):
    task = pw.CharField()
    completion = pw.BooleanField(default=False)

    def validate(self):
        if len(self.task) <= 3:
            self.errors.append("Length of task name is less than 3")