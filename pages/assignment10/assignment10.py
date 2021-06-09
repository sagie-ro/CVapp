from flask import Blueprint, Flask, request, session, url_for
from flask import render_template, jsonify
import mysql.connector

assignment10 = Blueprint('assignment10', __name__,
                         static_folder='static',
                         static_url_path='/pages/assignment10',
                         template_folder='templates')


# routes
@assignment10.route('/assignment10', methods=['GET', 'POST', 'DELETE', 'PUT'])
def index():
    current_method = request.method
    ## SELECT
    if current_method == 'GET':
        query = "select * from users"
        query_result = interact_db(query=query, query_type='fetch')
        return render_template('/assignment10.html', users=query_result)
    ## INSERT
    if current_method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        # password = request.form['password']
        query = "INSERT INTO users(email, first_name, last_name ) VALUES ('%s', '%s, '%s'')" % (email, first_name, last_name)
        interact_db(query=query, query_type='commit')
        return render_template('assignment10.html')
    ##UPDATE
    if current_method == 'PUT':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        # password = request.form['password']
        query = "UPDATE users SET firstName = '%s', lastName = '%s' WHERE email = '%s'" % (first_name, last_name, email)
        interact_db(query=query, query_type='commit')
        return render_template('assignment10.html')
    ##DELETE
    if current_method == 'DELETE':
        email = request.form['email']
        query = "DELETE FROM users WHERE email = '%s'" % email
        query_result = interact_db(query=query, query_type='commit')
        return render_template('/assignment10.html', users=query_result)


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

    # if query_type == 'delete':
    #     query_result = cursor.execute(query)
    #     return_value = query_result

    connection.close()
    cursor.close()
    return return_value

# -----------------------------------------------------------------------------------#
