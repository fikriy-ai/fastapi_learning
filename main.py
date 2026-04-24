from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Optional
from fastapi.templating import Jinja2Templates
import uvicorn

# Create FastAPI instance
app = FastAPI()

# Create the books list
BOOKS = [
    {"id": 1, "title": "First Book", "author": "Author One"},
    {"id": 2, "title": "Second Book", "author": "Author Two"},
    {"id": 3, "title": "Third Book", "author": "Author Three"}
]

# Add a new books to the list
BOOKS.append({"id": 4, "title": "Fourth Book", "author": "Author Four"})
BOOKS.append({"id": 5, "title": "Fifth Book", "author": "Author Five"})
BOOKS.pop(0)  # Remove the first book from the list

# create the read_root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Book API!"}

# create the read_books endpoint
@app.get("/books")
def read_books():
    return BOOKS

# Mount static files
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9000)