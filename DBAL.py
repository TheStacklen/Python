#CONNECTION
import pymysql
def connection():
    conn=pymysql.connect(host="Localhost",
                           user="root",
                           password="sakln7794",
                           db="EMS")
    return conn
def getData():
    con=connection()
    cursor=con.cursor()
    cursor.execute("select * from Employee")
    data=cursor.fetchall()
    return data
def insertData():
    con=connection()
    cursor=con.cursor()
    cursor.execute(f" INSERT INTO Employee (EmpID,EmpName,DOJ,salary,Department,Age,country,contact) values({obj.empID},'{obj.empName}','{obj.DOJ}',{obj.salary},{obj.depID},{obj.age},'{obj.country}',{obj.contact})")
    con.commit()
    con.close()
def updateData():
    con=connection()
    cursor=con.cursor()
    cursor.execute(f"update Employee set '{obj2.Name}' where {obj2.id}")
    con.commit()
    con.close()
def deleteData():
    con=connection()
    cursor=con.cursor()
    cursor.execute("delete from Employee where {obj3.name}")
    con.commit()
    
    
    
    
    
