from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
#https://pydantic-docs.helpmanual.io/usage/models/

app = FastAPI()
@app.get("/")
def hello_world():
    return {"Hello": "World"}


"""
Ml part 
"""
import praw
from transformers import pipeline
from transformers import pipeline
import random


reddit = praw.Reddit(
    client_id=config.REDDIT_API_CLIENT_ID,
    client_secret=config.REDDIT_API_CLIENT_SECRET,
    user_agent=config.REDDIT_API_USER_AGENT,
)

subreddit = reddit.subreddit('TSLA') 

from praw.models import MoreComments

top_comments = []

for submission in subreddit.top(limit=10):
    for top_level_comment in submission.comments:
        if isinstance(top_level_comment, MoreComments):
                    continue
        top_comments.append(top_level_comment.body)

sentiment_model = pipeline("sentiment-analysis")
def get_random_comment(conversations):
    comment = random.choice(conversations)
    return comment



class PredictionRequest(BaseModel):
  query_string: str

@app.post("/sentiment-sum")
async def calculate_sentiment_sum(predictionrequest: PredictionRequest):
    return predictionrequest




