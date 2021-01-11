import peeweedbevolve
from dotenv import load_dotenv
load_dotenv()
from models import *

db.evolve(ignore_tables={"base"})