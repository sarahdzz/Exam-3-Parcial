import requests
import socket

def inf_maquina():
    try:
        
        respuesta = requests.get('http://api.ipify.org/?format=json') #Solicitud GET-API
        if respuesta.status_code == 200: # Verificar si fue exitosa (código de estado 200)
            datos = respuesta.json()
            print("Hostname:", socket.gethostname())  # Imprimir el hostname y la dirección IP
            print("IP:", datos['ip'])# Dirección IP
        else:
            print("Error al obtener la información del sistema. Código de estado:", respuesta.status_code)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    inf_maquina()