from fastapi import FastAPI
import pickle
import pandas as pd
from utils.models import PacientModel

model =  pickle.load(open('./models/model.pkl', 'rb'))
preproc_pipeline = pickle.load(open('./models/preproc_pipeline.pkl', 'rb'))

app = FastAPI()

@app.get('/')
def root():
    return { 'message': 'OK' }

# TODO: Make prediction accept multiple instances
@app.post('/predict')
def predict(pacient: PacientModel):
    pacient_df = pd.DataFrame(pacient.dict(), index=[0])
    X = preproc_pipeline.transform(pacient_df)
    y_prob = model.predict_proba(X)
    return { 'prediction': y_prob[0][1] } # TODO: Format response in a better way

