# Projekt iz kolegija Mreže računala 2 na Fakultetu organizacije i informatike

Serverska strana za mail sustav koji pruža forward secrecy.

# Pokretanje

Klonirajte repozitorij:

    git clone https://gitlab.com/viktoracoric/fsem-server.git

Pri prvom pokretanju pokrenite:

    python3 enkripcija.py e && sed -i 's/write_key()$/#write_key()/' enkripcija.py

Ova komanda se koristi za generiranje tajnog ključa ```key.key```.

Nakon ispunjenog zahtjeva iznad, server se pokreće s

    python3 main.py
