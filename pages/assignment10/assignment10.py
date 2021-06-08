from flask import Blueprint, Flask, request, session, url_for
from flask import render_template, jsonify
import mysql.connector

assignment10 = Blueprint('assignment10', __name__,
                         static_folder='static',
                         static_url_path='/pages/assignment10',
                         template_folder='templates')


# routes
@assignment10.route('/assignment10', methods=['Get', 'POST'])
def index():
    if request.method == 'GET':## SELECT
        query = "select * from users"
        query_result = interact_db(query=query, query_type='fetch')
        return render_template('/assignment10.html', users=query_result)
    if request.method == 'POST':## INSERT
        name = request.form['name']
        lastname = request.form['lastname']
        email = request.form['email']
        #password = request.form['password']
        query = "INSERT INTO users(name, lastname, email ) VALUES (%s, %s, %s)" %(name, lastname, email)
        interact_db(query=query, query_type='commit')
        return render_template('assignment10.html',)




# ---------------------------------------------------------------------------------------#
def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         password='root',
                                         database='web_course_schema')
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)

    if query_type == 'commit':
        connection.commit()
        return_value = True

    if query_type == 'fetch':
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value

# -----------------------------------------------------------------------------------#
