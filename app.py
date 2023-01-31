import mariadb
import dbcreds


def verify_user():
    
    conn = mariadb.connect(
                            user = dbcreds.user,
                            password = dbcreds.password,
                            host = dbcreds.host,
                            port = dbcreds.port,
                            database = dbcreds.database
                            )
    cursor = conn.cursor()
    username = input("Enter username:")
    password = input("Enter password:")
    cursor.execute("CALL add_command(?,?)", [username,password])
    result = cursor.fetchall()
    print(result)
    cursor.close()
    conn.close()
    if result:
        return result
    else:
        return None 


def insert_post():

    conn = mariadb.connect(
                            user = dbcreds.user,
                            password = dbcreds.password,
                            host = dbcreds.host,
                            port = dbcreds.port,
                            database = dbcreds.database
                            )
    cursor = conn.cursor()
    client_id = int(input("Enter client_id: "))
    if client_id == 1:
        content = input("Enter content: ")
        title = input("Enter title: ")
        cursor.execute("CALL insert_post(?,?,?)",[client_id,content,title])
        conn.commit()
        cursor.close()
        conn.close
        return
# When inserting use conn commit not cursor fetchall. Also no WHERE CLAUSE in insert procedures/queries
    elif client_id == 2:
        content = input("Enter content: ")
        title = input("Enter title: ")
        cursor.execute("CALL insert_post(?,?,?)",[client_id,content,title])
        conn.commit()
        cursor.close()
        conn.close
        return
    elif client_id == 3:
        content = input("Enter content: ")
        title = input("Enter title: ")
        cursor.execute("CALL insert_post(?,?,?)",[client_id,content,title])
        conn.commit()
        cursor.close()
        conn.close
        return
    else:
        client_id >= 4
        print("Client id not found in database")
        cursor.close()
        conn.close
    return



def retrieve_post():

    conn = mariadb.connect(
                            user = dbcreds.user,
                            password = dbcreds.password,
                            host = dbcreds.host,
                            port = dbcreds.port,
                            database = dbcreds.database
                            )
    cursor = conn.cursor()
    print("You have now activated the Read all Posts function")
    cursor.execute("SELECT title, content FROM post")
    result = cursor.fetchall()
    print(result)
    cursor.close()
    conn.close
    return


def log_user_infinite():

    conn = mariadb.connect(
                            user = dbcreds.user,
                            password = dbcreds.password,
                            host = dbcreds.host,
                            port = dbcreds.port,
                            database = dbcreds.database
                            )
    cursor = conn.cursor()
    
    username = input("Enter username: ")
    password = input("Enter password: ")
        
    cursor.execute("CALL add_command(?,?)", [username,password])
    result = cursor.fetchall()
    if len(result) == 1:
        print(result)
        print("Logged in successfully")
        cursor.close()
        conn.close()
    elif len(result) == 0:    
        is_valid = False
        while not is_valid:
            try:
                is_valid = True
                log_user_infinite()
            except ValueError:
                print("Unreachable print. Just a placeholder")



def start_process():

    is_valid = False
    while not is_valid:
        pass1= input("Enter option: ")
        try:
            pass1 = int(pass1)
            is_valid = True
        except ValueError:
            print("Wrecked ser")

    if pass1 == 1:
        print("Option 1 selected: Insert a new post")
        insert_post()
        return
    elif pass1 == 2:
        print("Option 2 selected: Read all posts")
        retrieve_post()
        return
    elif pass1 == 3:
        print("Goodbye! ")
        return
    else:
        pass1 >= 4
        print("Error: INPUT SPECIFIED OPTIONS ONLY")
        return


print("Hello Sir/Madam. Select from the following options:\
    \n1. Insert a new post\
    \n2. Read all posts\
    \n3. Quit")

start_process()
# insert_post()
# retrieve_post()
# log_user_infinite()