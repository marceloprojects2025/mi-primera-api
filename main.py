from fastapi import FastAPI

app = FastAPI(title="API de Marcelo 2026")


@app.get("/")
def read_root():
    return {
        "usuario": "marceloprojects2025",
        "status": "Online",
        "mensaje": "Entorno configurado con éxito",
    }


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "description": "Este es un ejemplo de endpoint"}
