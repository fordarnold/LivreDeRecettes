#!/usr/bin/env python
from eve import Eve
from eve.auth import BasicAuth

class Authenticate(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource, method):
        print resource
        print method 
        if resource == 'user' and method == 'GET':
            user = app.data.driver.db['user']
            user = user.find_one({'username': username,'password':password})
            
            if user:
                return True
            else:
                return False
        elif resource == 'user' and method == 'POST':
            print username
            print password
            return username == 'admin' and password == 'password'
        else:
            return True
            
# run the app when the program is executed as a main program
if __name__ == '__main__':
    app = Eve(auth=Authenticate)
    app.run()