#!flask/bin/python
#initial app from https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask
# helping with https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

from flask import Flask, jsonify

app = Flask(__name__)

clients = [
        {
            'id': 0,
            'name': 'Agata',
            'surname': 'Kot'
        },

        {
            'id': 1,
            'name': 'Ania',
            'surname': 'Pies'
        },

        {
            'id': 2,
            'name': 'Lena',
            'lashes': 'Kurka'
        },

        {
            'id': 3,
            'name': 'Mariola',
            'surname': 'Wąż'
        }
]

visits = [
        {
            'id': 0,
            'client_id': 0,
            'parameters': '8-9-10-11B-11-12-11-10C',
			'date' : '10-10-2020'
        },

        {
            'id': 1,
            'client_id': 1,
            'parameters': '8-9-11-12-13-12',
			'date': '09-09-2020'
        },

        {
            'id': 2,
            'client_id': 2,
            'parameters': '8-9-10-11-10-9',
			'date': '11-08-2020'
        },

        {
            'id': 3,
            'client_id': 3,
            'parameters': '8-9-10-11-12-13-12-11-10-9-8',
			'date': '12-09-2020'
        }
]

@app.route('/api/v1.0/clients', methods=['GET'])
def get_clients():
    return jsonify({'clients': clients})

@app.route('/api/v1.0/visits', methods=['GET'])
def get_clients():
    return jsonify({'visits': visits})

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
