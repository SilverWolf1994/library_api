from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy import or_
from starlette import status
from typing import List
from app.config.database import get_db
from app.models.book import Book
from app.schemas.book import BaseBook, CreateBook

book = APIRouter()

@book.get("/")
def read_root():
    message = {"Welcome to the Library API"}
    return message


# LIST
@book.get("/books", response_model=List[BaseBook])
def list_books(db:Session = Depends(get_db)):
    listBooks = db.query(Book).all()
    return listBooks

@book.get("/books/author-anio/{search}", response_model=List[BaseBook])
def list_books_by_author_year(search:str, db:Session = Depends(get_db)):
    listBooks = db.query(Book).filter(or_(Book.author.like(search), Book.year.like(search))).all()

    if not listBooks:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No books registered with AUTHOR OR YEAR: {search}")
    
    return listBooks
# /LIST


# CREATE
@book.post("/books", response_model=List[CreateBook])
def create_book(post_book:CreateBook, db:Session = Depends(get_db)):
    createBook = Book(**post_book.model_dump())
    db.add(createBook)
    db.commit()
    db.refresh(createBook)
    return [createBook]
# /CREATE


# READ
@book.get("/books/{id}", response_model=BaseBook)
def read_book(id:str, db:Session = Depends(get_db)):
    readBook = db.query(Book).session.get(Book, id)

    if not readBook:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with ISBN: {id} not found")
    
    return readBook

@book.get("/books/title-author/{search}", response_model=BaseBook)
def read_book_by_title_author(search:str, db:Session = Depends(get_db)):
    readBook = db.query(Book).filter(or_(Book.title.like(search), Book.author.like(search))).first()

    if not readBook:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with TITLE or AUTHOR: {search} not found")
    
    return readBook

# /READ


# UPDATE
@book.put("/books/{id}", response_model=BaseBook)
def update_book(id:str, put_book:BaseBook, db:Session = Depends(get_db)):
    updateBook = db.query(Book).session.get(Book, id)

    if not updateBook:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with ISBN: {id} does not exist")

    updateBook.title = put_book.title
    updateBook.author = put_book.author
    updateBook.year = put_book.year
    updateBook.published = put_book.published
    db.commit()
    return updateBook
# /UPDATE


# DELETE
@book.delete("/books/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(id:str, db:Session = Depends(get_db)):
    deleteBook = db.query(Book).session.get(Book, id)

    if not deleteBook:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with ISBN: {id} not found")
    
    db.delete(deleteBook)
    db.commit()
    return None
# /DELETE
