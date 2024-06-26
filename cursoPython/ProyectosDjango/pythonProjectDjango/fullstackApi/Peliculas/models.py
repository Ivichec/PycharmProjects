import requests
import json
import cx_Oracle


class Empleado1:
    def __init__(self):
        self.connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")

    def insertdato(self, idper, nombre, img, idserie):
        apiurl = "https://apiseriespersonajes.azurewebsites.net/api/Personajes"
        departamento = {"idPersonaje": idper, "nombre": nombre, "imagen": img , "idSerie": idserie}
        response = requests.post(apiurl, json=departamento)
        print("Status: " + str(response.status_code))
    def baja(self, dept_no):
        cursor = self.connection.cursor()
        try:
            consulta = "DELETE FROM DEPT WHERE DEPT_NO = :p1"
            cursor.execute(consulta, (dept_no,))
            self.connection.commit()
            return True
        except cx_Oracle.DatabaseError as error:
            print("Error: ", error)
            return False
        finally:
            cursor.close()
    def modificar(self, dept_no,loc):
        cursor = self.connection.cursor()
        try:
            consulta = "UPDATE DEPT SET LOC = :p1 WHERE DEPT_NO = :p2"
            cursor.execute(consulta, (loc,dept_no))
            self.connection.commit()
        except cx_Oracle.DatabaseError as error:
            print("Error: ", error)
        finally:
            cursor.close()
    def devolverdato(self):
        api_url = "https://apiseriespersonajes.azurewebsites.net/api/Series"
        response = requests.get(api_url)
        series = response.json()
        return series
    def devolverserie(self,serie):
        api_url = "https://apiseriespersonajes.azurewebsites.net/api/Series/PersonajesSerie/"+serie
        response = requests.get(api_url)
        series = response.json()
        return series
