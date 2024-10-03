

# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client.connect(('192.168.137.1', 22222))
# BUFFER_SIZE=4096
# messaggio="ciao"
# client.sendall(messaggio.encode())
# from_server = client.recv(BUFFER_SIZE).decode()
# print("I received from SERVER {from_server}")
# client.close()

# import socket

# host = '192.168.137.1'  # Indirizzo IP del server
# port = 22222         # Porta del server
# valore= 55
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.connect((host, port))
#     while True:
#     #invia i dati
#         message = input("inserici comando di movimento: ")
#         messaggio_da_inviare=f"{message[0]},{valore}"
#         s.sendall(messaggio_da_inviare.encode())
        
#     # Ricevi la risposta dal server
#         data = s.recv(1024)
#         print(data.decode())



# Crea un software che stampi il nome del tasto cliccato su tastiera (solo lettere)
# Usa la libreria:
# pynput

# dato che si vuole stampare solo le lettere, creo una lista contenente tutti i numeri della tastiera
numeri = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

#importo la libreria richiesta
from pynput import keyboard
import socket


# definisco la funzione che stampa le lettere quando sono premute
def on_press(key):
    # non riconosce i caratteri non numerici come delete, canc, ctrl, ecc...; ho bisogno di verificare che non sia un carattere di quelli se no alzano una eccezzione che gestisco
    try:
        # se il carattere è una lettera, lo stampo
        if key.char not in numeri and key.char != None:
            print('alphanumeric key {0} pressed'.format(key.char))
        
    except AttributeError:
        # se il carattere non è riconosciuto, quindi non è numerico, non lo stampo
        if key == keyboard.Key.esc:
            # Stop listener
            return False
        else:
            pass

# Creo un event listener, che per ogni evento generato dalla tastiera può fare qualcosa, keyboard.Listener(on_press=functionForKeyPressed, on_release=functionForKeyReleased)
# è un thread che termina quando viene premuto esc o quando terminato manualmente
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

# faccio partire il trhead e gli assegno la funzione on_press
listener = keyboard.Listener( on_press=on_press)
listener.start()