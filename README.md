# Deploy FastAPI with Open AI on Render

Use this repo as a template to deploy a Python [FastAPI](https://fastapi.tiangolo.com) service on Render that includes OpenAI endpoints.

## Notes:

- Update `name` in `render.yaml` to the name of your service
- Includes Pytest - Modify tests in test_main.py and run tests with the command `pytest`
- Includes two endpoints: `/prompt` and `/prompt/stream`

## Manual Steps

1. You may use this repository directly or [create your own repository from this template](https://github.com/render-examples/fastapi/generate) if you'd like to customize the code.
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
