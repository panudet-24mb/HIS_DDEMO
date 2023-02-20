import sys
from app.core.server import get_application 
from loguru import logger
from fastapi_utils.tasks import repeat_every
from pydantic import BaseModel
from fastapi import FastAPI, Header
from typing import Union


version = f"{sys.version_info.major}.{sys.version_info.minor}"


app = get_application() 


class RegisterUser(BaseModel):
    user_code : str
    first_name: str
    last_name: str
    class Config:
        schema_extra = {
            "example": {
                "user_code": "0001",
                "first_name": "Panudet",
                "last_name": "Panumas",
            }
        }

class Recognition(BaseModel):
    face_recognition_type : str
    face_embedding: list
    face_url: str
    class Config:
        schema_extra = {
            "example": {
                "face_recognition_type": "facerecognition_2d_128d",
                "face_embedding": [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.10],
                "face_url": "http://localhost:8000/static/face/0001.jpg",   
            }
        }

class RegisterWebHook(BaseModel):
    webhook_url: str
    apikey : str
    secretkey : str
    class Config:
        schema_extra = {
            "example": {
                "apikey": "",
                "secretkey" : "",
                "webhook_url": "http://localhost:8000/api/v1/facerecognition-service/webhook",
            }
        }


logger.info(f"application start - {version}" )

@app.post("/api/v1/facerecognition-service/register")
def register_user(Regis : RegisterUser ,apikey: Union[str, None] = Header(default=None)):
    if apikey != "8095b8afa7751c8f6bfa84cb6617fde6":
        return {"status": "this user_agent is not allowed"}
    return {"status": "success" , "user_code": Regis.user_code , "first_name": Regis.first_name , "last_name": Regis.last_name}

@app.post("/api/v1/facerecognition-service/{user_account}")
def face_recognition(user_account: str , Recog : Recognition ,apikey: Union[str, None] = Header(default=None)):
    if apikey != "8095b8afa7751c8f6bfa84cb6617fde6":
        return {"status": "this user_agent is not allowed"}
    if user_account != "N00001":
        return {"status": "this account is not allowed"}
    return {"status": "kafka is consummed"}



@app.post("/api/v1/facerecognition-service/register_webhook" , description=" ลงทะเบียน Webhook สำหรับรับข้อมูลผลลัพท์จากการทำ Face Recognition")
          
def register_webhook(Regis : RegisterWebHook):
    if Regis.apikey != "8095b8afa7751c8f6bfa84cb6617fde6" :
        return {"status": "this apikey is not allowed"}
    if Regis.secretkey !=   "cfc0280f5cf25208ff01782cd8a6ac51":
        return {"status" : "this secretkey is not allowed"}
    return {"status": "success" , "webhook_url": Regis.webhook_url}

       