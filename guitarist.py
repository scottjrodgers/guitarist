"""
Main Guitarist program

1) Read a .tab file
2) Initialize the guitar
3) Initialize the note sequencer
4) Play the tab into the sequencer
5) Initialize MIDI
6) Play the notes
"""

from guitar import Guitar
from sequencer import Sequencer
from song_objects import *


def read_tab(fname):
    tuning = None
    tab = None
    with open(fname, "r") as f:
        for line in f:
            stripped_line = line.strip()
            if stripped_line.startswith("TUNING:"):
                tokens = stripped_line.split(':')
                string_tunings = tokens[1].strip().split(" ")
                tuning = list()
                for note in string_tunings:
                    note = note.strip()
                    if len(note) > 0:
                        tuning.append(note)
                        assert len(tuning) <= 6

            if stripped_line.startswith(",") or stripped_line.startswith("."):
                tab = list()
                tab.append(line)
            if line.startswith("|"):
                tab.append(line)
            if stripped_line.startswith("u") or stripped_line.startswith("d"):
                if len(tab) > 0:
                    tab.append(line)
    return tab, tuning


def play_tab(fname):
    """
    """
    tab, tuning = read_tab(fname)
    print(tuning)
    for row in tab:
        row = row[0:-1]
        print(row)

    guitar = Guitar(tuning)
    seq = Sequencer()

    # First pass version
    t = 0.0
    for idx, ch in enumerate(tab[0]):
        if ch in [',', '.']:
            notes = []
            for string in [6, 5, 4, 3, 2, 1]:
                fret = ""
                x = idx
                while tab[string][x].isdigit():
                    fret = tab[string][x] + fret
                    x -= 1

                if len(fret) == 0:
                    fret = None
                else:
                    fret = int(fret)

                notes.append(fret)

            guitar.play(seq, t, notes)
            if ch == ',':
                t += 0.25
            else:
                t += 0.19
    seq.play()


if __name__ == "__main__":
    play_tab("tab/sample.tab")
