from flask import Blueprint, Flask, request, session, url_for, redirect
from flask import render_template, jsonify
import mysql.connector

assignment10 = Blueprint('assignment10', __name__,
                         static_folder='static',
                         static_url_path='/pages/assignment10',
                         template_folder='templates')


# routes
@assignment10.route('/assignment10', methods=['GET'])
def index():
    current_method = request.method
    query_result = False
    query1 = "select * from users"
    query_result = interact_db(query=query1, query_type='fetch')
    return render_template('/assignment10.html', users=query_result, req_method=request.method)

# UPDATE
@assignment10.route('/update', methods=['POST'])
def update():
    query_result = False
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    # password = request.form['password']
    query3 = "UPDATE users SET firstName = '%s', lastName = '%s' WHERE email = '%s'" % (first_name, last_name, email)
    query_result = interact_db(query=query3, query_type='fetch')
    return redirect('/assignment10')


# DELETE
@assignment10.route('/delete', methods=['POST'])
def delete():
    query_result = False
    if request.method == 'POST':
        email = request.form['email']
        query4 = "DELETE FROM users WHERE email = '%s'" % (email)
        query_result = interact_db(query=query4, query_type='commit')
    return redirect('/assignment10')

# INSERT
@assignment10.route('/insert', methods=['POST'])
def insert():
    query_result = False
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        # password = request.form['password']
        query2 = f"INSERT INTO users(email, first_name, last_name) VALUES('%s', '%s', '%s')" % (
            email, first_name, last_name)
        # data = (email, first_name, last_name)
        query_result = interact_db(query=query2, query_type='commit')
    return redirect('/assignment10')


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
