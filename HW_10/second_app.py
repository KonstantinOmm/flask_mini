from help import get_avr_data as calc_avr_data
from flask import Flask

app = Flask(__name__)


@app.route('/avr_data')
def get_avr_data():
    avg_height, avg_weight = calc_avr_data()
    return f"<h1> Средний рост: {avg_height} cm <br> Средний вес: {avg_weight} kg</h1>"


@app.route('/requirements')
def get_requirements():
    with open('requirements', 'r') as file:
        return file.read().replace('\n', '<br>')


if __name__ == "__main__":
    app.run(debug=True, port=5050)
