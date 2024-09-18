dizionario_iniziale = {"a": 1, "b": 2, "c": 3}

# Creazione di un nuovo dizionario con chiavi e valori scambiati
dizionario_scambiato = {v: k for k, v in dizionario_iniziale.items()}

# Stampare il nuovo dizionario
print(dizionario_scambiato)