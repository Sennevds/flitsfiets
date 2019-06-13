# Capture speeddata with Raspberry Pi and OPS-241A radar(WIP)

Deze code is gebasseerd op de code van [@Aliekens]( https://github.com/aliekens/flitsfiets ) maar aangepast om op een RPI(of ander linux systeem) te draaien!
We verbinden de radar via usb op de RPI en niet via de headers!

# Requirements

| Component |
| ------------- | 
| [OPS-241A radar](https://www.mouser.be/ProductDetail/203-OPS241ACWRP) |
| RPI(Bijna eender welke versie kan alleen wifi nodig voor het posten van de data) |
| Raspbian(ik gebruik de lite versie) |
| Een MySQL Database |

# Install

Ik ga er vanuit dat je een basis kennis hebt hoe je de RPI moet installeren(SD-kaart prepareren, enablen van SSH etc). Weet je niet hoe je dit moet doen denk ik dat het best is dat je eerst een aantal tutorials volgt over de basissetup van RPI en Linux
* Disable Linux gebruik van de serial interface:
 * sudo raspi-config
 * Selecteer optie 5(Interfacing options)
 * Optie 6 (Serial)
 * No (Zorgt er voor dat de linux console niet meer op de serial output)
 * Yes
* Sluit de radar via usb aan op de rpi
* reboot
* clone deze code op je rpi(git clone https://github.com/Sennevds/flitsfiets.git)
* cd flitsfiets\src
* pip install --user --requirement requirements.txt
* nano config_template.py  (of je eigen keuze van editor)
* Vul de gegevens in van je MySQL database
* python radar.py

# WIP
Ik probeer de komende weken de code en readme nog uit te breiden. Dit is een voorlopige eerste versie!
Oorspronkelijke code van Anthony Liekens is te vinden op zijn GitHub account [@Aliekens/flitfiets]( https://github.com/aliekens/flitsfiets )