from django.db import models
import oracledb

class Serie():
    idserie=0
    nombre=""
    imagen=""
    year=0
    
class Personaje():
    idperson=0
    nombre=""
    imagen=""
    idserie=0
    
class ServiceSeries():
    def __init__(self):
        self.connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')
        
    def getSeries(self):
        sql="select * from series"
        cursor=self.connection.cursor()
        cursor.execute(sql)
        lista=[]
        for row in cursor:
            serie=Serie()
            serie.idserie=row[0]
            serie.nombre=row[1]
            serie.imagen=row[2]
            serie.year=row[3]
            lista.append(serie)
        cursor.close()
        return lista
    
class ServicePersonaje():
    def __init__(self):
        self.connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')
        
    def getPersonajes(self):
        sql="select * from personajes"
        cursor=self.connection.cursor()
        cursor.execute(sql)
        lista=[]
        for row in cursor:
            person=Personaje()
            person.idperson=row[0]
            person.nombre=row[1]
            person.imagen=row[2]
            person.idserie=row[3]
            lista.append(person)
        cursor.close()
        return lista
    
    def getPersonajesSeries(self):
        sql="select * from personajes where idserie=:p1"
        cursor=self.connection.cursor()
        cursor.execute(sql)
        lista=[]
        for row in cursor:
            person=Personaje()
            person.idperson=row[0]
            person.nombre=row[1]
            person.imagen=row[2]
            person.idserie=row[3]
            lista.append(person)
        cursor.close()
        return lista
        
