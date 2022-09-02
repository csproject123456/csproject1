import mysql.connector
import datetime
now = datetime.datetime.now()
mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="stock")
mycursor=mydb.cursor(buffered=True)

def create_database():
    

    mydb = mysql.connector.connect(host='localhost',user='root',password='root',database='stock')  # change as per system
    mycursor = mydb.cursor()   
    sql = \
        "CREATE TABLE if not exists product (\
                  pcode int(10) PRIMARY KEY,\
                  pname char(30) NOT NULL,\
                  pprice float(8,2) ,\
                  pqty int(10) ,\
                  pcat char(30));"
    mycursor.execute(sql)
    sql = \
        "CREATE TABLE if not exists orders (\
                  orderid int(6)PRIMARY KEY ,\
                  orderdate DATE ,\
                  pcode char(30) NOT NULL , \
                  pprice float(8,2) ,\
                  pqty int(10) ,\
                  supplier char(50),\
                  pcat char(30));"
    mycursor.execute(sql)

    sql = \
        "CREATE TABLE if not exists sales (\
                  salesid int(4) PRIMARY KEY ,\
                  salesdate DATE ,\
                  pcode char(30) references product(pcode), \
                  pprice float(8,2) ,\
                  pqty int(4) ,\
                  Total double(8,2)\
                  );"
    mycursor.execute(sql)
    sql = \
        "CREATE TABLE if not exists user (\
                  uid char(20) PRIMARY KEY,\
                  uname char(30) NOT NULL,\
                  upwd char(30));"
    mycursor.execute(sql)
create_database()
print("  Welcome  ")

print("1.Create Account? ")
print("2.Login Account")

ask=input("Enter Choice")

while True:
    if ask=="1":
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="stock")
        mycursor=mydb.cursor()
        uid=input("Enter emaid id :")
        name=input(" Enter Name :")
        paswd=input("Enter Password :")
        sql="INSERT INTO user values (%s,%s,%s);"
        val=(uid,name,paswd)
        mycursor.execute(sql,val)
        '''sql="select uid from user where uid=%s;"
        val=(uid,)'''
        
        mydb.commit()
        print(mycursor.rowcount, " user created")
        
        
        break
    if ask=="2":
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="stock")
        mycursor=mydb.cursor()
        askemail=input("enter emailid")
        askpass=input("enter password")
        sql="select * from user where uid=%s and upwd=%s;"
        data=(askemail,askpass)
        mycursor.execute(sql,data)
        myresult=mycursor.fetchall()
        if myresult==[]:      
            print("Email Id And Password  doesnt  match")
        else:
            break
def product_management():
    while True:
        print ('\t\t\t 1. Add New Product')
        print('\t\t\t 2. List Product')
        print( '\t\t\t 3. Update Product')
        print( '\t\t\t 4. Delete Product')
        print( '\t\t\t 5. Back (Main Menu)')
        p = int(input('\t\tEnter Your Choice :'))
        if p == 1:
            addproduct()
        if p == 2:
            listproduct()
        if p == 3:
           modifyproduct()
        if p == 4:
            deleteproduct()
        if p == 5:
            break        
def sales_mgmt( ):
           while True :
                      print("\t\t\t 1. Sale Items")
                      print("\t\t\t 2. List Sales")
                      print("\t\t\t 3. Back (Main Menu)")
                      s=int (input("\t\tEnter Your Choice :"))
                      if s== 1 :
                                 saleitem()
                      if s== 2 :
                                 sale()
                      if s== 3 :
                                 break

def addproduct():
    pcode=int(input("enter the product code:"))
    pname=input("enter the product name:")
    pqty=int(input("enter the quantity to buy"))
    pprice=int(input("enter the price of the product"))
    pcat=input("enter category")
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="stock")
    mycursor=mydb.cursor()
    sql="insert into product values(%s,%s,%s,%s,%s);"
    data=(pcode,pname,pqty,pprice,pcat)
    mycursor.execute(sql,data)
    mydb.commit()
def modifyproduct():
    while True:
        print("Choose which data to be modified")
        print("1.Product Name")
        print("2.Product Quantitity")
        print("3.Product Price")
        ask=int(input("enter your choice"))
        code=int(input("Enter the product code :"))
        if ask==1:
            name=input("enter the new name:")
            sql="UPDATE product SET pname=%s where pcode=%s;"
            val=(name,code)
            mycursor.execute(sql,val)
            mydb.commit()
            print("\t\t Product details updated")
        if ask==2:
            qty=int(input("Enter the quantity :"))
            sql="UPDATE product SET pqty=%s where pcode=%s;"
            val=(qty,code)
            mycursor.execute(sql,val)
            mydb.commit()
            print("\t\t Product details updated")
        if ask==3:
            price=int(input("enter the price"))
            sql="UPDATE product SET pprice=%s where pcode=%s;"
            val=(price,code)
            mycursor.execute(sql,val)
            print("\t\t Product details updated")
            mydb.commit()
        if ask==4:
            break
def deleteproduct():
           mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="stock")
           mycursor=mydb.cursor()
           code=int(input("Enter the product code :"))
           sql="DELETE FROM product WHERE pcode = %s;"
           val=(code,)
           mycursor.execute(sql,val)
           mydb.commit()
           print(mycursor.rowcount," record(s) deleted");

def listproduct():
           mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="stock")
           mycursor=mydb.cursor()
           sql="SELECT * from product;"
           mycursor.execute(sql)
           print("\t\t\t\t PRODUCT DETAILS")
           print("\t\t","-"*46)
           print("\t\t code    name    price   quantity      category")
           print("\t\t","-"*46)
           for i in mycursor:
                      print("\t\t",i[0],"\t",i[1],"\t",i[2],"\t   ",i[3],"\t\t",i[4])
           print("\t\t","-"*46)
def saleitem():
           mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="stock")
           mycursor=mydb.cursor()
           pcode=input("Enter product code: ")
           sql4="SELECT count(*) from product WHERE pcode=%s;"
           val4=(pcode,)
           mycursor.execute(sql4,val4)
           qty=int(input("Enter no of quantity to sell :"))
           '''sql5="select pqty from product where pcode=%s;"
           val=(pcode,)
           mycursor.execute(sql5,val)
           qtycheck=mycursor.fetchall()
           
           if qtycheck<qty:
               print("Not enough quantity to sell")
               mydb.commmit()
           else:               '''
           price=int(input("enter the price in which each quantity is to be sold:"))
           totalprice=price*qty
           print("Collect Rs:",totalprice)
           sql2="UPDATE product SET pqty=pqty-%s WHERE pcode=%s;"      
           val=(qty,pcode)
           mycursor.execute(sql2,val)
           print("successfully sold")
           sql="select price from product where pcode=%s;"
           val=(pcode,)
           mycursor.execute(sql,val)
           profitcheck=mycursor.fetchall()
           profit=price-profitcheck
           print("total profit" , profit)
           sql="insert into sales values(salesid,saledate,pcode,pprice,pqty);"
           mydb.commit()
               
while True:
    print("\t\t\t STOCK MANAGEMENT")
    print("\t\t\t ****************\n")
    print("\t\t 1. PRODUCT MANAGEMENT")
    print("\t\t 2. PURCHASE MANAGEMENT")
    print("\t\t 3. SALES MANAGEMENT")
    print("\t\t 4. EXIT\n")
    n=int(input("Enter your choice :"))
    if n== 1:
        product_management()
    if n== 3:
        sales_mgmt()
    if n== 4:
        break
                       
    
    
