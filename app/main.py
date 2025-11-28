# import


# local import
from app import app_config


# instance app
# ---------------------------------------------------
app = app_config()


# root endpoint
# ---------------------------------------------------
@app.get("/")
async def get_app_root_endpoint(

) -> object:

    # return
    return {"FastAPI": "Success Init"}
