# Wstęp
W ramach wykladu 5 z BCYB - IoT Security zaprezentowano `Shodan CLI`
oraz pakiet `Shodan` dla `Python`. W ramach tutoriala:
* wyszukiwanie za pomocą `Shodan CLI`
  * publicznie otwarte serwisy VNC
* wykorzystanie API Shodana w skryptach `Python`
  * wyszukiwanie dostępnych brokerów MQTT
  * próba subskrypcji do znalezionych brokerów

Tutorial i zamieszczone kody przygotowano na podstawie: *Gray Hat Hacking: The Ethical Hacker's Handbook 5th Edition*, McGraw-Hill Education, 2018.

# Instalacja `Shodan CLI`
Wymaga: `Python` oraz pakiet `setuptools`
```console
root@kali:~$ easy_install shodan
root@kali:~$ shodan init <your API key>
root@kali:~$ shodan info
```

# Wyszukiwanie za pomocą `Shodan CLI`
## Publicznie otwarte serwisy VNC (wykorzystujące protokól RFB)
```console
root@kali:~$ shodan search --fields ip_str,port,org,hostnames RFB
```

# API Shodana w skryptach `Python`
## Instalacja wymaganych pakietów
```console
root@kali:~$ pip install shodan
root@kali:~$ pip install paho-mqtt
```
## Wyszukiwanie dostępnych brokerów MQTT
```console
root@kali:~$ python shodan_search_mqtt.py
```

## Próba subskrypcji do znalezionych brokerów
```console
root@kali:~$ python mqtt-scan.py
```
