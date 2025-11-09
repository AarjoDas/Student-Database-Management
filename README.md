# Student Database Management

### Author: AARJO DAS 101349195

### Date: 2025-11-09

### Course: COMP3005

## Prerequisites
- Python v 3.13+
- pip
- PostgreSQL
- Clone repository using:
    git clone gttps://github.com/AarjoDas/Student-Database-Management.git
- Install dependancies in correct directory:

    cd .\Student-Database-Management\
    pip install -r dependancies.txt
  
## Features
- Creates new student in DB
- Reads all students and lists
- Updates student email by ID
- Deletes student information by ID
  
## Running Instructions
1. Create Database with default sample data (included in p1.sql)
2. Configure python file to db:

   host = "localhost",
   
   database = "COMP3005A3Q1", # Update depending on your DB name

   user = "postgres",

   password = "student", # Update depending on your account password

   port = "5432"
5. Run python file
   - py q1.py
