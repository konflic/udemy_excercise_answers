import socket
import random

LOCALHOST = "127.0.0.1"

def random_port():
    return random.randint(20000, 30000)
    
my_socket = socket.socket()
ipadd_port = (LOCALHOST, random_port())

print("Connect: ", ipadd_port)
my_socket.bind(ipadd_port)
my_socket.listen(1)

connection, address = my_socket.accept()

con_data = connection.recv(4096)

print(con_data)

data_from_client = con_data.decode("utf-8")
headers = data_from_client.split("\n")

response_data = "HTTP/1.1 200 OK\r\nContent-Type:text/html\r\n\r\n<h2>Got headers:</h2>\r\n"

for header in headers:
    if ":" in header:
        response_data += f"<p>{header}</p>"

response_data = response_data

response_data = f"{response_data}"

connection.send(response_data.encode("utf-8"))

my_socket.close()
