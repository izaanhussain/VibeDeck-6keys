# VibeDeck-6keys

VibeDeck-6 keys is my 6-key macropad, built for Pixl
This is the smaller version of my vibedeck. I wanted to make something small, simple & compact. this is built around the Seeed XIAO RP2040 with 6 Cherry MX switches and the EC11 encoder.

<img width="746" height="360" alt="image" src="https://github.com/user-attachments/assets/ab71a0f8-8a05-45f2-8416-a83ec64216db" />

# Components 

1) Seeed Studio XIAO RP2040
2) 6 keys
3) 1x EC11 Rotary encoder
4) Sandwich-style Case
5) 4x M3 Bolts

# Case (CAD) 

Everything (the case and the plate) fits together using 4 M3 Bolts. Crimson-click has 2 separate pieces which are connected by these bolts. The keys are covered by the DSA keycaps.THis is made with fushion 360
 
<img width="744" height="363" alt="image" src="https://github.com/user-attachments/assets/bfad1c1c-2ddf-4d93-b502-e15ea440aa1b" />

<img width="746" height="360" alt="image" src="https://github.com/user-attachments/assets/ab71a0f8-8a05-45f2-8416-a83ec64216db" />

# PCB 

The PCB is made in KIcad

<img width="926" height="470" alt="image" src="https://github.com/user-attachments/assets/ba61888c-7d6a-43f1-b8b1-d49158881ac1" />

<img width="1033" height="583" alt="image" src="https://github.com/user-attachments/assets/927dd478-f83a-46ca-ab76-ecfcc25f7e99" />

<img width="972" height="547" alt="image" src="https://github.com/user-attachments/assets/7345d04f-afbf-4fc7-bc51-60b1e5c6b8fc" />

# Firmware Overview
 I used the KMK firmware with CircuitPython you can find the main.py in the firmware folder 
 current code has  
 1) The rotary encoder has functions of volume up and down; press to mute.
 2) The 6 keys have all different functions. (any key functions can be assigned by changing the code)

# BOM 
1) 6x Cherry MX switches
2) 6x DSA keycaps
3) 4x M3 Bolts
4) 1x XIAO RP2040
5) 1X EC11 Rotary Encoder
6) 1x Case
7) 1x USB Type-C cable

# Production
 The production files are in the "production" folder where you can find the gerbers.zip & POS file too
