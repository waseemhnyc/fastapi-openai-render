import httpx
import asyncio

async def fetch_stream():
    async with httpx.AsyncClient() as client:
        async with client.stream(
                "POST", "http://127.0.0.1:8000/prompt/stream", 
                json={"message": "Write me 3 paragraph poem about why the sky is blue"}
                ) as response:
            async for line in response.aiter_text():
                print(line, end="")

if __name__ == "__main__":
    asyncio.run(fetch_stream())

