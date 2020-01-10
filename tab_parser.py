"""
Parser for Guitar Tab

Requirements:
    1. Must have at least one blank row (no non-whitespace) between phrases
    2. SECTION: no blank lines between SECTION header and the phrase
    3. Notation lines must start with "|" or "||"
"""

from song_objects import *


class TabParser:
    def __init__(self):
        # Init variables
        self.song = Song()
        self.section = None

        # Init symbol keys
        self.hammer_on = 'h'
        self.pull_off = 'p'
        self.slide_up = '/'
        self.slide_down = '\\'
        self.strum_up = 'u'
        self.strum_down = 'd'
        self.strong_beat = ','
        self.off_beat = '.'
        self.triplet = 't'
        self.bar = '|'
        self.thumb_over = 'T'

    @staticmethod
    def cross_section(tab, i):
        section = []
        for row in tab:
            if i < len(row):
                section.append(row[i])
            else:
                section.append(' ')
        return section

    @staticmethod
    def is_numbers(strings):
        num_digits = 0
        for ch in strings:
            if ch.isdigit():
                num_digits += 1
            elif ch != '-':
                return False
        return num_digits > 0

    def tokenize_strings(self, strings):
        if strings == ['|','|','|','|','|','|']:
            return "bar"
        elif strings == ['-','-','*','*','-','-']:
            return "dots"
        elif strings == ['-','-','-','-','-','-']:
            return "gap"
        elif self.is_numbers(strings):
            return "numbers"
        else:
            return "unknown"

    def handle_phrase(self, tab):
        # walk through the tab one column at a time
        # figure out which rows are strings, and which rows are which strings
        # recognize paterns in the set of characters in a vertical cross section of the tab

        # Understand rows above and below the strings
        section = self.cross_section(tab, 0)
        rows_above = 0
        rows_below = 0
        found_strings = False
        for ch in section:
            if ch != "|":
                if not found_strings:
                    rows_above += 1
                else:
                    rows_below += 1
            else:
                found_strings = True

        # tokenize the cross-sections
        sections = list()
        for i in range(max([len(x) for x in tab])):
            section = self.cross_section(tab, i)
            strings = section[rows_above:(len(tab) - rows_below)]

            token = self.tokenize_strings(strings)
            sections.append([token, strings, section])
            # if token == 'unknown':
            #     token = '*** UNKNOWN ***-------------------------------------------'
            # print("{} - {}".format(strings, token))

    def parse(self, fname):
        with open(fname, "r") as f:
            tab_phrase = None
            for line in f:
                line = line.replace('\n', '')
                stripped_line = line.strip()
                colon_idx = stripped_line.find(":")
                if colon_idx > 0:
                    key = stripped_line[0:colon_idx].strip()
                    value = stripped_line[(colon_idx + 1):].strip()

                    if key == 'SONG':
                        self.song.title = value
                    elif key == 'BY':
                        self.song.by = value
                    elif key == 'TUNING':
                        value = value.replace("[", "").replace("]", "")
                        toks = value.split(' ')
                        tuning = list()
                        for tok in toks:
                            if len(tok) > 0:
                                tuning.append(tok)
                        self.song.tuning = tuning
                    elif key == 'TIMSIG':
                        print("TODO: parse time signature from '{}'".format(value))
                        pass
                    elif key == 'hammer-on':
                        assert len(value) == 1
                        self.hammer_on = value
                    elif key == 'pull-off':
                        assert len(value) == 1
                        self.pull_off = value
                    elif key == 'slide-down':
                        assert len(value) == 1
                        self.slide_down = value
                    elif key == 'slide-up':
                        assert len(value) == 1
                        self.slide_up = value
                    elif key == 'strum-down':
                        assert len(value) == 1
                        self.strum_down = value
                    elif key == 'strum-up':
                        assert len(value) == 1
                        self.strum_up = value
                    elif key == 'strong-beat':
                        assert len(value) == 1
                        self.strong_beat = value
                    elif key == 'off-beat':
                        assert len(value) == 1
                        self.off_beat = value
                    elif key == 'triplet':
                        assert len(value) == 1
                        self.triplet = value
                    elif key == 'SECTION':
                        self.section = Section(self.song, value)
                    elif key == 'REPEAT SECTION':
                        self.song.repeat_section(value)
                else:
                    if len(stripped_line) > 0:
                        first_char = stripped_line[0]
                        if first_char in (self.strong_beat, self.off_beat,
                                          self.bar, self.strum_up, self.strum_down):
                            if tab_phrase is None:
                                tab_phrase = list()
                            tab_phrase.append(line)
                        else:  # temporary
                            print("line: '{}' not recognized.".format(line))
                    else:
                        # blank line
                        if tab_phrase is not None:
                            self.handle_phrase(tab_phrase)
                            tab_phrase = None


if __name__ == "__main__":
    tp = TabParser()
    tp.parse("tab/sample.tab")
