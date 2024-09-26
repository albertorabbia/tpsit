import socket
import time

# Definizione dell'indirizzo e della porta del server
server_address = ("127.0.0.1", 22222)  # localhost
BUFFER_SIZE = 1024  # Numero di byte massimo che il client può ricevere

# Creazione del socket UDP del client
udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Inviare 10 messaggi al server
for i in range(10):
    # Definizione del messaggio da inviare
    message = f"Messaggio {i + 1} dal client"
    
    # Invio del messaggio al server
    udp_client_socket.sendto(message.encode(), server_address)
    
    # Ricezione della risposta dal server
    data, address = udp_client_socket.recvfrom(BUFFER_SIZE)
    
    # Decodifica della risposta ricevuta
    print(f'Risposta ricevuta dal server: {data.decode()}')
    
    # Attendere 1 secondo prima di inviare il prossimo messaggio
    time.sleep(1)

# Chiusura del socket
udp_client_socket.close()
print("Client chiuso.")