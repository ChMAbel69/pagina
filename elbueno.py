from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import numpy as np
import io
import os
from config import config 
from config import columnas_eliminar
from builder import dfbuilder
from builder import dfops
app = FastAPI()
import uvicorn

if __name__ == "__main__":
    uvicorn.run("elbueno:app", host="0.0.0.0", port=8000)

# Esto es para que tu futura página web pueda hablar con Python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/consultar")
async def realizar_consulta(file: UploadFile = File(...),
                            reporte: str = Form(...),
                            semana: int = Form(None),
                            anio: int = Form(None)):
    # 1. Recibir el archivo
    bytes_data = await file.read()
    
    if len(bytes_data)>0:
        df = pd.read_excel(io.BytesIO(bytes_data))

    else:
        print("el archivo esta vacio")
    
    
    if reporte not in config:
        return {"error": "Reporte no existe"}

    reqs = config[reporte]["requires"]

    if reqs.get("semana") and semana is None:
        return {"error": "Semana requerida"}

    if reqs.get("anio") and anio is None:
        return {"error": "Año requerido"}
    

    builder = dfbuilder(df, config, columnas_eliminar)
    resultados = builder.build(reporte, semana=semana, anio=anio)
    
    def limpiar_para_json(df):
        df = df.copy()

        df = df.replace([np.nan, np.inf, -np.inf], None)

        for col in df.select_dtypes(include=['datetime64[ns]']).columns:
            df[col] = df[col].astype(str)

        return df

    data_limpia = {}

    for nombre, contenido in resultados.items():
        #print("ITERANDO:", nombre)

        df_limpio = limpiar_para_json(contenido["df"]).to_dict(orient="records")

        reportes_limpios = {}

        for rep_nombre, rep_df in contenido["reportes"].items():
            if isinstance(rep_df, pd.DataFrame):
                reportes_limpios[rep_nombre] = limpiar_para_json(rep_df).to_dict(orient="records")
            else:
                reportes_limpios[rep_nombre] = rep_df

        data_limpia[nombre] = {
        "df": df_limpio,
        "reportes": reportes_limpios }

    #print("FINAL:", data_limpia.keys())
    #print("RESULTADOS:", resultados.keys())
    #print("DATA LIMPIA:", data_limpia.keys())
    return {
        "status": "success",
        "data": data_limpia
}
