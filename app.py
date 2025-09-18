from flask import Flask, render_template, request
import pandas as pd
import joblib

# Load artifacts
scaler = joblib.load("artifacts/scaler.pkl")
encoder = joblib.load("artifacts/encoder.pkl")
model = joblib.load("artifacts/model.pkl")

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get input
        age = float(request.form["age"])
        gender = request.form["gender"]

        # Encode gender
        gender_encoded = encoder.transform([gender])[0]

        # Prepare dataframe (age + gender)
        input_df = pd.DataFrame([[age, gender_encoded]], columns=["age", "gender"])

        # Apply scaling only on age (dummy salary needed because scaler was fit on [age, salary])
        input_scaled = input_df.copy()
        input_scaled[["age", "salary"]] = scaler.transform(
            input_df[["age"]].assign(salary=0)
        )

        # Predict on scaled features (age, gender)
        predicted_salary_scaled = model.predict(input_scaled[["age", "gender"]])[0]

        # Inverse-transform salary to original scale
        dummy = pd.DataFrame([[0, predicted_salary_scaled]], columns=["age", "salary"])
        salary_original = scaler.inverse_transform(dummy)[0][1]

        return f"<h3>Predicted Salary: {salary_original:.2f}</h3>"

    except Exception as e:
        return f"<h3>Error: {str(e)}</h3>"

if __name__ == "__main__":
    app.run(debug=True)
