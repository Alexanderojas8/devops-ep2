from fastapi import FastAPI

app = FastAPI()


@app.get("/saludo")
def saludo():
    return {"mensaje": "Hola desde Python"}


@app.get("/restar")
def restar(a: int, b: int):
    return {"resultado": a - b}