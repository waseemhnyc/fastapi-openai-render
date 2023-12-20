# FastAPI with Open AI deployed on Render

Use this repo as a template to deploy a Python [FastAPI](https://fastapi.tiangolo.com) service on Render that includes OpenAI endpoints.


## Why use this template

📌 Includes two endpoints: `/prompt` and `/prompt/stream`

📡 `/prompt/stream` streams responses from OpenAI → FastAPI → Client

🚀 Deploy with one click

✅ Includes Pytest - Modify tests in `test_main.py` and run tests with the command `pytest`

## Run Project Locally

Clone or fork repository

```bash
git clone https://github.com/waseemhnyc/fastapi-openai-render.git
```

Create a virutalenv and source the environment

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the necessary libraries

```bash
pip install -r requirements.txt
```

Create a .env file and input your OpenAI API Key in the file

```bash
cp .env.example .env
```

Run local server
```bash
uvicorn main:app --host 0.0.0.0
```

## Manual Steps To Deploy

1. You may use this repository directly or [create your own repository from this template](https://github.com/waseemhnyc/fastapi-openai-render/generate) if you'd like to customize the code.
2. Create a new Web Service on Render.
3. Specify the URL to your new repository or this repository.
4. Render will automatically detect that you are deploying a Python service and use `pip` to download the dependencies.
5. Specify the following as the Start Command.

    ```shell
    uvicorn main:app --host 0.0.0.0 --port $PORT
    ```
6. Add `OPENAI_API_KEY` as an environment variable.
6. Click Create Web Service.

## Or `Click to Deploy`:

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/waseemhnyc/fastapi-openai-render.git)

## Frequently Asked Questions (FAQ)

**Question:** How can I customize the `Click to Deploy` button to point to my forked repository?

```
By updating the URL to your forked repository in this README file.
```

**Question:** How can I change the name of my web service?

```
You can change the name of your web service by modifying the `name` key in the `render.yaml` file.
```

```bash
  - type: web
    name: your-custom-service-name
    runtime: python
```
