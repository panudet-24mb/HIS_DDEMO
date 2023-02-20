
from fastapi import FastAPI 
from starlette.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import logging
from fastapi_utils.session import FastAPISessionMaker
from fastapi_utils.tasks import repeat_every





def get_application() -> FastAPI:
    application = FastAPI(title="NOKSOFT-Facerecognition-Service", debug=True, version="0.0.0.1" )
    create_static_folder_if_not_exist()
    application.mount("/static", StaticFiles(directory="app/static"), name="static")
    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
   
    return application

def create_static_folder_if_not_exist():
    import os
    if not os.path.exists("app/static"):
        os.makedirs("app/static")



