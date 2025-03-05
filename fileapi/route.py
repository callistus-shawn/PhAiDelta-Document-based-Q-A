from fastapi import APIRouter
from .rag.function import upload
from .rag.function import question

def rout():
    router=APIRouter()
    router.add_api_route("/question",question,methods=["POST"])
    router.add_api_route("/upload",upload,methods=["POST"])
    return router