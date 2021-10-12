from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)


class Employee(db.Model):
    employee_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    department_name = db.Column(db.String, db.ForeignKey('department.name'), nullable=False)
    is_head_of = db.Column(db.String, db.ForeignKey('department.name'), nullable=True)


class Department(db.Model):
    name = db.Column(db.String(50), primary_key=True, nullable=False)
    location = db.Column(db.String(120), nullable=False)
    employees = db.relationship('Employee', backref='department')
    head = db.relationship('Employee', backref='head_of_department', uselist=False)


class Project(db.Model):
    project_id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(100), nullable=False),
    members = db.Relationship('Employee', secondary=project_members, backref='projects')


project_members = db.Table('project_members',
    db.Column('employee_id', db.Integer, db.ForeignKey('employee.employee_id'), primary_key=True),
    db.Column('project_id', db.Integer, db.ForeignKey('project.project_id'), primary_key=True)
)

if __name__ == "__main__":
    app.run()
