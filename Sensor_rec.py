from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import pyautogui


s = socket(AF_INET, SOCK_STREAM)
print("socket created")
port = 9999
s.bind(('192.168.104.177', port))


global timestamp
global acceleration
timestamp=[]
acceleration=[]
def accept_client_connections():
    while True:
        client, client_address = s.accept()
        print("%s:%s has connected" % client_address)
        Thread(target=client_handler, args=(client,)).start()

def client_handler(client):
    sensor='linear acceleration sensor'
    while True:
        try:
            data = eval(client.recv(1024).decode())
            print(data)
            x_gyro=data[sensor][0]
            y_gyro=data[sensor][1]
            z_gyro=data[sensor][2]
            x_input=x_gyro*50
            y_input=y_gyro*30
            pyautogui.move(x_input, y_input)
            if not data:
                break

        except Exception as e:
            print(e)
            continue





if __name__ == "__main__":

    s.listen(5)
    print("Waiting for connection...")

    ACCEPT_THREAD = Thread(target=accept_client_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    s.close()

