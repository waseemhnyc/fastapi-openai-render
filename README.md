# FastAPI with Open AI deployed on Render

Use this repo as a template to deploy a Python [FastAPI](https://fastapi.tiangolo.com) service on Render that includes OpenAI endpoints.

## Why use this template

- Includes two endpoints: `/prompt` and `/prompt/stream`
- `/prompt/stream` streams back responses from OpenAI to FastAPI to your client
- Deploy with one click
- Includes Pytest - Modify tests in test_main.py and run tests with the command `pytest`

## Run Project Locally

1. Clone or Fork repository
2. Create your `.env` file with `cp .env.example .env` and update your `OPENAI_API_KEY`
3. Create virtualenv 
4. Source virtualenv
5. Install requirements
6. Run local server `uvicorn main:app --host 0.0.0.0`


## Manual Steps

1. You may use this repository directly or [create your own repository from this template](https://github.com/waseemhnyc/fastapi-openai-render/generate) if you'd like to customize the code.
2. Create a new Web Service on Render.
3. Specify the URL to your new repository or this repository.
4. Render will automatically detect that you are deploying a Python service and use `pip` to download the dependencies.
5. Specify the following as the Start Command.

    ```shell
    uvicorn main:app --host 0.0.0.0 --port $PORT
    ```

6. Click Create Web Service.

Or simply click:

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/waseemhnyc/fastapi-openai-render.git)
