def login(username, password, userdb, sessiondb):
    if(userdb.query_all().first()==userdb):
        print('nice')

