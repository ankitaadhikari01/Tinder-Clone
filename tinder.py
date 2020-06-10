import guihelper
import dbhelper

class Tinder(guihelper.GUI):
    def __init__(self):
        #Open login window
        self._dbObject=dbhelper.DBHelper()
        super().__init__(self.loginHandler,self.regHandler)

    def loginHandler(self,email,password):
        response=self._dbObject.search("email",email,"password",password,"users")
        if len(response)==0:
            print("Invalid Email Or Password")
        else:
            self.user_id=response[0][0]
            a = email
            b = password
            self.doLogin(response,a,b)


    def viewHandler(self):
        super().viewWindow(self.a,self.b)
        response=self._dbObject.search("email",a,"password",b,"users")
        self.mainWindow(a,b)
        print(a,b)
        """if len(response)==0:
            print("Invalid Email or Password")
        else:
            self.user_id=response[0][0]
            self.view(response)"""


    def doLogin(self,data,a,b):
        self.mainWindow(self,data,a,b,mode=1)

    def view(self,data):
        self.veiwWindow(self,data,mode=0)

    #def doLogout(self,data):
     #   self.logoutWindow()



    def viewUsers(self,a,b,num):
        data=[]
        response=self._dbObject.searchOne('user_id',self.user_id,'users','NOT LIKE')

        if num<0:
            self.printMessage("Error","No Users Before This One,,Out Of Range")

        elif num>len(response)-1:
            self.printMessage("Error","No Users After This One,,Out of Range")

        else:
            x = response[num]
            data.append(x)
            self.mainWindow(self, data,a,b, mode=2, num=num)


    def regHandler(self,name,email,password,age,gender,city,bio):

        mydict={
            'user_id':"NULL",
            'fname':name,
            'email':email,
            'password':password,
            'age':age,
            'gender':gender,
            'bg':'avatar.jpg',
            'city':city,
            'bio':bio
        }

        flag=self._dbObject.insert(mydict,'users')
        if flag==0:
            print("Registration Failed")
        else:
            print("Registration Succesful")

    def propose(self,juliet_id):
        data=self._dbObject.search('romeo_id',self.user_id,'juliet_id',juliet_id,'proposals')

        if len(data)>0:
            self.printMessage("Error","Already Proposal Sent to this Person" )
        else:
            mydict = {
                'proposal_id': 'NULL',
                'romeo_id': self.user_id,
                'juliet_id': juliet_id
            }

            response = self._dbObject.insert(mydict, 'proposals')

            if response == 1:
                self.printMessage("Success", "Proposal sent successfully")
            else:
                self.printMessage("Proposal Failed", "Some Error Occured")


obj1=Tinder()