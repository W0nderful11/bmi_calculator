from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


# Модель для входных данных
class BMIInput(BaseModel):
    height: float
    weight: float


# API endpoint
@app.post("/calculate_bmi")
def calculate_bmi(data: BMIInput):
    if data.height <= 0 or data.weight <= 0:
        raise HTTPException(status_code=400, detail="Height and weight must be positive numbers.")

    # Формула расчёта BMI
    bmi = data.weight / (data.height ** 2)
    classification = classify_bmi(bmi)

    return {
        "bmi": round(bmi, 2),
        "classification": classification
    }


# Функция для классификации BMI
def classify_bmi(bmi: float) -> str:
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"
