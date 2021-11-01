from fastapi import FastAPI
from fastapi.responses import JSONResponse
import requests
import os 

app = FastAPI()

@app.post("/answer/")
async def predict(question: str):
    # it is an entrypoint of our system
    nel = requests.post('http://{0}:80/predict?question={1}'.format(os.environ['NEL_NAME'], question)).json()
    rel_pred = requests.post('http://{0}:80/predict?question={1}'.format(os.environ['REL_PRED_NAME'], question)).json()
    query_exec = requests.post(
        'http://{0}:80/predict?named_entity={1}&predicted_relation={2}'.format(os.environ['QUERY_EXEC_NAME'], nel['named_entitiy'], rel_pred['predicted_relation'])
    ).json()
    output = [nel, rel_pred, query_exec] # static solution
    print("API:\n", output)
    return JSONResponse(content=output)