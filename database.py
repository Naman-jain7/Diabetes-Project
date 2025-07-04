import mysql.connector
from patient import Patient

class DataBaseHandler:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(host=host, user=user, password=password, database=database)
        self.cursor = self.conn.cursor()
        
    def create_table(self):
        self.cursor.execute('''
        create table if not exists patients(
            id int AUTO_INCREMENT primary key,
            name varchar(100) not null,
            age int,
            pregnancies int,
            glucose float,
            bp float,
            skinThickness float,
            insulin float,
            bmi float,
            dpf float,
            prediction varchar(50)
        )
        ''')
        
    def insert_patient(self, patient:Patient, prediction):
        query = '''insert into patients(name, age, pregnancies, glucose, bp, skinThickness, insulin, bmi, dpf, prediction) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
        values = patient.to_tuple() + (prediction,)
        self.cursor.execute(query, values)
        self.conn.commit()