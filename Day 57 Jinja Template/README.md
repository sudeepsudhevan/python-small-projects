# SAMPLE

```
@app.route('/guess/<your_name>')
def guess_data(your_name):
    parameter = {
        "name": your_name
    }
    response_gender_api_data = requests.get("https://api.genderize.io", params=parameter).json()
    your_gender = response_gender_api_data["gender"]
    response_age_api_data = requests.get("https://api.agify.io", params=parameter).json()
    your_age = response_age_api_data["age"]

    return render_template("guess_age_gender.html", name=your_name, gender=your_gender, age=your_age)


if __name__ == "__main__":
    app.run(debug=True)
