# BMI Calculator API

## Description

This project provides a RESTful API to calculate the Body Mass Index (BMI) and determine its classification. The API accepts height and weight data, calculates BMI, and returns the result with classification according to standard categories.

## Setup

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/W0nderful11/bmi_calculator.git
```

### 2. Create a Virtual Environment

Navigate to the project folder and create a virtual environment:

```bash
cd bmi_calculator
python -m venv venv
```

### 3. Activate the Virtual Environment

- For **Windows**:

```bash
venv\Scripts\activate
```

- For **macOS/Linux**:

```bash
source venv/bin/activate
```

### 4. Install Dependencies

Install the required dependencies:

```bash
pip install fastapi uvicorn pydantic
```

## Running the Server

To start the API, run the following command:

```bash
uvicorn main:app --reload
```

The API will be available at: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

## Using the API

### Endpoint `/calculate_bmi`

- **Method**: `POST`
- **Description**: Calculates the Body Mass Index (BMI) and returns its classification.

### Input Data (JSON):

```json
{
  "height": 1.75,  // Height in meters (positive number)
  "weight": 70     // Weight in kilograms (positive number)
}
```

### Response (JSON):

```json
{
  "bmi": 22.86,            // Calculated Body Mass Index
  "classification": "Normal weight"  // BMI classification
}
```

### BMI Classification:

- **Underweight**: BMI < 18.5
- **Normal weight**: BMI 18.5–24.9
- **Overweight**: BMI 25–29.9
- **Obesity**: BMI ≥ 30

### Example Error (JSON):

If the input data is invalid (e.g., negative values):

```json
{
  "error": "Height and weight must be positive numbers."
}
```

## Testing

You can test the API using the built-in Swagger UI interface, available at: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

## Project Structure

- `main.py`: The source code for the API.
- `README.md`: Project documentation.

## Notes

- Make sure you have Python 3.7 or higher installed.
- Use a virtual environment to isolate the project's dependencies.

## Expected Results

Example request:

```http
POST /calculate_bmi
Content-Type: application/json
{
  "height": 1.75,
  "weight": 70
}
```

Example response:

```json
{
  "bmi": 22.86,
  "classification": "Normal weight"
}
```

Error with invalid data:

```json
{
  "error": "Height and weight must be positive numbers."
}
```

## Evaluation

**Evaluation Criteria:**

- **Functionality** (10 points): The API correctly calculates BMI and returns accurate results.
- **Error Handling** (5 points): The API gracefully handles invalid inputs and returns meaningful error messages.
- **Code Quality** (5 points): The code is clean, well-commented, and follows best practices.
- **Documentation** (5 points): The README.md file contains clear setup instructions and usage examples.
