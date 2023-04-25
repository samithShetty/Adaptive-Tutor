from mysql import connector

# Function to create an account (register).
def register_user(user_, pass_, email_):
    
    try:
        with connector.connect(
            host = "localhost",
            user = "root",
            password = "3Schmoos!"
        ) as database:
            print(database)
    except connector.Error as e:
        print(e)

    database.reconnect()

    try:
      with connector.connect(
          host = "localhost",
          user = "root",
          password = "3Schmoos!",
          database = "python_login"
      ) as database:
          print(database)
    except connector.Error as e:
      print(e)
    
    database.reconnect()

    sql = "INSERT INTO accounts (username, password, email) VALUES (%s, %s, %s)"
    val = (user_, pass_, email_)

    with database.cursor() as cursor:
        cursor.execute(sql, val)
        database.commit()

    print(cursor.rowcount, "record inserted.")

# Function to check if user/pass combination exists (login).
def login_user(user_, pass_):
  
    try:
      with connector.connect(
          host = "localhost",
          user = "root",
          password = "3Schmoos!"
      ) as database:
          print(database)
    except connector.Error as e:
      print(e)

    database.reconnect()

    try:
      with connector.connect(
        host = "localhost",
        user = "root",
        password = "3Schmoos!",
        database = "python_login"
    ) as database:
        print(database)
    except connector.Error as e:
      print(e)
  
    database.reconnect()

    sql = "SELECT password FROM accounts WHERE username = " + user_ 
    #print(sql)

    with database.cursor(buffered=True) as cursor:
      cursor.execute(sql)

    myresult = cursor.fetchall()

    myresult = ' '.join(myresult[0])
    #print(myresult)
    #print(pass_)

    if myresult == pass_:
       print('successful login!')

#login_user("'testuser'", "testpass")
#register_user("testuser2", "testpass2", "testemail2")