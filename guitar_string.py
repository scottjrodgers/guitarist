"""
A class for a midi guitar string
"""


class GuitarString:
    def __init__(self, string_num, tuning=None):
        # init base variables
        self.string_num = string_num
        self.channel = string_num
        self.volume = 108
        self.last_fret = None
        self.last_velocity = 0

        # determine base_note from tuning
        default_tuning = ["E3", "B2", "G2", "D2", "A1", "E1"]
        if tuning is None:
            tuning = default_tuning[string_num - 1]
        self.tuning = tuning

        scale = {'C': 0, 'C#': 1, 'Db': 1, 'D': 2, 'D#': 3, 'Eb': 3, 'E': 4, 'F': 5, 'F#': 6,
                 'Gb': 6, 'G': 7, 'G#': 8, 'Ab': 8, 'A': 9, 'Bb': 10, 'B': 11}

        note = tuning[0:-1]
        octave = tuning[-1]

        if note not in scale or octave.isdigit() is False:
            print("Couldn't understand tuing: '{}' for string: {}".format(tuning, string_num))
            raise ValueError(tuning)

        octave = int(octave)
        self.base_note = 12 + 12 * octave + scale[note] + 2  # note, Hack: shifting up a whole tone to match my guitar.

        print("tuning: {} note: {} octave: {} -> base note of: {}".format(tuning, note, octave, self.base_note))

    def play(self, seq, t, fret, velocity):
        """
        Pluck the string with finger at the given fret.  Velocity gives the strength of the pluck
        """
        if self.last_fret is not None:
            seq.note_off(t, self.channel, self.base_note + self.last_fret)
        seq.note_on(t, self.channel, self.base_note + fret, velocity)
        self.last_fret = fret

    def mute(self, seq, t):
        """
        Stop the current ringing note for this string.
        """
        if self.last_fret is not None:
            seq.note_off(t, self.channel, self.base_note + self.last_fret)

    def pull_off(self, fret):
        """
        Do a pull-off to the given fret
        """
        pass

    def hammer_on(self, fret):
        """
        Do a hammer-on to the given fret
        """
        pass

    def slide(self, fret):
        """
        Slide finger to new fret
        """
        pass


if __name__ == "__main__":
    g = GuitarString(1)
    g = GuitarString(6, "C1")
    g = GuitarString(2, 'Bb2')
    # g = GuitarString(4, "A#1")
    # g = GuitarString(5, "C")
