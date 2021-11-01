from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/predict/")
async def predict(named_entity: str, predicted_relation: str):
    # execute your SPARQL query here
    output = {'query_result': named_entity + '+' + predicted_relation} # static solution
    print("QueryExecution:", output)
    return JSONResponse(content=output)