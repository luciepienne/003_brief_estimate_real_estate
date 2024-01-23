from fastapi import FastAPI, HTTPException
from typing_extensions import Annotated, Doc
import pickle
import uvicorn
import numpy as np

app = FastAPI(title='ESTIMATION')


#model = pickle.load(open(r'/mnt/c/Users/Utilisateur/Desktop/project_briefs/003_real_estate_api_estimate/RFR_2X_best_model_V2.pkl', 'rb'))
#model = pickle.load(open('RFR_2X_best_model_V2.pkl', 'rb'))
#model = pickle.load(r'C:\Users\Utilisateur\Desktop\project_briefs\003_real_estate_api_estimate\RFR_2X_best_model.pkl')
model = pickle.load(open('RFR_2X_best_model_V2.pkl', 'rb'))

@app.post("/price_predictor_v1/", description="With a given longitude and latitude, returns price per square meter best estimate")
async def price_predictor(longitude: float, latitude: float):
    input_data = np.array([[longitude, latitude]])
    return model.predict(input_data)[0]

if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=5000)


# @app.post("/sq2_price_predictor_v2/", description="Retourne une prédiction de prix au m²")
# async def sq2_price_predictor(longitude: float, latitude: float, taux: float):
#     input_data = np.array([[longitude, latitude, taux]])

#     return withInterestRates_model.predict(input_data)[0]

# # loading the model and make sure it is loaded fine
# def load_model(file_path):
#     try:
#         with open(file_path, 'rb') as file:
#             model = pickle.load(file)
#             return model
#     except FileNotFoundError:
#         print('fichier modèle introuvable')
#         return None


# # Fonction pour effectuer la prédiction
# def predict(model, longitude, latitude):
#     if model is None:
#         raise HTTPException(status_code=503, detail="Modèle non chargé")
#     input_data = [[longitude, latitude]]
#     return model.predict(input_data)[0]



