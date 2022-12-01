from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.email import Email

@app.route('/')
def todos():
    return render_template('email.html')


@app.route('/process', methods=['POST'])
def procesar_mails():
    data={
        "email":request.form['email']
    }
    if not Email.validate(data):
        return redirect('/')
    Email.save(data)
    flash('Felicitaciones!!!')
    return redirect('/results')


@app.route('/results')
def show_results():
    emails=Email.get_all()
    return render_template ('results.html', emails=emails) 


@app.route('/destroy/<int:id>')
def destroy_email(id):
    data = {
        "id": id
    }
    Email.destroy(data)
    return redirect('/results')














