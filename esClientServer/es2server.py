import socket

# Definizione dell'indirizzo e della porta del server
server_address = ("127.0.0.1", 22222)  # localhost
BUFFER_SIZE = 1024  # Numero di byte massimo che il server può ricevere

# Creazione del socket UDP del server
udp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_server_socket.bind(server_address)

print("Server in ascolto su", server_address)

# Ciclo per ricevere 10 messaggi dal client
for i in range(10):
    # Ricezione dei dati dal client
    data, address = udp_server_socket.recvfrom(BUFFER_SIZE)
    
    # Decodifica del messaggio ricevuto
    print(f'Messaggio {i + 1} ricevuto dal client: {data.decode()}')
    
    # Risposta al client
    response_message = f"Ricevuto il messaggio {i + 1}"
    udp_server_socket.sendto(response_message.encode(), address)

# Chiusura del socket
udp_server_socket.close()
print("Server chiuso.")