from fastapi import FastAPI
from dotenv import load_dotenv

from route import rout
load_dotenv()

app = FastAPI()
rout=rout()
app.include_router(rout)


