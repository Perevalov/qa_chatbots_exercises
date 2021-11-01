from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/predict/")
async def predict(question: str):
    # execute your Relation Prediction algoritm here
    output = {'predicted_relation': 'http://dbpedia.org/ontology/birthPlace'} # static solution
    print("RelationPrediction:", output)
    return JSONResponse(content=output)