import sqlite3

con = sqlite3.connect("test.db")

print("Opened database successfully")

"""
con = sqlite3.connect("test.db")
print("We will start!")

c = con.cursor()
sql = '''
    create table company
    (
        id int primary key not null, 
        name text not null,
        age int not null,
        address char(50),
        salary real
    );
'''
c.execute(sql)
con.commit()
con.close()

print("Opened database successfully!")
"""