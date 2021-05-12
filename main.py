import pickle
from fastapi import FastAPI

app = FastAPI()

db_save_file = './dbdump'

class MocDB:
    def __init__(self):
        self.db = {}
        self.load()

    def get(self, key):
        return self.db[key]

    def set(self, key, value):
        self.db[key] = value

    def load(self):
        with open(db_save_file, 'rb') as f:
            self.db = pickle.load(f)

    def save(self):
        with open(db_save_file, 'wb') as f:
            pickle.dump(self.db, f)



db = MocDB()

@app.get('/{key}')
def get(key):
    return db.get(key)
            
@app.post('/{key}/{value}')
def set(key, value):
    db.set(key, value)


@app.on_event("shutdown")
def close_event():
    db.save()