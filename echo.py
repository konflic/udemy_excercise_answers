import socket
import random

from http import HTTPStatus
import urllib.parse as urlparse

LOCALHOST = "127.0.0.1"

def random_port():
    return random.randint(20000, 30000)
    
my_socket = socket.socket()
ipadd_port = (LOCALHOST, random_port())

print("Connect: ", ipadd_port)
my_socket.bind(ipadd_port)
my_socket.listen(1)

while True:

    connection, address = my_socket.accept()
    con_data = connection.recv(4096)

    data_from_client = con_data.decode("utf-8").split("\n")
    first_line = data_from_client[0]
    status = HTTPStatus(200)

    if "status=" in first_line:
        try:
            status_int = int(urlparse.urlparse(first_line.split(" ")[1]).query.split("=")[1])
            status = HTTPStatus(status_int)
        except:
            pass

    status_string = f"{status.value} {status.phrase}"
    method = first_line.split(" ")[0]
    response_data = f"HTTP/1.1 {status_string}\r\nContent-Type:text/html\r\n\r\n<h2>Got headers:</h2>\r\n"

    response_data += f"<p>Request Method: {method}</p>"
    response_data += f"<p>Request Source: {address}</p>"
    response_data += f"<p>Response Status: {status_string}</p>"

    for header in data_from_client:
        if ":" in header:
            response_data += f"<p>{header}</p>"

    connection.send(response_data.encode("utf-8"))
    connection.close()
