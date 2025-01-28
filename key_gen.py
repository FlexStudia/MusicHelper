# coding: utf-8
from tools.tools import twelve_down, from_list_of_numbers_to_letters

MAJOR = [0, 4, 7]
MINOR = [0, 3, 7]
DIMED = [0, 3, 6]

# constants
KEYS_INTERVALS = {
    "Major": {  # Ionian
        "intervals": [0, 2, 4, 5, 7, 9, 11],
        "chord": {
            "I": MAJOR,
            "ii": MINOR,
            "iii": MINOR,
            "IV": MAJOR,
            "V": MAJOR,
            "vi": MINOR,
            "vii_d": DIMED,
        },
        "emotions": "joy, energy, light",
        "utilization": "most pop music and hymns",
    },
    "Dorian": {
        "intervals": [0, 2, 3, 5, 7, 9, 10],
        "chord": {
            "i": MINOR,
            "ii": MINOR,
            "III": MAJOR,
            "IV": MAJOR,
            "v": MINOR,
            "vi_d": DIMED,
            "VII": MAJOR,
        },
        "emotions": "minor sound with optimism and strength",
        "utilization": "often used for heroic or tranquil motifs",
    },
    "Phrygian": {
        "intervals": [0, 1, 3, 5, 7, 8, 10],
        "chord": {
            "i": MINOR,
            "II": MAJOR,
            "III": MAJOR,
            "iv": MINOR,
            "v_d": DIMED,
            "VI": MAJOR,
            "vii": MINOR,
        },
        "emotions": "darkness, suspense, mystery",
        "utilization": "adds exoticism and drama",
    },
    "Lydian": {
        "intervals": [0, 2, 4, 6, 7, 9, 11],
        "chord": {
            "I": MAJOR,
            "II": MAJOR,
            "iii": MINOR,
            "iv_d": DIMED,
            "V": MAJOR,
            "vi": MINOR,
            "vii": MINOR,
        },
        "emotions": "airiness, fantasy, luminous wonder",
        "utilization": "movie music, especially in the fantasy genre",
    },
    "Mixolydian": {
        "intervals": [0, 2, 4, 5, 7, 9, 10],
        "chord": {
            "I": MAJOR,
            "ii": MINOR,
            "iii_d": DIMED,
            "IV": MAJOR,
            "v": MINOR,
            "vi": MINOR,
            "VII": MAJOR,
        },
        "emotions": "calm, complacent, but not overly bright",
        "utilization": "blues, rock, folk",
    },
    "Minor": {  # Aeolian
        "intervals": [0, 2, 3, 5, 7, 8, 10],
        "chord": {
            "i": MINOR,
            "ii_d": DIMED,
            "III": MAJOR,
            "iv": MINOR,
            "v": MINOR,
            "VI": MAJOR,
            "VII": MAJOR,
        },
        "emotions": "melancholy, sadness, lyricism",
        "utilization": "traditional minor key in classical and pop music",
    },
    "Locrian": {
        "intervals": [0, 1, 3, 5, 6, 8, 10],
        "chord": {
            "i_d": DIMED,
            "II": MAJOR,
            "iii": MINOR,
            "iv": MINOR,
            "V": MAJOR,
            "VI": MAJOR,
            "vii": MINOR,
        },
        "emotions": "anxiety, instability, tension",
        "utilization": "perfect for avant-garde ideas",
    },
}
FROM_LETTER_TO_NUMBER = {"C": 0, "C#": 1, "D": 2, "D#": 3, "E": 4, "F": 5, "F#": 6, "G": 7, "G#": 8, "A": 9, "A#": 10, "B": 11}


class NotesAndChordsForKey:
    def __init__(self, key_name="", root_note=""):
        """
            key_name: str, root note of the key
                Can be "Major", "Minor", "Dorian", "Phrygian", "Lydian", "Mixolydian", "Locrian"
            root_note: str, root note of the key
                Can be "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"
        """
        self.key_name = key_name
        self.root_note = -1
        if self.key_name != "":
            self.root_note = FROM_LETTER_TO_NUMBER[root_note]  # it's a number, not a letter!
        self.key_notes_tones = []
        self.key_notes_letters = []
        self.key_chords = dict()
        self.key_chords["chords"] = dict()

    def get_notes_and_chords(self):
        if self.key_name != "" and self.root_note != "":
            self.get_notes()
            self.get_chords()

    def get_notes(self):
        if self.key_name != "" and self.root_note != "":
            self.key_notes_tones = [tone + self.root_note for tone in KEYS_INTERVALS[self.key_name]["intervals"]]
            tones_pushed_down = twelve_down(self.key_notes_tones)
            self.key_notes_letters = from_list_of_numbers_to_letters(tones_pushed_down)

    def get_chords(self):
        # run get_notes before this one
        if self.key_notes_tones:
            for index, accord_type in enumerate(KEYS_INTERVALS[self.key_name]["chord"].keys()):
                accord_note_tone = [self.key_notes_tones[index] + interval_value for interval_value in KEYS_INTERVALS[self.key_name]["chord"][accord_type]]
                tones_pushed_down = twelve_down(accord_note_tone)
                self.key_chords["chords"][accord_type] = from_list_of_numbers_to_letters(tones_pushed_down)


class GenerateAllKeys:
    def __init__(self):
        self.generate_and_save_all_keys()

    def generate_and_save_all_keys(self):
        self.save_all_keys(self.generate_all_keys())

    def generate_all_keys(self):
        all_keys = dict()
        for key_name in KEYS_INTERVALS.keys():
            all_keys[key_name] = dict()
            for root_note in FROM_LETTER_TO_NUMBER.keys():
                all_keys[key_name][root_note] = dict()
                my_CoreKeyToNotesAndChords = NotesAndChordsForKey(key_name, root_note)
                my_CoreKeyToNotesAndChords.get_notes_and_chords()
                all_keys[key_name][root_note]["notes"] = my_CoreKeyToNotesAndChords.key_notes_letters  # it's a list
                all_keys[key_name][root_note]["chords"] = my_CoreKeyToNotesAndChords.key_chords['chords']  # it's a dict with keys for chords type and values for corresponding notes
        return all_keys

    def save_all_keys(self, all_keys_dict):
        file_name = "all_keys.py"
        with open(file_name, "w") as f:
            f.write("all_keys = ")
            f.write(str(all_keys_dict))



def demo_f():
    # get notes and chords in a given key
    print("Notes and chords in a given key:")
    # C Major
    print("C Major")
    my_class_instance = NotesAndChordsForKey("Major", "C")
    my_class_instance.get_notes_and_chords()
    print(f"notes: {my_class_instance.key_notes_letters}")
    print(f"notes: {my_class_instance.key_chords['chords']}")
    # D Minor
    print("D Minor")
    my_class_instance = NotesAndChordsForKey("Minor", "D")
    my_class_instance.get_notes_and_chords()
    print(f"notes: {my_class_instance.key_notes_letters}")
    print(f"notes: {my_class_instance.key_chords['chords']}")
    # F# Mixolydian
    print("F# Lydian")
    my_class_instance = NotesAndChordsForKey("Lydian", "F#")
    my_class_instance.get_notes_and_chords()
    print(f"notes: {my_class_instance.key_notes_letters}")
    print(f"notes: {my_class_instance.key_chords['chords']}")


# demo_f()


# my_class_instance = GenerateAllKeys()
