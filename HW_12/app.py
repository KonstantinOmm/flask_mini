from flask import Flask
from webargs.flaskparser import use_kwargs
from webargs import fields
from help import get_requests

app = Flask(__name__)


@app.route('/rates')
@use_kwargs(
    {
        'currency': fields.Str(required=False, missing='USD')
    },
    location='query'
)
def get_avr_data(currency):
    result = get_requests(currency)
    return f'<h1>Курс биткоина к {result[0]} = {result[1]}</h1>'


if __name__ == "__main__":
    app.run(debug=True, port=5050)
