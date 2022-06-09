from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from transformers import pipeline
# import config
from utilities import download_blob


app = FastAPI()
@app.get("/")
def hello_world():
    return {"Hello": "yi"}

sentiment_model = pipeline("sentiment-analysis")

class PredictionRequest(BaseModel):
  query_string: str
  #query_string_list: List[str]  

@app.post("/new-sentiment")
async def analyze_sentiment(username: str, text: str):    
    user_inputted_sentiment = sentiment_model(text)
    return {f"USER: {username} TEXT: {text} SENTIMENT: {user_inputted_sentiment}"}

@app.get("/fetchnewmodel")
async def fetchnewmodel(): 
    download_blob('mlops_vectorweaviate_capstone', 'ner_models/ner_model.jsonl','ner_model.jsonl')  

