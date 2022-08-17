from db.run_sql import run_sql
from models.books_class import Book

def select_book_by_id(id):
    sql = "SELECT * FROM books WHERE id = %s"
    values = [id]
    return Book(**run_sql(sql, values))
    

def delete_book_by_id():
    pass


def update_book_by_id():
    pass


def insert_book(book):
    sql = "INSERT INTO books (name, author) VALUES (%s %s) RETURNING id"
    values = [books.name, author]
    run_sql(sql, values)

    return book


def show_all_books():
    sql = "SELECT * from authors"
    return run_sql(sql)
