"""
Guitar Class
"""
from guitar_string import GuitarString


class Guitar:
    def __init__(self, tuning=None):
        default_tuning = ['E1', 'A1', 'D2', 'G2', 'B2', 'E3']
        if tuning is None:
            tuning = default_tuning

        self.tuning = tuning
        self.strings = []
        for i in range(6):
            string = GuitarString(6 - i, tuning[5 - i])
            self.strings.append(string)

    def play(self, seq, t, notes):
        """
        play a set of notes from string 6 through string 1
        """
        for i in range(6):
            string_idx = 5 - i
            if notes[i] is not None:
                self.strings[string_idx].play(seq, t, notes[i], 75)

    def mute(self, seq, t):
        for string in self.strings:
            string.mute(seq)

