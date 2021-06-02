from flask import Flask, render_template, request, session

app = Flask(__name__)


@app.route('/main')
@app.route('/home')
@app.route('/')
def homepage():
    return render_template('CV.html')


@app.route('/contacts')
def contacts():
    return render_template('cvfetch.html')


@app.route('/assignment8')
def assignment8():
    curr_user = {'first': "Sagie", 'last': "Rootshtain"}
    return render_template('assignment8.html',
                           curr_user=curr_user,
                           Hobbies=['music', 'games', 'movies'],
                           musicTypes=('rock', 'pop', 'indi'))


@app.route('/assignment9', methods=['Get', 'Post'])
def assignment9():
    curr_user = {'first': '', 'last': ''}
    current_method = request.method
    if 'username' in session:
        username, lastname = session['username'], session['lastname']
    else:
        if current_method == 'GET':
            if 'first_name' in request.args:
                first_name = request.args['first_name']
                last_name = request.args['last_name']
            else:
                first_name, last_name = '', ''
        elif current_method == 'POST':
            if 'first_name' in request.args:
                first_name = request.form['first_name']
                last_name = request.form['last_name']
            else:
                first_name, last_name = '', ''
        else:
            first_name, last_name = '', ''
    if 'LogOut' in request.args:
        username, lastname = '', ''
    return render_template('assignment9.html',
                           curr_user=curr_user,
                           # username=username,
                           # lastname=lastname,
                           first_name=first_name,
                           last_name=last_name,
                           current_method=current_method)


@app.route('/friends')
def friends():
    curr_user = {'first': "Sagie", 'last': "Rootshtain"}
    return render_template('friends.html',
                           curr_user=curr_user,
                           Hobbies=['music', 'games', 'movies'],
                           friends=['roni', 'dor', 'maya'])


if __name__ == '__main__':
    app.run(debug=True)
