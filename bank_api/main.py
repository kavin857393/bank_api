from fastapi import FastAPI
from routers.accounts import router


app = FastAPI(title="Banking API")


# Include the accounts router
app.include_router(router)