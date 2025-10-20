from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "Пошел нахуй"}

@app.post("/add/{a}/{b}")
def add_numbers(a: int, b: int):
    return {"result": a + b}