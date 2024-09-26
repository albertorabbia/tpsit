import socket
import threading

# Definizione dell'indirizzo e della porta del server
server_address = ("127.0.0.1", 22222)  # localhost
BUFFER_SIZE = 1024  # Numero massimo di byte per messaggi

# Creazione del socket UDP del server
udp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_server_socket.bind(server_address)

print(f"Server avviato su {server_address}")

# Funzione per ricevere messaggi dal client
def receive_messages():
    while True:
        data, address = udp_server_socket.recvfrom(BUFFER_SIZE)
        print(f"Client: {data.decode()}")

# Avvio di un thread separato per la ricezione dei messaggi
receive_thread = threading.Thread(target=receive_messages)
receive_thread.daemon = True
receive_thread.start()

# Ciclo per inviare messaggi al client
while True:
    message = input("Server: ")
    udp_server_socket.sendto(message.encode(), ("127.0.0.1", 22223))  # Indirizzo del client

# Chiusura del socket alla fine (anche se non si arriverà mai qui nel ciclo infinito)
udp_server_socket.close()