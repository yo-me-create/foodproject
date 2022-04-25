import mysql.connector as connector

class MDBSupport:
    def __init__(self):
        self.con = connector.connect(
                        host='localhost',
                        port='3306',
                        user='root',
                        password='root',
                        database='yogen'
                        )
# If not exists whenever you fire query not create        duplicate table becouse here alredy exists
        query='create table if not exists uData(userId int primary key,userName varchar(50),phone varchar(12))'
        cur=self.con.cursor()
        cur.execute(query)
        print('Created Success')

    #Insert
    def insert_uData(self,userId,userName,phone):
        query = "insert into uData(userId,userName,phone) values({},'{}','{}')".format(userId, userName, phone)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print('User Data Successfully Saved')

    #Fetch All
    def fetch_all(self):
        query='select * from uData'
        cur=self.con.cursor()
        cur.execute(query)
        for data in cur:
            print('User Id:',data[0])
            print('User Name:',data[1])
            print('User Phone:',data[2])

    def delete_user(self, userId):
        query='delete from uData where userId={}'.format(userId)
        #print(query)
        d=self.con.cursor()
        d.execute(query)
        print('Deleted success')

    def update_user(self,userId,newName,newPhone):
        query="update uData set userName='{}',Phone='{}'where userID={}".format(newName,newPhone,userId)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print('Update Success')

