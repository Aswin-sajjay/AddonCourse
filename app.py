from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def bmi_calculator():
    bmi = None
    category = None
    color = None

    if request.method == "POST":
        try:
            height = float(request.form["height"])
            weight = float(request.form["weight"])

            # Convert cm to meters
            height_m = height / 100
            bmi = weight / (height_m ** 2)

            # Determine category
            if bmi < 18.5:
                category = "Underweight"
                color = "#3498db"  # blue
            elif 18.5 <= bmi < 25:
                category = "Normal"
                color = "#2ecc71"  # green
            elif 25 <= bmi < 30:
                category = "Overweight"
                color = "#f1c40f"  # yellow
            else:
                category = "Obese"
                color = "#e74c3c"  # red

            bmi = round(bmi, 2)
        except:
            bmi = "Invalid Input"

    return render_template("index.html", bmi=bmi, category=category, color=color)

if __name__ == "__main__":
    app.run(debug=True)

