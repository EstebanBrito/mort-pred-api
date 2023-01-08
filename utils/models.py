from pydantic import BaseModel
from typing import List

class PacientModel(BaseModel):
    SEXO: int
    EDAD: int
    EMBARAZO: int
    DIABETES: int
    EPOC: int
    ASMA: int
    INMUSUPR: int
    HIPERTENSION: int
    CARDIOVASCULAR: int
    OBESIDAD: int
    RENAL_CRONICA: int
    TABAQUISMO: int
    OTRA_COM: int
    DIAS_SINTOMAS: int
