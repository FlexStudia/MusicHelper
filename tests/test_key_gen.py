# coding: utf-8
from key_gen import NotesAndChordsForKey
from all_keys import ALL_KEYS

def test_get_notes():
    # Major
    key = "Major"
    # C
    class_instance = NotesAndChordsForKey(key, "C")
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ["C", "D", "E", "F", "G", "A", "B"]
    # C#
    class_instance = NotesAndChordsForKey(key, "C#")
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ["C#", "D#", "F", "F#", "G#", "A#", "C"]
    # F
    class_instance = NotesAndChordsForKey(key, "F")
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ["F", "G", "A", "A#", "C", "D", "E"]
    # F#
    class_instance = NotesAndChordsForKey(key, "F#")
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ["F#", "G#", "A#", "B", "C#", "D#", "F"]
    # A#
    class_instance = NotesAndChordsForKey(key, "A#")
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ["A#", "C", "D", "D#", "F", "G", "A"]
    # B
    class_instance = NotesAndChordsForKey(key, "B")
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ["B", "C#", "D#", "E", "F#", "G#", "A#"]
    # Minor
    key = "Minor"
    # C
    class_instance = NotesAndChordsForKey(key, "C")
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ["C", "D", "D#", "F", "G", "G#", "A#"]
    # C#
    class_instance = NotesAndChordsForKey(key, "C#")
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ["C#", "D#", "E", "F#", "G#", "A", "B"]
    # F
    class_instance = NotesAndChordsForKey(key, "F")
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ['F', 'G', 'G#', 'A#', 'C', 'C#', 'D#']
    # F#
    class_instance = NotesAndChordsForKey(key, "F#")
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ['F#', 'G#', 'A', 'B', 'C#', 'D', 'E']
    # A#
    class_instance = NotesAndChordsForKey(key, "A#")
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ['A#', 'C', 'C#', 'D#', 'F', 'F#', 'G#']
    # B
    class_instance = NotesAndChordsForKey(key, "B")
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ['B', 'C#', 'D', 'E', 'F#', 'G', 'A']
    # Dorian
    key = "Dorian"
    # C
    class_instance = NotesAndChordsForKey(key, "C")
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ['C', 'D', 'D#', 'F', 'G', 'A', 'A#']
    # C#
    class_instance = NotesAndChordsForKey(key, "C#")
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ['C#', 'D#', 'E', 'F#', 'G#', 'A#', 'B']
    # F
    class_instance = NotesAndChordsForKey(key, "F")
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ['F', 'G', 'G#', 'A#', 'C', 'D', 'D#']
    # F#
    class_instance = NotesAndChordsForKey(key, "F#")
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ['F#', 'G#', 'A', 'B', 'C#', 'D#', 'E']
    # A#
    class_instance = NotesAndChordsForKey(key, "A#")
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ['A#', 'C', 'C#', 'D#', 'F', 'G', 'G#']
    # B
    class_instance = NotesAndChordsForKey(key, "B")
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ['B', 'C#', 'D', 'E', 'F#', 'G#', 'A']
    # Phrygian
    key = "Phrygian"
    # C
    class_instance = NotesAndChordsForKey(key, "C")
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ['C', 'C#', 'D#', 'F', 'G', 'G#', 'A#']
    # C#
    class_instance = NotesAndChordsForKey(key, "C#")
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ['C#', 'D', 'E', 'F#', 'G#', 'A', 'B']
    # F
    class_instance = NotesAndChordsForKey(key, "F")
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ['F', 'F#', 'G#', 'A#', 'C', 'C#', 'D#']
    # F#
    class_instance = NotesAndChordsForKey(key, "F#")
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ['F#', 'G', 'A', 'B', 'C#', 'D', 'E']
    # A#
    class_instance = NotesAndChordsForKey(key, "A#")
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ['A#', 'B', 'C#', 'D#', 'F', 'F#', 'G#']
    # B
    class_instance = NotesAndChordsForKey(key, "B")
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ['B', 'C', 'D', 'E', 'F#', 'G', 'A']
    # Lydian
    key = "Lydian"
    # C
    class_instance = NotesAndChordsForKey(key, "C")
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ['C', 'D', 'E', 'F#', 'G', 'A', 'B']
    # C#
    class_instance = NotesAndChordsForKey(key, "C#")
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ['C#', 'D#', 'F', 'G', 'G#', 'A#', 'C']
    # F
    class_instance = NotesAndChordsForKey(key, "F")
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ['F', 'G', 'A', 'B', 'C', 'D', 'E']
    # F#
    class_instance = NotesAndChordsForKey(key, "F#")
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ['F#', 'G#', 'A#', 'C', 'C#', 'D#', 'F']
    # A#
    class_instance = NotesAndChordsForKey(key, "A#")
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ['A#', 'C', 'D', 'E', 'F', 'G', 'A']
    # B
    class_instance = NotesAndChordsForKey(key, "B")
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ['B', 'C#', 'D#', 'F', 'F#', 'G#', 'A#']
    # Mixolydian
    key = "Mixolydian"
    # C
    class_instance = NotesAndChordsForKey(key, "C")
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ['C', 'D', 'E', 'F', 'G', 'A', 'A#']
    # C#
    class_instance = NotesAndChordsForKey(key, "C#")
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ['C#', 'D#', 'F', 'F#', 'G#', 'A#', 'B']
    # F
    class_instance = NotesAndChordsForKey(key, "F")
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ['F', 'G', 'A', 'A#', 'C', 'D', 'D#']
    # F#
    class_instance = NotesAndChordsForKey(key, "F#")
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ['F#', 'G#', 'A#', 'B', 'C#', 'D#', 'E']
    # A#
    class_instance = NotesAndChordsForKey(key, "A#")
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ['A#', 'C', 'D', 'D#', 'F', 'G', 'G#']
    # B
    class_instance = NotesAndChordsForKey(key, "B")
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ['B', 'C#', 'D#', 'E', 'F#', 'G#', 'A']
    # Locrian
    key = "Locrian"
    # C
    class_instance = NotesAndChordsForKey(key, "C")
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ['C', 'C#', 'D#', 'F', 'F#', 'G#', 'A#']
    # C#
    class_instance = NotesAndChordsForKey(key, "C#")
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ['C#', 'D', 'E', 'F#', 'G', 'A', 'B']
    # F
    class_instance = NotesAndChordsForKey(key, "F")
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ['F', 'F#', 'G#', 'A#', 'B', 'C#', 'D#']
    # F#
    class_instance = NotesAndChordsForKey(key, "F#")
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ['F#', 'G', 'A', 'B', 'C', 'D', 'E']
    # A#
    class_instance = NotesAndChordsForKey(key, "A#")
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ['A#', 'B', 'C#', 'D#', 'E', 'F#', 'G#']
    # B
    class_instance = NotesAndChordsForKey(key, "B")
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ['B', 'C', 'D', 'E', 'F', 'G', 'A']


def test_get_accords():
    # C Major
    key, root_note = "Major", "C"
    class_instance = NotesAndChordsForKey(key, root_note)
    class_instance.get_notes_and_chords()
    assert class_instance.key_chords["chords"]["I"] == ["C", "E", "G"]
    assert class_instance.key_chords["chords"]["ii"] == ["D", "F", "A"]
    assert class_instance.key_chords["chords"]["iii"] == ["E", "G", "B"]
    assert class_instance.key_chords["chords"]["IV"] == ["F", "A", "C"]
    assert class_instance.key_chords["chords"]["V"] == ["G", "B", "D"]
    assert class_instance.key_chords["chords"]["vi"] == ["A", "C", "E"]
    assert class_instance.key_chords["chords"]["vii_d"] == ["B", "D", "F"]
    # D Dorian
    key, root_note = "Dorian", "D"
    class_instance = NotesAndChordsForKey(key, root_note)
    class_instance.get_notes_and_chords()
    assert class_instance.key_chords["chords"]["i"] == ["D", "F", "A"]
    assert class_instance.key_chords["chords"]["ii"] == ["E", "G", "B"]
    assert class_instance.key_chords["chords"]["III"] == ["F", "A", "C"]
    assert class_instance.key_chords["chords"]["IV"] == ["G", "B", "D"]
    assert class_instance.key_chords["chords"]["v"] == ["A", "C", "E"]
    assert class_instance.key_chords["chords"]["vi_d"] == ["B", "D", "F"]
    assert class_instance.key_chords["chords"]["VII"] == ["C", "E", "G"]
    # E Phrygian
    key, root_note = "Phrygian", "E"
    class_instance = NotesAndChordsForKey(key, root_note)
    class_instance.get_notes_and_chords()
    assert class_instance.key_chords["chords"]["i"] == ["E", "G", "B"]
    assert class_instance.key_chords["chords"]["II"] == ["F", "A", "C"]
    assert class_instance.key_chords["chords"]["III"] == ["G", "B", "D"]
    assert class_instance.key_chords["chords"]["iv"] == ["A", "C", "E"]
    assert class_instance.key_chords["chords"]["v_d"] == ["B", "D", "F"]
    assert class_instance.key_chords["chords"]["VI"] == ["C", "E", "G"]
    assert class_instance.key_chords["chords"]["vii"] == ["D", "F", "A"]
    # F Lydian
    key, root_note = "Lydian", "F"
    class_instance = NotesAndChordsForKey(key, root_note)
    class_instance.get_notes_and_chords()
    assert class_instance.key_chords["chords"]["I"] == ["F", "A", "C"]
    assert class_instance.key_chords["chords"]["II"] == ["G", "B", "D"]
    assert class_instance.key_chords["chords"]["iii"] == ["A", "C", "E"]
    assert class_instance.key_chords["chords"]["iv_d"] == ["B", "D", "F"]
    assert class_instance.key_chords["chords"]["V"] == ["C", "E", "G"]
    assert class_instance.key_chords["chords"]["vi"] == ["D", "F", "A"]
    assert class_instance.key_chords["chords"]["vii"] == ["E", "G", "B"]
    # G Mixolydian
    key, root_note = "Mixolydian", "G"
    class_instance = NotesAndChordsForKey(key, root_note)
    class_instance.get_notes_and_chords()
    assert class_instance.key_chords["chords"]["I"] == ["G", "B", "D"]
    assert class_instance.key_chords["chords"]["ii"] == ["A", "C", "E"]
    assert class_instance.key_chords["chords"]["iii_d"] == ["B", "D", "F"]
    assert class_instance.key_chords["chords"]["IV"] == ["C", "E", "G"]
    assert class_instance.key_chords["chords"]["v"] == ["D", "F", "A"]
    assert class_instance.key_chords["chords"]["vi"] == ["E", "G", "B"]
    assert class_instance.key_chords["chords"]["VII"] == ["F", "A", "C"]
    # A Minor (Aeolian)
    key, root_note = "Minor", "A"
    class_instance = NotesAndChordsForKey(key, root_note)
    class_instance.get_notes_and_chords()
    assert class_instance.key_chords["chords"]["i"] == ["A", "C", "E"]
    assert class_instance.key_chords["chords"]["ii_d"] == ["B", "D", "F"]
    assert class_instance.key_chords["chords"]["III"] == ["C", "E", "G"]
    assert class_instance.key_chords["chords"]["iv"] == ["D", "F", "A"]
    assert class_instance.key_chords["chords"]["v"] == ["E", "G", "B"]
    assert class_instance.key_chords["chords"]["VI"] == ["F", "A", "C"]
    assert class_instance.key_chords["chords"]["VII"] == ["G", "B", "D"]
    # B Locrian
    key, root_note = "Locrian", "B"
    class_instance = NotesAndChordsForKey(key, root_note)
    class_instance.get_notes_and_chords()
    assert class_instance.key_chords["chords"]["i_d"] == ["B", "D", "F"]
    assert class_instance.key_chords["chords"]["II"] == ["C", "E", "G"]
    assert class_instance.key_chords["chords"]["iii"] == ["D", "F", "A"]
    assert class_instance.key_chords["chords"]["iv"] == ["E", "G", "B"]
    assert class_instance.key_chords["chords"]["V"] == ["F", "A", "C"]
    assert class_instance.key_chords["chords"]["VI"] == ["G", "B", "D"]
    assert class_instance.key_chords["chords"]["vii"] == ["A", "C", "E"]


def test_all_key_gen_match_notes():
    # Major
    key = "Major"
    # C
    key_note = "C"
    class_instance = NotesAndChordsForKey(key, key_note)
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ALL_KEYS[key][key_note]["notes"]
    # C#
    key_note = "C#"
    class_instance = NotesAndChordsForKey(key, key_note)
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ALL_KEYS[key][key_note]["notes"]
    # F
    key_note = "F"
    class_instance = NotesAndChordsForKey(key, key_note)
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ALL_KEYS[key][key_note]["notes"]
    # F#
    key_note = "F#"
    class_instance = NotesAndChordsForKey(key, key_note)
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ALL_KEYS[key][key_note]["notes"]
    # A#
    key_note = "A#"
    class_instance = NotesAndChordsForKey(key, key_note)
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ALL_KEYS[key][key_note]["notes"]
    # B
    key_note = "B"
    class_instance = NotesAndChordsForKey(key, key_note)
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ALL_KEYS[key][key_note]["notes"]
    # Minor
    key = "Minor"
    # C
    key_note = "C"
    class_instance = NotesAndChordsForKey(key, key_note)
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ALL_KEYS[key][key_note]["notes"]
    # C#
    key_note = "C#"
    class_instance = NotesAndChordsForKey(key, key_note)
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ALL_KEYS[key][key_note]["notes"]
    # F
    key_note = "F"
    class_instance = NotesAndChordsForKey(key, key_note)
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ALL_KEYS[key][key_note]["notes"]
    # F#
    key_note = "F#"
    class_instance = NotesAndChordsForKey(key, key_note)
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ALL_KEYS[key][key_note]["notes"]
    # A#
    key_note = "A#"
    class_instance = NotesAndChordsForKey(key, key_note)
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ALL_KEYS[key][key_note]["notes"]
    # B
    key_note = "B"
    class_instance = NotesAndChordsForKey(key, key_note)
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ALL_KEYS[key][key_note]["notes"]
    # Dorian
    key = "Dorian"
    # C
    key_note = "C"
    class_instance = NotesAndChordsForKey(key, key_note)
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ALL_KEYS[key][key_note]["notes"]
    # C#
    key_note = "C#"
    class_instance = NotesAndChordsForKey(key, key_note)
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ALL_KEYS[key][key_note]["notes"]
    # F
    key_note = "F"
    class_instance = NotesAndChordsForKey(key, key_note)
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ALL_KEYS[key][key_note]["notes"]
    # F#
    key_note = "F#"
    class_instance = NotesAndChordsForKey(key, key_note)
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ALL_KEYS[key][key_note]["notes"]
    # A#
    key_note = "A#"
    class_instance = NotesAndChordsForKey(key, key_note)
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ALL_KEYS[key][key_note]["notes"]
    # B
    key_note = "B"
    class_instance = NotesAndChordsForKey(key, key_note)
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ALL_KEYS[key][key_note]["notes"]
    # Phrygian
    key = "Phrygian"
    # C
    key_note = "C"
    class_instance = NotesAndChordsForKey(key, key_note)
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ALL_KEYS[key][key_note]["notes"]
    # C#
    key_note = "C#"
    class_instance = NotesAndChordsForKey(key, key_note)
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ALL_KEYS[key][key_note]["notes"]
    # F
    key_note = "F"
    class_instance = NotesAndChordsForKey(key, key_note)
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ALL_KEYS[key][key_note]["notes"]
    # F#
    key_note = "F#"
    class_instance = NotesAndChordsForKey(key, key_note)
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ALL_KEYS[key][key_note]["notes"]
    # A#
    key_note = "A#"
    class_instance = NotesAndChordsForKey(key, key_note)
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ALL_KEYS[key][key_note]["notes"]
    # B
    key_note = "B"
    class_instance = NotesAndChordsForKey(key, key_note)
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ALL_KEYS[key][key_note]["notes"]
    # Lydian
    key = "Lydian"
    # C
    key_note = "C"
    class_instance = NotesAndChordsForKey(key, key_note)
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ALL_KEYS[key][key_note]["notes"]
    # C#
    key_note = "C#"
    class_instance = NotesAndChordsForKey(key, key_note)
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ALL_KEYS[key][key_note]["notes"]
    # F
    key_note = "F"
    class_instance = NotesAndChordsForKey(key, key_note)
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ALL_KEYS[key][key_note]["notes"]
    # F#
    key_note = "F#"
    class_instance = NotesAndChordsForKey(key, key_note)
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ALL_KEYS[key][key_note]["notes"]
    # A#
    key_note = "A#"
    class_instance = NotesAndChordsForKey(key, key_note)
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ALL_KEYS[key][key_note]["notes"]
    # B
    key_note = "B"
    class_instance = NotesAndChordsForKey(key, key_note)
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ALL_KEYS[key][key_note]["notes"]
    # Mixolydian
    key = "Mixolydian"
    # C
    key_note = "C"
    class_instance = NotesAndChordsForKey(key, key_note)
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ALL_KEYS[key][key_note]["notes"]
    # C#
    key_note = "C#"
    class_instance = NotesAndChordsForKey(key, key_note)
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ALL_KEYS[key][key_note]["notes"]
    # F
    key_note = "F"
    class_instance = NotesAndChordsForKey(key, key_note)
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ALL_KEYS[key][key_note]["notes"]
    # F#
    key_note = "F#"
    class_instance = NotesAndChordsForKey(key, key_note)
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ALL_KEYS[key][key_note]["notes"]
    # A#
    key_note = "A#"
    class_instance = NotesAndChordsForKey(key, key_note)
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ALL_KEYS[key][key_note]["notes"]
    # B
    key_note = "B"
    class_instance = NotesAndChordsForKey(key, key_note)
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ALL_KEYS[key][key_note]["notes"]
    # Locrian
    key = "Locrian"
    # C
    key_note = "C"
    class_instance = NotesAndChordsForKey(key, key_note)
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ALL_KEYS[key][key_note]["notes"]
    # C#
    key_note = "C#"
    class_instance = NotesAndChordsForKey(key, key_note)
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ALL_KEYS[key][key_note]["notes"]
    # F
    key_note = "F"
    class_instance = NotesAndChordsForKey(key, key_note)
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ALL_KEYS[key][key_note]["notes"]
    # F#
    key_note = "F#"
    class_instance = NotesAndChordsForKey(key, key_note)
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ALL_KEYS[key][key_note]["notes"]
    # A#
    key_note = "A#"
    class_instance = NotesAndChordsForKey(key, key_note)
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ALL_KEYS[key][key_note]["notes"]
    # B
    key_note = "B"
    class_instance = NotesAndChordsForKey(key, key_note)
    class_instance.get_notes()
    assert class_instance.key_notes_letters == ALL_KEYS[key][key_note]["notes"]


def test_all_key_gen_match_chords():
    # C Major
    key, root_note = "Major", "C"
    class_instance = NotesAndChordsForKey(key, root_note)
    class_instance.get_notes_and_chords()
    assert class_instance.key_chords["chords"] == ALL_KEYS[key][root_note]["chords"]
    # D Dorian
    key, root_note = "Dorian", "D"
    class_instance = NotesAndChordsForKey(key, root_note)
    class_instance.get_notes_and_chords()
    assert class_instance.key_chords["chords"] == ALL_KEYS[key][root_note]["chords"]
    # E Phrygian
    key, root_note = "Phrygian", "E"
    class_instance = NotesAndChordsForKey(key, root_note)
    class_instance.get_notes_and_chords()
    assert class_instance.key_chords["chords"] == ALL_KEYS[key][root_note]["chords"]
    # F Lydian
    key, root_note = "Lydian", "F"
    class_instance = NotesAndChordsForKey(key, root_note)
    class_instance.get_notes_and_chords()
    assert class_instance.key_chords["chords"] == ALL_KEYS[key][root_note]["chords"]
    # G Mixolydian
    key, root_note = "Mixolydian", "G"
    class_instance = NotesAndChordsForKey(key, root_note)
    class_instance.get_notes_and_chords()
    assert class_instance.key_chords["chords"] == ALL_KEYS[key][root_note]["chords"]
    # A Minor (Aeolian)
    key, root_note = "Minor", "A"
    class_instance = NotesAndChordsForKey(key, root_note)
    class_instance.get_notes_and_chords()
    assert class_instance.key_chords["chords"] == ALL_KEYS[key][root_note]["chords"]
    # B Locrian
    key, root_note = "Locrian", "B"
    class_instance = NotesAndChordsForKey(key, root_note)
    class_instance.get_notes_and_chords()
    assert class_instance.key_chords["chords"] == ALL_KEYS[key][root_note]["chords"]
