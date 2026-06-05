from mariadb import mariadb

def disorders():
    

    try:
        with mariadb.connect(
            user="catman",
            password="",
            host="10.2.2.59",
            port=3306,
            database="mewgenics_wiki") as conn:
            
            mycursor = conn.cursor()
            
            mycursor.execute("SELECT * FROM disorders")
            
            myresult = mycursor.fetchall()
            
            return myresult

    except mariadb.Error as e:
        print(f"Error connecting to MariaDB platform: {e}")
def passives():
    

    try:
        with mariadb.connect(
            user="catman",
            password="",
            host="10.2.2.59",
            port=3306,
            database="mewgenics_wiki") as conn:
            
            mycursor = conn.cursor()
            
            mycursor.execute("SELECT * FROM passives")
            
            myresult = mycursor.fetchall()
            
            return myresult

    except mariadb.Error as e:
        print(f"Error connecting to MariaDB platform: {e}")