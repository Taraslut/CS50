from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    # name = 'Taras'
    name = request.args.get('name')
    # res
    # request.cookies
    if request.method == 'POST':
        return 'POST method is used!'
    return render_template('form-0.html', name=name)


@app.route('/project/', methods=['GET', 'POST'])
def project():
    if request.method == 'GET':
        return 'GET method is used!'
    if request.method == 'POST':
        return 'POST method is used!'

        # return 'The project page!'


@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'GET':
        return hello_world()
    if valid_login(request.form['username'], request.form['password']):
        return 'Method POST is got.'


if __name__ == '__main__':
    app.debug = True
    app.run()


with app.test_request_context('/hello', method='POST'):
    #u теперь, и до конца блока with, вы можете что-либо делать
    #u с контекстом, например, вызывать простые assert-ы:
    assert request.path == '/hello'
    assert request.method == 'POST'
