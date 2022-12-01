from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')



class Email:
    
    def __init__(self,data):
        self.id = data['id']
        self.email= data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        

        
    @classmethod
    def save(cls,data):
        query = "INSERT INTO emails (email) VALUES (%(email)s)"
        return connectToMySQL('emails').query_db(query,data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM emails;"
        results =  connectToMySQL('emails').query_db(query)
        email =[]
        for i in results:
            email.append(cls(i))
        return email
    

    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM emails WHERE id = %(id)s;"
        return connectToMySQL('emails').query_db(query,data)
    
    
    

    @staticmethod
    def validate(email):
        is_valid = True
        query = "SELECT * FROM emails WHERE email = %(email)s;"
        results = connectToMySQL('emails').query_db(query,email)
        if len(results) >= 1:
            flash("El email ya existe")
            is_valid=False
        if not EMAIL_REGEX.match(email['email']):
            flash("Email no válido!")
            is_valid=False
        return is_valid

    