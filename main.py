from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel

import openai


class Settings(BaseSettings):
    openai_api_key: str
    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = openai.Client(api_key=settings.openai_api_key)
aclient = openai.AsyncClient(api_key=settings.openai_api_key)
system_prompt = """
The following is a conversation with an AI assistant. 
The assistant is helpful, creative, clever, and very friendly.\n\n
Human: Hello, who are you?\n
AI: I am an AI created by OpenAI. How can I help you today?
\nHuman: 
"""


class Prompt(BaseModel):
    message: str


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/prompt")
async def prompt_response(prompt: Prompt):
    openai_response = client.chat.completions.create(
        model="gpt-4-1106-preview",
        stream=True,
        messages=[
            {
                "role": "system", 
                "content": system_prompt
            },
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt.message},
                ],
            }
        ],
    )
    return {"response": openai_response.choices[0].text.strip()}


@app.post("/prompt/stream")
async def prompt_response_stream(prompt: Prompt):
    openai_response = await aclient.chat.completions.create(
        model="gpt-4-1106-preview",
        stream=True,
        messages=[
            {
                "role": "system", 
                "content": system_prompt
            },
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt.message},
                ],
            }
        ],
    )
    
    async def generate():
        async for token in openai_response:
            content = token.choices[0].delta.content
            if content is not None:
                yield content

    return StreamingResponse(generate(), media_type="text/event-stream")
