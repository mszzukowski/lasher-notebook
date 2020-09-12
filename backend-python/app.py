#!flask/bin/python
#initial app from https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask
# helping with https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

from flask import Flask, jsonify

app = Flask(__name__)

clients = [
        {
            'id': 0,
            'name': 'Agata',
            'lashes': '8-9-10-11B-11-12-11-10C'
        },

        {
            'id': 1,
            'name': 'Ania',
            'lashes': '8-9-11-12-13-12'
        },

        {
            'id': 2,
            'name': 'Lena',
            'lashes': '8-9-10-11-10-9'
        },

        {
            'id': 3,
            'name': 'Mariola',
            'lashes': '8-9-10-11-12-13-12-11-10-9-8'
        }
]


@app.route('/api/v1.0/clients', methods=['GET'])
def get_clients():
    return jsonify({'clients': clients})

if __name__ == '__main__':
    app.run(debug=True)
