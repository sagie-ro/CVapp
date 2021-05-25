from flask import Flask, render_template

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
                           Hobbies=['music','games','movies'],
                           musicTypes=('rock', 'pop', 'indi'))


@app.route('/friends')
def friends():
    curr_user = {'first': "Sagie", 'last': "Rootshtain"}
    return render_template('friends.html',
                           curr_user=curr_user,
                           Hobbies=['music', 'games', 'movies'],
                           friends=['roni', 'dor', 'maya'])



if __name__ == '__main__':
    app.run(debug=True)
