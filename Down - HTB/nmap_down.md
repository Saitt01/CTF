## 📡 Nmap Scan

### Comando eseguito:

nmap -sC -sV ip_target


### Output:

Starting Nmap 7.95 ( https://nmap.org ) at 2025-06-20 06:36 CEST

Nmap scan report for 10.129.232.247 (10.129.232.247)

Host is up (0.11s latency).

Not shown: 998 closed tcp ports (reset)

PORT STATE SERVICE VERSION

22/tcp open ssh OpenSSH 8.9p1 Ubuntu 3ubuntu0.11 (Ubuntu Linux; protocol 2.0)

| ssh-hostkey:

| 256 f6:cc:21:7c:ca:da:ed:34:fd:04:ef:e6:f9:4c:dd:f8 (ECDSA)

|_ 256 fa:06:1f:f4:bf:8c:e3:b0:c8:40:21:0d:57:06:dd:11 (ED25519)

80/tcp open http Apache httpd 2.4.52 ((Ubuntu))

|_http-title: Is it down or just me?

|_http-server-header: Apache/2.4.52 (Ubuntu)

Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel


Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .

Nmap done: 1 IP address (1 host up) scanned in 11.69 seconds

