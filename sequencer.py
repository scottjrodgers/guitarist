"""
Simple MIDI sequencer
"""

import rtmidi
from time import sleep, perf_counter


class Sequencer:
    def __init__(self, debug=False):
        self.midi = rtmidi.MidiOut()
        if debug:
            available_ports = self.midi.get_ports()
            print(available_ports)
        self.midi.open_port(1)

        self.event_list = list()

    def note_on(self, t, channel, note, velocity):
        self.event_list.append((t, (0x90 + channel, note, velocity)))

    def note_off(self, t, channel, note):
        self.event_list.append((t, (0x80 + channel, note)))

    def play(self):
        # sort our events list based on the time
        events = sorted(self.event_list, key=lambda e: e[0])
        print("Playing MIDI...")

        # initialize our sequencer
        base = perf_counter()
        for t, msg in events:
            now = perf_counter() - base
            if now < t:
                sleep(t - now)
            self.midi.send_message(msg)

        print("Done.")




