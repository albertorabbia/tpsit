def calcola_fattoriale(n):
    if n == 0:
        return 1
    else:
        return n * calcola_fattoriale(n - 1)

numero = int(input("Inserisci un numero intero positivo: "))

if numero < 0:
    print("Il fattoriale di numeri negativi non è definito.")
elif numero == 0:
    print("Il fattoriale di 0 è 1.")
else:
    risultato = calcola_fattoriale(numero)
    print(f"Il fattoriale di {numero} è {risultato}.")