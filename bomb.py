from buttonsequence import ButtonSequence
from contactserver import diffuse_bomb, send_strike
from sounds import play_strike, play_explosion, play_diffuse_sound

wires = {1:'red', 2:'blue', 3:'green'}
wire_to_cut = 'blue'
buttonSequence = ButtonSequence(wires, wire_cut, history_size=1)

def wire_cut(wire):
    if wire == wire_to_cut:
        diffuse_bomb()
        play_diffuse_sound()
    else:
        obj = send_strike()
        if obj['dead']:
            play_explosion()
        else:
            play_strike()
