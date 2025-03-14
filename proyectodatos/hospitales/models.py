from django.db import models
import oracledb

# Create your models here.
class Departamento:
    numero = 0
    nombre = ""
    localidad = ""
    
class Hospital:
    id = 0
    nombre = ""
    direccion = ""
    telefono = ""
    num_cama = 0
    
class Empleados:
    id = 0
    apellido =""
    oficio = ""
    salario = 0
    no_dept = 0
    
    
    
class ServiceDepartamentos:
    def __init__(self):
        self.connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')
        
    def getDepartamentos(self):
        sql ="select * from dept"
        cursor = self.connection.cursor()
        cursor.execute(sql)
        lista=[]
        for row in cursor:
            dept=Departamento()
            dept.numero=row[0]
            dept.nombre=row[1]
            dept.localidad=row[2]
            lista.append(dept)
        cursor.close()
        return lista
    
    def insertDepartamentos(self, numero, nombre, localidad):
        sql= "insert into dept values(:p1, :p2, :p3) " 
        cursor = self.connection.cursor()
        cursor.execute(sql, (numero, nombre, localidad))
        registros = cursor.rowcount
        self.connection.commit()
        cursor.close()
        return registros
    
    def deleteDepartamentos(self, numero):
        sql= "delete from dept where dept_no = :p1 " 
        cursor = self.connection.cursor()
        cursor.execute(sql, (numero,))
        registros = cursor.rowcount
        self.connection.commit()
        cursor.close()
        return registros
    
    def updateDepartamentos(self, nombre, localidad, numero):
        sql= "update dept set dnombre= :p1, loc = :p2 where dept_no = :p3 " 
        cursor = self.connection.cursor()
        cursor.execute(sql, (nombre, localidad, numero))
        registros = cursor.rowcount
        self.connection.commit()
        cursor.close()
        return registros
    
    def detallesDepartamento(self, numero):
        sql = "select * from dept where dept_no= :p1"
        cursor = self.connection.cursor()
        cursor.execute(sql, (numero, ))
        row = cursor.fetchone()
        dept= Departamento()
        dept.numero = row [0]
        dept.nombre = row [1]
        dept.localidad = row [2]
        cursor.close()
        return dept
           
class ServiceHospitales:
    def __init__(self):
        self.connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')  
    
    def getHospitales(self):
        sql ="select * from hospital"
        cursor = self.connection.cursor()
        cursor.execute(sql)
        lista=[]
        for row in cursor:
            hosp=Hospital()
            hosp.id=row[0]
            hosp.nombre=row[1]
            hosp.direccion=row[2]
            hosp.telefono=row[3]
            hosp.num_cama=row[4]
            lista.append(hosp)
        cursor.close()
        return lista
    
class ServiceEmpleados:
    def __init__(self):
        self.connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')
        
    def getEmpleados(self):
        sql ="select * from emp"
        cursor = self.connection.cursor()
        cursor.execute(sql)
        lista=[]
        for row in cursor:
            emp=Empleados()
            emp.id=row[0]
            emp.apellido=row[1]
            emp.oficio=row[2]
            emp.salario=row[5]
            emp.no_dept=row[7]
            lista.append(emp)
        cursor.close()
        return lista
    
    def filtraEmpleados(self, dept):
        sql ="select * from emp where dept_no=:p1"
        cursor = self.connection.cursor()
        cursor.execute(sql, (dept,))
        lista=[]
        for row in cursor:
            emp=Empleados()
            emp.id=row[0]
            emp.apellido=row[1]
            emp.oficio=row[2]
            emp.salario=row[5]
            emp.no_dept=row[7]
            lista.append(emp)
        cursor.close()
        return lista