import socket
import threading

# Definizione dell'indirizzo e della porta del client
client_address = ("127.0.0.1", 22223)  # localhost
BUFFER_SIZE = 1024  # Numero massimo di byte per messaggi

# Creazione del socket UDP del client
udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_client_socket.bind(client_address)

print(f"Client avviato su {client_address}")

# Funzione per ricevere messaggi dal server
def receive_messages():
    while True:
        data, address = udp_client_socket.recvfrom(BUFFER_SIZE)
        print(f"Server: {data.decode()}")

# Avvio di un thread separato per la ricezione dei messaggi
receive_thread = threading.Thread(target=receive_messages)
receive_thread.daemon = True
receive_thread.start()

# Ciclo per inviare messaggi al server
while True:
    message = input("Client: ")
    udp_client_socket.sendto(message.encode(), ("127.0.0.1", 22222))  # Indirizzo del server

# Chiusura del socket alla fine (anche se non si arriverà mai qui nel ciclo infinito)
udp_client_socket.close()