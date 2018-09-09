"""
Collection of song data structures
TODO: Repeat-Start, Repeat-End flags
TODO: Populate "next" attributes
TODO: D.C. al Fine, D.S. al Fine, D.S. al Coda.  Multiple repeats (if thens essentially) -
TODO: Track times through a section for use in repeats
TODO: Track if a section is being played due to a D.S. or D.S. Jump

"""


class NotationEvent:
    """
    Base class for notation events
    """

    def __init__(self, beat, string_num):
        """
        set time, t
        init several variables to None
        """
        self.beat = beat
        self.string_num = string_num
        self.string = beat.measure.section.strings[string_num]
        self.prev = self.string.last_note()
        self.next = None

    def add_note(self, object):
        self.beat.notes[self.string_num] = object
        self.string.add_note(object)

    def exec(self):
        pass


class Pluck(NotationEvent):
    def __init__(self, beat, string_num, fret):
        super().__init__(beat, string_num)
        self.fret = fret
        self.add_note(self)


class Mute(NotationEvent):
    def __init__(self, beat, string_num):
        super().__init__(beat, string_num)
        self.add_note(self)


class Slide(NotationEvent):
    def __init__(self, beat, string_num, to_fret):
        self.to_fret = to_fret
        self.from_fret = None
        super().__init__(beat, string_num)
        self.add_note(self)


class PullOff(NotationEvent):
    def __init__(self, beat, string_num, to_fret):
        self.to_fret = to_fret
        super().__init__(beat, string_num)
        self.add_note(self)


class HammerOn(NotationEvent):
    def __init__(self, beat, string_num, to_fret):
        self.to_fret = to_fret
        super().__init__(beat, string_num)
        self.add_note(self)


class Beat:
    def __init__(self, measure, duration, strength=0.75):
        self.beat_num = None
        self.duration = duration
        self.measure = measure
        self.strength = strength
        self.notes = [None for i in range(7)]  # ignore zero and use strings 1 through 6
        measure.add_beat(self)


class Measure:
    def __init__(self, section):
        self.section = section
        self.prev = section.last_measure()
        self.next = None
        self.measure_number = section.add_measure(self)
        self.beats = list()
        self.current_beat = 0.0

    def add_beat(self, beat):
        beat.beat_num = self.current_beat
        self.current_beat += beat.duration
        self.beats.append(beat)


class NotationString:
    def __init__(self, section, string_num):
        self.section = section
        self.string_num = string_num
        self.notes = list()

    def last_note(self):
        n_notes = len(self.notes)
        if n_notes == 0:
            return None
        else:
            return self.notes[n_notes - 1]

    def add_note(self, note):
        self.notes.append(note)


class Section:
    def __init__(self, song, name):
        self.song = song
        self.name = name
        self.strings = [NotationString(self, i) for i in range(7)]  # ignore zero and use strings 1 through 6
        self.measures = list()

    def add_measure(self, measure):
        self.measures.append(measure)
        return len(self.measures) - 1

    def last_measure(self):
        n_meas = len(self.measures)
        if n_meas == 0:
            return None
        return self.measures[n_meas - 1]


class Song:
    def __init__(self, title=None, by=None, tuning=None):
        if tuning is None:
            tuning = ["E2", "A2", "D3", "G3", "B3", "E4"]
        self.title = title
        self.by = by
        self.tuning = tuning
        self.sections = dict()
        self.section_sequence = list()

    def add_section(self, section):
        self.sections[section.name] = section
        self.section_sequence.append(section.name)

    def repeat_section(self, section_name):
        assert section_name in self.sections
        self.section_sequence.append(section_name)


if __name__ == "__main__":
    # Test the heck out of these
    # song = Song()
    section = Section(None, "A1")
    measure = Measure(section)
    beat = Beat(measure, 0.5, strength=0.8)
    Pluck(beat, 1, 12)
    Pluck(beat, 2, 0)
    Pluck(beat, 6, 0)

    beat2 = Beat(measure, 0.5, strength=0.7)
    Pluck(beat2, 3, 12)

    beat3 = Beat(measure, 0.5, strength=0.8)
    Slide(beat3, 3, 10)

    pass