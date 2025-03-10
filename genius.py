from pico_i2c_lcd import I2cLcd
from machine import I2C, Pin
from picozero import Speaker
from time import sleep
from random import randint, choice
from utime import ticks_ms


# --------------------- Gameplay Function ---------------------- #
def get_press(dark):
    timer = ticks_ms()
    while ticks_ms() - timer < 5000:
        if not botton[0].value():
            if not dark:
                led[0].value(1)
            speaker.play(song[0],0.2)
            led[0].value(0)
            while not botton[0].value():
                pass
            return 0
        if not botton[1].value():
            if not dark:
                led[1].value(1)
            speaker.play(song[1],0.2)
            led[1].value(0)
            while not botton[1].value():
                pass
            return 1
        if not botton[2].value():
            if not dark:
                led[2].value(1)
            speaker.play(song[2],0.2)
            led[2].value(0)
            while not botton[2].value():
                pass
            return 2
        if not botton[3].value():
            if not dark:
                led[3].value(1)
            speaker.play(song[3],0.2)
            led[3].value(0)
            while not botton[3].value():
                pass
            return 3
    else:
        return -1

# ----------------------------------------------------------------- #

# ------------ Led Init Functions ----------- #

def animation_1():
    for i in range(2):
        led[i].value(1)
        sleep(0.08)
        led[i].value(0)
        led[i+2].value(1)
        sleep(0.09)
        led[i+2].value(0)

def animation_2():
    for i in range(4):
        led[i].value(1)
        speaker.play(song[i],0.5)
        led[i].value(0)
        sleep(0.3)

# ------------------------------------------ #

# ----------------------------- Display LCD Functions --------------------------------#
def difficulty():
    lcd.clear()
    lcd.putstr('Difficulty:         ')
    lcd.putstr('-Easy Green         ')
    lcd.putstr('-Medium Yellow      ')
    lcd.putstr('-Hard Red           ')
    while True:
        if not botton[0].value():
            time = ticks_ms()
            first = True
            while not botton[0].value():
                if first and ticks_ms() - time > 4000:
                    first = False
                    lcd.clear()
                    lcd.move_to(0,1)
                    lcd.putstr('      Opening...    ')
                    sleep(0.5)
                    upp()
                    sleep(0.6)
                    static()
                    lcd.clear()
                    lcd.move_to(0,1)
                    lcd.putstr('        Open        ')
            if first:
                lcd.clear()
                lcd.putstr('---- Easy Mode -----')
                lcd.move_to(0,2)
                lcd.putstr('      Score: ')
                return 1
            else:
                while botton[2].value():
                    pass
                else:
                    lcd.clear()
                    lcd.move_to(0,1)
                    lcd.putstr('      Closing...    ')
                    sleep(1)
                    down()
                    sleep(0.3)
                    lcd.clear()
                    lcd.putstr('Difficulty:         ')
                    lcd.putstr('-Easy Green         ')
                    lcd.putstr('-Medium Yellow      ')
                    lcd.putstr('-Hard Red           ')

        elif not botton[1].value():
            lcd.clear()
            lcd.putstr('--- Medium Mode ----')
            lcd.move_to(0,2)
            lcd.putstr('      Score: ')
            return 2
        elif not botton[2].value():
            lcd.clear()
            lcd.putstr('---- Hard Mode -----')
            lcd.move_to(0,2)
            lcd.putstr('      Score: ')
            return 3
        elif not botton[3].value():
            time = ticks_ms()
            while not botton[3].value():
                if ticks_ms() - time > 2000:
                    lcd.backlight_off()
            if ticks_ms() - time > 2000:
                animation_2()
                animation_2()
                lcd.clear()
                sleep(0.5)
                lcd.backlight_on()
                lcd.putstr('--- Secret Mode ----')
                lcd.move_to(0,2)
                lcd.putstr('      Score: ')
                return 4

def slide():
    global i, j, right, up
    if right:
        if j < 14:
            j+=1
        else:
            right = False
    if not right:
        if j > 0:
            j-=1
        else:
            right = True
            j+=1
    if up:
        if i < 3:
            i+=1
        else:
            up = False
    if not up:
        if i > 0:
            i-=1
        else:
            up = True
            i+=1

# ----------------------------------------------------------------------------------- #

# -------------------------------- Level Functions ---------------------------------- #
def easy(dark):
    select = -1
    game = True
    lost = False
    while game:
        sequence.append(randint(0, 3))
        lcd.move_to(12,2)
        lcd.putstr(f'{len(sequence)-1}')
        sleep(1)
        for i in sequence:
            led[i].value(1)
            speaker.play(song[i], 0.4)
            led[i].value(0)
            sleep(0.4)
        for collor in sequence:
            if game == True:
                select = get_press(dark)
            if select == collor:
                select = -1
            else:
                game = False
                lost = True
        if len(sequence) == 10:
            game = False
    if lost == False:
        led_hard.toggle()
        sleep(0.1)
        win_1()
    else:
        lost_display()

def medium(dark):
    select = -1
    game = True
    lost = False
    while game:
        sequence.append(randint(0, 3))
        lcd.move_to(12,2)
        lcd.putstr(f'{len(sequence)-1}')
        sleep(1)
        for i in sequence:
            led[i].value(1)
            speaker.play(song[i], 0.23)
            led[i].value(0)
            sleep(0.23)
        for collor in sequence:
            if game == True:
                select = get_press(dark)
            if select == collor:
                select = -1
            else:
                game = False
                lost = True
        if len(sequence) == 15:
            game = False
    if lost == False:
        led_hard.toggle()
        sleep(0.1)
        win_2()
    else:
        lost_display()

def hard(dark):
    select = -1
    game = True
    lost = False
    while game:
        sequence.append(randint(0, 3))
        time = (((2.71828182845904523536028747135266249)**(-len(sequence)/36))-0.2)/2
        lcd.move_to(12,2)
        lcd.putstr(f'{len(sequence)-1}')
        sleep(1)
        for i in sequence:
            led[i].value(1)
            speaker.play(song[i], time)
            led[i].value(0)
            sleep(time)
        for collor in sequence:
            if game == True:
                select = get_press(dark)
            if select == collor:
                select = -1
            else:
                game = False
                lost = True
        if len(sequence) == 20:
            game = False
    if lost == False:
        led_hard.toggle()
        sleep(0.1)
        win_3()
    else:
        lost_display()

def secret(dark):
    select = -1
    game = True
    lost = False
    while game:
        sequence.append(randint(0, 3))
        lcd.move_to(12,2)
        lcd.putstr(f'{len(sequence)-1}')
        sleep(1)
        for i in sequence:
            speaker.play(song[i], 0.25)
            sleep(0.25)
        for collor in sequence:
            if game == True:
                select = get_press(dark)
            if select == collor:
                select = -1
            else:
                game = False
                lost = True
        if len(sequence) == 15:
            game = False
    if lost == False:
        led_hard.toggle()
        sleep(0.1)
        win_4()
    else:
        lost_display()

# ----------------------------------------------------------------------------------#

# ---------- musical functions ----------#

def win_1():
    lcd.clear()
    lcd.move_to(0,1)
    lcd.putstr("      You Win       ")
    for note in win1_notes:
        speaker.play(note,0.4)
    lcd.clear()

def win_2():
    lcd.clear()
    lcd.move_to(0,1)
    lcd.putstr("      You Win       ")
    upp()
    for note in win2_notes:
        speaker.play(note,0.2)
        if win2_notes.index(note) == 2:
            static()
    down()
    sleep(0.3)
    static()
    lcd.clear()

def win_3():
    lcd.clear()
    lcd.move_to(0,1)
    lcd.putstr("      You Win       ")
    upp()
    for note in win3_notes:
        speaker.play(note,0.3)
        if win3_notes.index(note) == 1:
            static()
    down()
    sleep(0.3)
    static()
    lcd.clear()

def win_4():
    lcd.clear()
    lcd.move_to(0,1)
    lcd.putstr("      You Win       ")
    for note in win4_notes:
        speaker.play(note,0.25)
    lcd.clear()

def lost_display():
    lcd.clear()
    lcd.move_to(0,1)
    lcd.putstr("      You lost      ")
    speaker.play(300, 0.3)
    sleep(0.2)
    speaker.play(300, 0.3)
    sleep(0.2)
    lcd.clear()

def init():
    num = randint(0, 1)
    for note in init_notes[num]:
        speaker.play(note, 0.25)

def easy_song():
    for note in easy_notes:
        speaker.play(note, 0.24)

def medium_song():
    for note in medium_notes:
        speaker.play(note, 0.2)

def hard_song():
    for note in hard_notes:
        speaker.play(note,0.3)

def secret_song():
    for note in secret_notes:
        speaker.play(note,0.2)

def menu_song():
    for note in menu_notes:
        speaker.play(note,0.25)

# --------------------------------------- #

# --------------- Box Functions ------------------ #
def upp():
    pin_open.value(1)
    pin_close.value(0)

def down():
    pin_open.value(0)
    pin_close.value(1)

def static():
    pin_close.value(0)
    pin_open.value(0)
    
# ------------------------------------------------ #

# ----------------- Initial Attributions --------------- #
i2c = I2C(id=1,scl=Pin(27),sda=Pin(26),freq=100000)
lcd = I2cLcd(i2c, 0x27, 4, 20) # LCD 16x2
pin_open = Pin(7, Pin.OUT, value = 0)
pin_close = Pin(8, Pin.OUT, value = 1)
botton = [Pin(10, Pin.IN, Pin.PULL_UP), Pin(11, Pin.IN, Pin.PULL_UP), Pin(12, Pin.IN, Pin.PULL_UP), Pin(13, Pin.IN, Pin.PULL_UP)]
led = [Pin(21, Pin.OUT,value = 0), Pin(20, Pin.OUT, value = 0), Pin(19, Pin.OUT, value = 0), Pin(18, Pin.OUT, value = 0)]
led_hard = Pin(5, Pin.OUT, value = 0)

# --------------------------------------------------------#

# ---------------------- Songs ----------------------------- #
song = ['f5','g5', 'a5', 'c6']

win2_notes = ['f#5', 'f#5','d5', 'b4', 0, 'b4', 0, 'e5',
            0, 'e5', 0, 'e5', 'g#5', 'g#5', 'a5', 'b5',
            'a5', 'a5', 'a5', 'e5', 0, 'd5', 0, 'f#5',
            0, 'f#5', 0, 'f#5', 'e5', 'e5', 'f#5', 'e5',
            'f#5', 'f#5', 'd5', 'b4', 0, 'b4', 0, 'e5']

win1_notes = ['e4', 'e4', 'f4', 'g4', 'g4', 'f4', 'e4', 'd4',
              'c4', 'c4', 'd4', 'e4','e4', 'd4', 'd4', 'e4',
              'e4', 'f4', 'g4', 'g4', 'f4', 'e4', 'd4','c4',
              'c4', 'd4', 'e4', 'd4', 'c4', 'c4',]

win3_notes = ['g4', 'a4', 'b4', 'd5', 'd5', 'b4', 'c5', 'c5', 'g4', 'a4',
              'b4', 'd5', 'd5', 'c5', 'b4', 0, 'g4', 'g4', 'a4', 'b4',
              'd5', 0, 'd5', 'c5', 'b4', 'g4', 'c5', 0, 'c5', 'b4', 'a4',
              'a4', 'b4', 0, 'b4', 'a4', 'g4', 'g4', 0]

win4_notes = ['b5', 'd6', 'b5',
  'f#5', 'b5','f#5', 'd5', 'f#5', 'd5',
  'b4','f4', 'b4', 'd5', 'b4',
  'c#5', 'b4', 'c#5', 'b4','a#4', 'c#5', 'e5','c#5',
  'd5','b4','b5', 'd6', 'b5',
  'f#5', 'b5','f#5','d5', 'f#5', 'd5', 'b4','d5', 'c#5', 'd5',
  'd5', 'c#5', 'd5', 'b5', 'd5',
  'd5', 'c#5', 'f#5',  'f5', 'f#5',
  'f#5', 'f5', 'f#5', 'd6', 'f#5']

init_notes = [[0, 0, 0, 'd#4', 'e4', 0, 'f#4', 'g4', 0, 'd#4',
              'e4', 'f#4', 'g4', 'c5', 'b4', 'e4', 'g4', 'b4',
              'a#4', 'a4', 'g4', 'e4', 'd4', 'e4', 0, 0],
              ['e5', 'b4', 'c5', 'd5', 'c5', 'b4','a4', 'a4',
               'c5', 'e5', 'd5', 'c5',
              'b4', 'c5', 'd5', 'e5',
              'c5', 'a4', 'a4', 'a4']]

sw_notes = ['a#4', 'a#4', 'a#4', 'f5', 'c6','a#5', 'a5',
            'g5', 'f6', 'c6','a#5', 'a5', 'g5','f6', 'c6',
            'a#5', 'a5', 'a#5', 'g5', 'c5','c5', 'c5',
            'f5', 'c6', 'a#5', 'a5', 'g5', 'f6', 'c6']

easy_notes = [0, 'd5', 'b4', 'd5', 'c#5', 'd5', 'c#5', 'a4', 0,
              0, 'a4', 'f#5', 'e5', 'd5','c#5', 'd5', 'c#5', 'a4']

medium_notes = ['g4', 'c4', 'd#4', 'f4', 'g4', 'c4', 'd#4',
                'f4','g4', 'c4', 'd#4', 'f4', 'g4', 'c4',
                'd#4', 'f4', 'g4', 'c4', 'e4', 'f4', 'g4']

hard_notes = ['e4', 'a4', 'c5', 'b4', 'a4', 'c5', 'a4', 'b4',
              'a4', 'f4', 'g4','e4', 'e4', 'a4', 'c5','b4',
              'a4', 'c5', 'a4', 'c5', 'a4', 'e4', 'd#4','d4']

secret_notes = [0, 'd4', 'd4' ,'g4', 'g4', 'a#4','a4', 'a4','g4',
                'g4', 'g4', 'd5','d5', 'c5', 'c5','c5', 'a4', 'a4', 'a4', 'g4', 'g4', 'a#4', 'a4','a4',
                'f4', 'f4', 'g#4', 'g#4','d4', 'd4','d4']

menu_notes = ['c6', 'g5', 'f6']

# ------------------------------------------------------- #

# ---------------- Init Game ---------------- #
speaker = Speaker(22)
lcd.move_to(0,1)
lcd.putstr('     Loading...     ')
init()
lcd.clear()
# ------------------------------------------- #

# ---- Variable Declarations ---- #
init = False
run = False
right = True
up = True
dark = False
change = False
sequence = []
selection = 0
i = 0
j = 0

# ------------------------------- #


# ------------------------- Main -------------------------- #
while True:
    if (not botton[0]() or not botton[1]() or not botton[2].value() or not botton[3].value()) and init == False:
        menu_song()
        selection = difficulty()
        sequence = []
        init = True
        if selection == 1:
            easy_song()
            easy(dark)
            init = False
            selection = 0
        elif selection == 2:
            medium_song()
            medium(dark)
            init = False
            selection = 0
        elif selection == 3:
            hard_song()
            hard(dark)
            init = False
            selection = 0
        elif selection == 4:
            secret_song()
            dark = True
            secret(dark)
            dark = False
            init = False
            selection = 0

    elif init == False:
        animation_1()
        lcd.clear()
        slide()
        lcd.move_to(j, i)
        lcd.putstr('Genius')

# --------------------------------------------------------- #
