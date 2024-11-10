from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

@app.get('/users')
async def read_users() -> dict:
    return {"users": users}

@app.post('/user/{username}/{age}')
async def create_user(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username')],
                      age: int = Path(ge=18, le=120, description='Enter age')) -> dict:
    user_id = str(int(max(users, key=int)) + 1)
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return {"message": f"User {user_id} is registered"}

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: int, username: Annotated[str, Path(min_length=5, max_length=20,
                                                                  description='Enter username')],
                      age: int = Path(ge=18, le=120, description='Enter age')) -> dict:
    users[str(user_id)] = f"Имя: {username}, возраст: {age}"
    return {"message": f"User {user_id} has been updated"}

@app.delete('/user/{user_id}')
async def delete_user(user_id: int) -> dict:
    if str(user_id) in users:
        del users[str(user_id)]
        return {"message": f"User {user_id} has been deleted"}
