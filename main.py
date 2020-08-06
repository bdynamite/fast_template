from fastapi import FastAPI
from sql_app import database


app = FastAPI()


@app.get("/check_db_connection")
async def root():
    try:
        res = database.db.connect()
    except Exception as e:
        res = str(e)
    else:
        database.db.close()
    return {"connect_params": database.db.connect_params, "res": res}
