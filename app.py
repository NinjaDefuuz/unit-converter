from flask import Flask, render_template, request
from converter_core import convert_length

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        raw_value = request.form.get("value", "").strip()
        from_unit = request.form.get("from_unit", "m")
        to_unit = request.form.get("to_unit", "cm")

        if not raw_value:
            error = "Please enter a value first."
        else:
            try:
                value = float(raw_value)
                converted = convert_length(value, from_unit, to_unit)
                result = {
                    "input_value": value,
                    "from_unit": from_unit,
                    "to_unit": to_unit,
                    "output_value": round(converted, 6),
                }
            except ValueError as e:
                error = str(e)

    return render_template("converter.html", result=result, error=error)


if __name__ == "__main__":
    app.run(debug=True)