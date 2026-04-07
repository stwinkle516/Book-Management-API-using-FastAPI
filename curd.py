from fastapi import FastAPI, status
from pydantic import BaseModel
from datetime import date
from fastapi.exceptions import HTTPException

app = FastAPI()

books = [
      {
    "id": 1,
    "title": "The Alchemist",
    "author": "Paulo Coelho",
    "publish_date": "1988-04-15"
  },
  {
    "id": 2,
    "title": "Atomic Habits",
    "author": "James Clear",
    "publish_date": "2018-10-16"
  },
  {
    "id": 3,
    "title": "Rich Dad Poor Dad",
    "author": "Robert T. Kiyosaki",
    "publish_date": "1997-04-01"
  },
  {
    "id": 4,
    "title": "Ikigai",
    "author": "Héctor García & Francesc Miralles",
    "publish_date": "2016-01-01"
  }
]

@app.get("/books")
def get_books():
    return books

@app.get("/book/{book_id}")
def get_book(book_id:int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not Found")


class Book(BaseModel):
  id:int
  title:str
  author:str
  publish_date:date

@app.post("/book")
def create_books(book:Book):
    new_books = book.model_dump()
    books.append(new_books)


class BookUpdate(BaseModel):
  title:str
  author:str
  publish_date:date

@app.put("/book/{book_id}")
def update_book(book_id:int, book_update:BookUpdate):
    for book in books:
        if book["id"]== book_id:
            # book["author"] == author
          book["title"]= book_update.title
          book["author"]=book_update.author
          book["publish_date"]=book_update.publish_date
          return book

    raise HTTPException (status_code=status.HTTP_404_NOT_FOUND, detail="Book not Found")

# class BookDelete(BaseModel):
#   id:int
#   title:str
#   author:str
#   publish_date:date

@app.delete("/book/{book_id}")
def delete_book(book_id:int):
  for book in books:
      if book["id"] == book_id:
        books.remove(book)
        return{"message":"Book Removed"}
  
  raise HTTPException (status_code=status.HTTP_404_NOT_FOUND, detail="Book not Found")


        
        
        