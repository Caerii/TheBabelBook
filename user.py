from baseObject import baseObject
import hashlib

class user(baseObject):
    """User class that stores user information."""
    def __init__(self):
        """Initialize the user class."""
        self.setup('jakirab_sofia_users')
        self.roles = [{'value':'admin','text':'admin'},{'value':'user','text':'user'}]
    def hashPassword(self,pw):
        """Hash the password in order to store it in the database."""
        pw = pw+'xyz'
        return hashlib.md5(pw.encode('utf-8')).hexdigest()
    def verify_new(self,n=0):
        """Verify that the user is valid before inserting into the database."""
        if self.data[n]['email'] == '':
            self.errors.append('Email cannot be blank.')
        if '@' not in self.data[n]['email']:
            self.errors.append('Email must contain @.')
        u = user()
        u.getByField('email',self.data[n]['email'])
        if len(u.data) > 0:
            self.errors.append('Email already in use.')
        if len(self.data[n]['password']) < 2:
            self.errors.append('Password must be > 1 chars.')
        else:
            self.data[n]['password'] = self.hashPassword(self.data[n]['password'])
        if len(self.errors ) == 0:
            return True
        else:
            return False
        
    def verify_update(self,n=0):
        """Verify that the user is valid before updating the database."""
        if self.data[n]['email'] == '':
            self.errors.append('Email cannot be blank.')
        if '@' not in self.data[n]['email']:
            self.errors.append('Email must contain @.')
        u = user()
        u.getByField('email',self.data[n]['email'])
        if len(u.data) > 0 and u.data[0]['id'] != self.data[n]['id']:
            self.errors.append('Email already in use.')
            
            
        if len(self.data[n]['password']) > 0: #user intends to change pw
            if self.data[n]['password'] != self.data[n]['password2']:
                self.errors.append('Retyped password must match.')
            if len(self.data[n]['password']) < 5:
                self.errors.append('Password must be > 4 chars.')
            else:
                self.data[n]['password'] = self.hashPassword(self.data[n]['password'])
        else:
            del self.data[n]['password']
              
        if len(self.errors ) == 0:
            return True
        else:
            return False 
    def tryLogin(self, email, password):
        """Try to login with the email and password."""
        hpw = self.hashPassword(password)
        
        sql = f"SELECT * FROM `{self.tn}` WHERE `email` = %s AND `password` = %s;"
        #print(sql,email,password,hpw)
        self.cur.execute(sql,(email,hpw))
        self.data = []
        for row in self.cur:
            self.data.append(row)
        if len(self.data) == 1:
            return True
        else:
            return False
    def dropDownList(self):
        """Return a list of users for use in a drop down list."""
        choices = []
        for item in self.data:
            d = {}
            d['value'] = item[self.pk]
            d['text'] = f"{item['name']} ({item['email']})"
            choices.append(d)
        return choices
    def attachRelated(self,treename,tree):
        """Attach treenode data to the user."""

    