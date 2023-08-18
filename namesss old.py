import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Akis.123",
  database="Application"
)

mycursor = mydb.cursor()

sql = "INSERT INTO resumemain (Fullname, DOB, Nationality, School, Dept, SAT, SATSubject, Gender, Overall, ClassRank) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
val = [
    ('Harshitha Devi', '2002/09/03', 'Indian', 'AKIS', 'Computer Science', 1250, 2340, 'Female', 95, 2),
    ('Aayushi Patel', '2003/01/12', 'Indian', 'AKIS', 'Computer Science', 1500, 2390, 'Female', 94, 1),
    ('Nandini Parekh', '2002/04/30', 'Indian', 'AKIS', 'Computer Science', 1150, 2240, 'Female', 92, 5),
    ('Sonu Nigam', '2001/04/28','Canadian', 'AKIS', 'Computer Science', 1220, 2300, 'Male', 93, 3 ),
    ('Shahrukh Khan', '1990/05/01', 'Canadian', 'AKIS', 'Computer Science', 1230, 2240, 'Male', 91, 4),
    ('Salman Khan ', '1991/06/20', 'Canadian', 'DMIS', 'Computer Science', 1350, 1840, 'Male', 96, 6),
    ('Arijit Singh ','1998/11/30', 'Canadian', 'DMIS', 'Computer Science', 1450, 1780, 'Male', 97, 10),
    ('Shreya Ghoshal ', '2001/01/16', 'Canadian', 'DMIS', 'Computer Science', 1150, 2220, 'Female', 91, 12),
    ('Varun Dhawan ', '2001/03/19', 'British', 'DMIS', 'Computer Science', 1260, 2240, 'Male', 90, 7),
    ('Alia Bhatt ', '2003/10/14', 'British', 'DMIS', 'Computer Science', 1280, 2140, 'Female', 89, 9),
    ('Priyanka Chopra Jonas ', '2003/05/13', 'British', 'DPS', 'Computer Science', 1200, 2040, 'Female', 88, 8),
    ('Anushka Sharma', '2001/08/28', 'British', 'DPS', 'Computer Science', 1300, 2350, 'Female', 87, 11),
    ('Virat Kohli', '2001/06/30', 'British', 'SIS', 'Computer Science', 1400, 2360, 'Male', 86, 13),
    ('Siddharth Malhotra', '1999/02/11', 'American', 'DPS', 'Computer Science', 1050, 2370, 'Male', 85, 15),
    ('Deepika Padukone', '1991/04/12', 'American', 'SIS', 'Computer Science', 1290, 2240, 'Female', 84, 14),
    ('Ranveer Singh', '1990/03/21', 'American', 'MES', 'Computer Science', 1390, 2250, 'Male', 83, 17),
    ('Thanda Aadmi', '2003/07/25', 'American', 'MES', 'Computer Science', 1550, 2400, 'Male', 82, 18),
    ('Javed Jaffrey', '2004/05/14', 'American', 'MES', 'Computer Science', 1600, 2350, 'Male', 98, 16),
    ('Vidya Vox', '2002/09/17', 'American', 'BPS', 'Computer Science', 1350, 2320, 'Female', 80, 19),
    ('Dev Patel', '2001/06/03', 'Qatari', 'BPS', 'Computer Science', 1350, 2140, 'Male', 79, 20),
    ('Karan Johar', '2001/01/24', 'Qatari', 'SIS', 'Computer Science', 1100, 2100, 'Male', 78, 21),
    ('Ranbir Kapoor', '2000/11/27', 'Qatari', 'EMS', 'Computer Science', 1150, 2290, 'Male', 77, 22),
    ('Kareena Kapoor', '2002/12/16', 'Indian', 'EMS', 'Computer Science', 1370, 2380, 'Male', 76, 25),
    ('Hrithik Roshan', '2003/08/18', 'Indian', 'BPS', 'Computer Science', 1050, 1980, 'Male', 75, 24),
    ('Katrina Kaif', '2001/12/20', 'Indian', 'AKIS', 'Computer Science', 1150, 1870, 'Female', 74, 23),
    ('Preeti Zinta', '2000/06/12', 'Indian', 'AKIS', 'Computer Science', 1420, 2130, 'Female', 73, 26)
]
mycursor.executemany(sql, val)
mycursor.execute("Select * from resumemain")

myresult=mycursor.fetchall()

mydb.commit()

print(mycursor.rowcount, "record inserted.")



