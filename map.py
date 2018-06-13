from buttonsequence import ButtonSequence
from contactserver import send_strike
from sounds import play_text, play_correct_sound, play_strike
from servo import release_servo

cities = {1:'vancouver', 2:'nyc', 3:'alaska'}
city_sequence = ['vancouver', 'nyc', 'alaska']
buttonSequence = ButtonSequence(cities, city_pressed, history_size=3)
servo_pin = 10

i=0

def city_pressed(city, history):
    if city == city_sequence[i]:
        i += 1
        play_correct_sound()
        play_text(city)
    else:
        i = 0
        play_strike()
        play_text(city + " was wrong")
        send_strike()
    if i == len(city_sequence):
        play_success()
        release_servo(servo_pin)
        i=0
