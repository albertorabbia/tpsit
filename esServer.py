import socket

# Imposta l'indirizzo del server e la porta
server_ip = '127.0.0.1'  # Usa localhost per testare in locale
server_port = 22222

# Crea un socket TCP/IP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Lega il socket all'indirizzo e alla porta specificati
server_socket.bind((server_ip, server_port))

# Inizia ad ascoltare le connessioni
server_socket.listen(1)
print(f'Server in ascolto su {server_ip}:{server_port}')

# Accetta una connessione
conn, addr = server_socket.accept()
print(f'Connessione stabilita con {addr}')

# Funzione per ricevere e stampare i tasti premuti
def handle_client_connection(conn):
    while True:
        data = conn.recv(1024)  # Riceve dati in blocchi di 1024 byte
        if not data:
            break
        print(f'Tasto ricevuto: {data.decode()}')

    # Chiude la connessione
    conn.close()

# Avvia la gestione della connessione
handle_client_connection(conn)

# Chiude il socket server
server_socket.close()