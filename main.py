from MdbSupport import MDBSupport

def main():
    mdb=MDBSupport()
    while True:
        print()
        print()
        print('YOU CAN SELECT OPTION FOR PROCESS')
        print()
        print('PRESS 1 > INSERT NEW USER NAME')
        print('PRESS 2 > DISPLAY ALL DATA')
        print('PRESS 3 > DELETE USER')
        print('PRESS 4 > UPDATE USER')
        print('PRESS 5 > EXIT')
        print()
        try:
            choice=int(input())
            if(choice==1):
                #insert user
                userId=int(input("Enter User ID :"))
                userName=input("Enter User Name :")
                userPhone=input("Enter User Phone :")
                mdb.insert_uData(userId, userName, userPhone)
                

            elif(choice==2):
                #Display User
                mdb.fetch_all()
                
                pass
            elif(choice==3):
                #Delete User
                userId=int(input("Enter User ID :"))
                mdb.delete_user(userId)
                

            elif(choice==4):
                #Update User
                userId=int(input("Enter Id of Update User :"))
                userName=input("Enter New User Name :")
                userPhone=input("Enter New User Phone :")
                mdb.update_user(userId, userName, userPhone)
                

            elif(choice==5):
                #Exit
                break
            else:
                print('PLEASE SELECT VALID CHOICE NUMBER')

        except Exception as e:
            print(e)
            print('INVALID PROCESS')

if __name__=="__main__":
    main()

