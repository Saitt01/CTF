## 🔍 Ricognizione Iniziale con Nmap

### ⚙️ Comando eseguito
```bash
nmap -sC -sV 10.129.151.196

## 📋 Risultato della scansione

Starting Nmap 7.95 ( https://nmap.org ) at 2025-05-23 14:50 CEST
Nmap scan report for 10.129.151.196 (10.129.151.196)
Host is up (0.041s latency).
Not shown: 996 filtered tcp ports (no-response)

PORT    STATE SERVICE     VERSION
21/tcp  open  ftp         vsftpd 2.3.4
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to 10.10.16.22
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      vsFTPd 2.3.4 - secure, fast, stable
|_End of status
|_ftp-anon: Anonymous FTP login allowed (FTP code 230)

22/tcp  open  ssh         OpenSSH 4.7p1 Debian 8ubuntu1 (protocol 2.0)
| ssh-hostkey: 
|   1024 60:0f:cf:e1:c0:5f:6a:74:d6:90:24:fa:c4:d5:6c:cd (DSA)
|_  2048 56:56:24:0f:21:1d:de:a7:2b:ae:61:b1:24:3d:e8:f3 (RSA)

139/tcp open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp open  netbios-ssn Samba smbd 3.0.20-Debian (workgroup: WORKGROUP)

Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Script results

smb-security-mode: 
  account_used: <blank>
  authentication_level: user
  challenge_response: supported
  message_signing: disabled (dangerous, but default)

smb2-time: Protocol negotiation failed (SMB2)
clock-skew: mean: 2h00m36s, deviation: 2h49m44s, median: 34s

smb-os-discovery: 
  OS: Unix (Samba 3.0.20-Debian)
  Computer name: lame
  Domain name: hackthebox.gr
  FQDN: lame.hackthebox.gr
  System time: 2025-05-23T08:51:35-04:00