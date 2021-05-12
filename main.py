from fastapi import FastAPI

app = FastAPI()

class MocDB:
    def __init__(self):
        self.db = {}

    def get(self, key):
        return self.db[key]

    def set(self, key, value):
        self.db[key] = value

db = MocDB()

@app.get('/{key}')
def get(key):
    return db.get(key)
            
@app.post('/{key}/{value}')
def set(key, value):
    db.set(key, value)
