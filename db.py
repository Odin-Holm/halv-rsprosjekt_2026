from mariadb import mariadb

def disorders():
    

    try:
        with mariadb.connect(
            user="mewgenics_man",
            password="4321",
            host="10.2.0.140",
            port=3306,
            database="mewgenics_wiki") as conn:
            
            mycursor = conn.cursor()
            
            mycursor.execute("SELECT * FROM disorders")
            
            myresult = mycursor.fetchall()
            
            return myresult

    except mariadb.Error as e:
        print(f"Error connecting to MariaDB platform: {e}")