"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaaq867avj5o49ejqdg-a.oregon-postgres.render.com/todo_n6v5
";
        database="todo_n6v5",
        user="todo_n6v5_user",
        password="59FdEzb3eCh6T9IXQXTjmai3I60AKECg")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
