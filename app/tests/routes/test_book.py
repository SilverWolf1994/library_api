import pytest
from fastapi import HTTPException
from fastapi.testclient import TestClient
from app.routes.book import book

client = TestClient(book)

# ROOT
def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()[0] == "Welcome to the Library API"

# LIST
def test_list_books():
    response = client.get("/books")
    assert response.status_code == 200, response.text

def test_list_books_by_author_year():
    search = "2024"
    try:
        response = client.get(f"/books/author-anio/{search}")
        if response:
            assert response.status_code == 200, response.text
    except:
        with pytest.raises(HTTPException) as exception:
            response = client.get(f"/books/author-anio/{search}")
        assert exception.value.status_code == 404
        assert exception.value.detail == f"No books registered with AUTHOR OR YEAR: {search}"

# CREATE
def test_create_book():
    response = client.post("/books/", json={
        "isbn": "TEST_12345",
        "title": "TEST_TITLE",
        "author": "TEST_AUTHOR",
        "year": "2024",
        "published": 1,
        "created": "12-12-2024 00:00:00"
    })

    assert response.status_code == 200, response.text
    data = response.json()[0]
    assert data["isbn"] == "TEST_12345"
    assert data["title"] == "TEST_TITLE"
    assert data["author"] == "TEST_AUTHOR"
    assert data["year"] == "2024"
    assert data["published"] == 1
    assert data["created"] == "12-12-2024 00:00:00"
    assert "isbn" in data

# READ
def test_read_book():
    isbn_id = "123456789"
    response = client.get(f"/books/{isbn_id}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["isbn"] == "123456789"
    assert data["title"] == "JINX"
    assert data["author"] == "EKKO"
    assert data["year"] == "2024"
    assert data["published"] == 1
    assert data["created"] == "12-12-2024 00:00:00"

def test_read_book_by_title_author():
    search = "Stephen Pruebas"
    try:
        response = client.get(f"/books/title-author/{search}")
        if response:
            assert response.status_code == 200, response.text
    except:
        with pytest.raises(HTTPException) as exception:
            response = client.get(f"/books/title-author/{search}")
        assert exception.value.status_code == 404
        assert exception.value.detail == f"Book with TITLE or AUTHOR: {search} not found"

# UPDATE
def test_update_book():
    isbn_id = "987654321"
    book = client.get(f"/books/{isbn_id}")
    data = book.json()
    response = client.put(f"/books/{isbn_id}", json={
        "isbn": data["isbn"],
        "title": "UPDATED The Test of Cthulhu",
        "author": "UPDATED Stephen Pruebas",
        "year": "2024",
        "published": data["published"],
        "created": data["created"]
    })

    assert response.status_code == 200, response.text
    data = response.json()
    assert data["isbn"] == isbn_id
    assert data["title"] == "UPDATED The Test of Cthulhu"
    assert data["author"] == "UPDATED Stephen Pruebas"
    assert data["year"] == "2024"

# DELETE
def test_delete_book():
    isbn_id = "TEST_12345"
    book = client.delete(f"/books/{isbn_id}")
    assert book.status_code == 204, book.text

    with pytest.raises(HTTPException) as exception:
        client.get(f"/books/{isbn_id}")
    assert exception.value.status_code == 404
    assert exception.value.detail == f"Book with ISBN: {isbn_id} not found"

    
