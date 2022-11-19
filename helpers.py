import openai
import os


openai.api_key = os.environ['OPENAI_API_KEY']


def query(payload):
    completion = openai.Completion.create(engine="text-davinci-002", max_tokens=2048, prompt="summarize the following article:" + payload )
    return completion 