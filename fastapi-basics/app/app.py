from fastapi import FastAPI, HTTPException
from app.schemas import PostCreate
app = FastAPI()


@app.get("/hello-world")
def hello_world():
    return {"message": "Hello World!"}  # JSON


text_posts = {
    1: {"title": "New post", "content": "cool test post"},
    2: {
        "title": "Learning FastAPI",
        "content": "FastAPI is a modern Python web framework that makes building APIs easy and fast.",
    },
    3: {
        "title": "Python tips",
        "content": "Use list comprehensions for cleaner and more readable code.",
    },
    4: {
        "title": "REST API design",
        "content": "Always use proper HTTP status codes and meaningful resource naming.",
    },
    5: {
        "title": "Async programming",
        "content": "Async endpoints in FastAPI can handle more concurrent requests efficiently.",
    },
    6: {
        "title": "Database integration",
        "content": "SQLAlchemy and Tortoise ORM are popular choices for FastAPI projects.",
    },
    7: {
        "title": "Authentication basics",
        "content": "JWT tokens are commonly used for stateless authentication in APIs.",
    },
    8: {
        "title": "Deployment guide",
        "content": "Use uvicorn behind a reverse proxy like nginx for production deployments.",
    },
    9: {
        "title": "Testing APIs",
        "content": "The TestClient from FastAPI makes it simple to write unit tests for your endpoints.",
    },
    10: {
        "title": "Error handling",
        "content": "Custom exception handlers help provide consistent error responses across your API.",
    },
}


@app.get("/posts")
def get_all_posts(limit:int = None):
    if limit:
        return list(text_posts.values())[:limit]
    return text_posts


@app.get("/posts/{id}")
def get_post(id: int):
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not found")
    return text_posts.get(id)

@app.post("/posts")
def create_post(post:PostCreate):
    new_post={ "title":post.title,"content":post.content}
    text_posts[max(text_posts.keys())+1]=new_post
    return new_post

