from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/predict/")
async def predict(question: str):
    # execute your NEL algoritm here
    output = {'named_entitiy': 'http://dbpedia.org/resource/Donald_Trump'} # static solution
    print("NEL:", output)
    return JSONResponse(content=output)