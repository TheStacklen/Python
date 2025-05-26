import DBAL
class Employee:
    def __init__(self,empID=1,empname="EmployeeName",DOJ="20-12-2024",salary=900,departmentID=10,age=19,country="India",contact=7879794548):
        self.empID=empID
        self.empname=empname
        self.DOJ=DOJ
        self.salary=salary
        self.department=departmentID
        self.age=age
        self.country=country
        self.contact=contact
    def get(self):
        data=DBAL.getData()
        return data
    def post(self):
        a=DBAL.insertData
        return a
    def put(self):
        s=DBAL.updateData
        return s
    def delete(self):
        r=DBAL.deleteData
        return r
        
