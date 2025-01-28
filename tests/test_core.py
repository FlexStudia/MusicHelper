# coding: utf-8

import core


def test_keys_from_notes():
    assert set(core.keys_from_notes(["C", "D", "E", "F", "G", "A", "B"])) == {"C Major", "D Dorian", "E Phrygian", "F Lydian", "G Mixolydian", "A Minor", "B Locrian"}
    assert set(core.keys_from_notes(['C#', 'D', 'E', 'F#', 'G', 'A', 'B'])) == {'A Mixolydian', 'B Minor', 'C# Locrian', 'D Major', 'E Dorian', 'F# Phrygian', 'G Lydian'}


def test_chords_for_a_cord():
    # add cords
    assert core.add_chords_for_a_cord(["C", "E", "G"], ["C", "D", "E", "F", "G", "A", "B"]) == (["C", "D", "E", "G"], ["C", "E", "F", "G"])
    assert core.add_chords_for_a_cord(["C", "D#", "G"], ["D#", "F", "G", "G#", "A#", "C", "C#"]) == (["C", "C#", "D#", "G"], ["C", "D#", "F", "G"])
    assert core.add_chords_for_a_cord(["G#", "B", "D#"], ["A", "B", "C#", "D#", "E", "F#", "G#"]) == (["G#", "A", "B", "D#"], ["G#", "B", "C#", "D#"])
    # sus cords
    assert core.sus_chords_for_a_cord(["C", "E", "G"], ["C", "D", "E", "F", "G", "A", "B"]) == (["C", "D", "G"], ["C", "F", "G"])
    assert core.sus_chords_for_a_cord(["C", "D#", "G"], ["D#", "F", "G", "G#", "A#", "C", "C#"]) == (["C", "C#", "G"], ["C", "F", "G"])
    assert core.sus_chords_for_a_cord(["G#", "B", "D#"], ["A", "B", "C#", "D#", "E", "F#", "G#"]) == (["G#", "A", "D#"], ["G#", "C#", "D#"])
    # 7th cords
    assert core.seventh_chords_for_a_cord(["C", "E", "G"], ["C", "D", "E", "F", "G", "A", "B"]) == ["C", "E", "G", "B"]
    assert core.seventh_chords_for_a_cord(["C", "D#", "G"], ["D#", "F", "G", "G#", "A#", "C", "C#"]) == ["C", "D#", "G", "A#"]
    assert core.seventh_chords_for_a_cord(["G#", "B", "D#"], ["A", "B", "C#", "D#", "E", "F#", "G#"]) == ["G#", "B", "D#", "F#"]


def test_compare_keys():
    assert core.get_similar_keys("Major", "C") == {'Major': {'identical': ('Major', 'C'), 'similar': [('Major', 'F'), ('Major', 'G')]}, 'Dorian': {'identical': ('Dorian', 'D'), 'similar': [('Dorian', 'G'), ('Dorian', 'A')]}, 'Phrygian': {'identical': ('Phrygian', 'E'), 'similar': [('Phrygian', 'A'), ('Phrygian', 'B')]}, 'Lydian': {'identical': ('Lydian', 'F'), 'similar': [('Lydian', 'C'), ('Lydian', 'A#')]}, 'Mixolydian': {'identical': ('Mixolydian', 'G'), 'similar': [('Mixolydian', 'C'), ('Mixolydian', 'D')]}, 'Minor': {'identical': ('Minor', 'A'), 'similar': [('Minor', 'D'), ('Minor', 'E')]}, 'Locrian': {'identical': ('Locrian', 'B'), 'similar': [('Locrian', 'E'), ('Locrian', 'F#')]}}
    assert core.get_similar_keys("Major", "F") == {'Major': {'identical': ('Major', 'F'), 'similar': [('Major', 'C'), ('Major', 'A#')]}, 'Dorian': {'identical': ('Dorian', 'G'), 'similar': [('Dorian', 'C'), ('Dorian', 'D')]}, 'Phrygian': {'identical': ('Phrygian', 'A'), 'similar': [('Phrygian', 'D'), ('Phrygian', 'E')]}, 'Lydian': {'identical': ('Lydian', 'A#'), 'similar': [('Lydian', 'D#'), ('Lydian', 'F')]}, 'Mixolydian': {'identical': ('Mixolydian', 'C'), 'similar': [('Mixolydian', 'F'), ('Mixolydian', 'G')]}, 'Minor': {'identical': ('Minor', 'D'), 'similar': [('Minor', 'G'), ('Minor', 'A')]}, 'Locrian': {'identical': ('Locrian', 'E'), 'similar': [('Locrian', 'A'), ('Locrian', 'B')]}}


def test_get_closest_keys():
    assert core.get_closest_keys("Major", "C") == {'Dorian': {'+1': ('Dorian', 'G'), '+2': ('Dorian', 'C'), '-1': ('Dorian', 'A'), '-2': ('Dorian', 'E'), '0': ('Dorian', 'D')}, 'Locrian': {'+1': ('Locrian', 'E'), '+2': ('Locrian', 'A'), '-1': ('Locrian', 'F#'), '-2': ('Locrian', 'C#'), '0': ('Locrian', 'B')}, 'Lydian': {'+1': ('Lydian', 'A#'), '+2': ('Lydian', 'D#'), '-1': ('Lydian', 'C'), '-2': ('Lydian', 'G'), '0': ('Lydian', 'F')}, 'Major': {'+1': ('Major', 'F'),  '+2': ('Major', 'A#'),  '-1': ('Major', 'G'),  '-2': ('Major', 'D'),  '0': ('Major', 'C')}, 'Minor': {'+1': ('Minor', 'D'),  '+2': ('Minor', 'G'),  '-1': ('Minor', 'E'),  '-2': ('Minor', 'B'),  '0': ('Minor', 'A')}, 'Mixolydian': {'+1': ('Mixolydian', 'C'), '+2': ('Mixolydian', 'F'), '-1': ('Mixolydian', 'D'), '-2': ('Mixolydian', 'A'), '0': ('Mixolydian', 'G')}, 'Phrygian': {'+1': ('Phrygian', 'A'),  '+2': ('Phrygian', 'D'),  '-1': ('Phrygian', 'B'),  '-2': ('Phrygian', 'F#'),  '0': ('Phrygian', 'E')}}


def test_get_intervals():
    assert core.get_intervals("C") == {'P1': 'C', 'P8': 'C+', 'P5': 'G', 'P4': 'F', 'M3': 'E', 'm6': 'G#', 'm3': 'D#', 'M6': 'A', 'M2': 'D', 'm7': 'A#', 'm2': 'C#', 'M7': 'B', 'm5': 'F#'}
    assert core.get_intervals("F#") == {'M2': 'G#', 'M3': 'A#', 'M6': 'D#+', 'M7': 'F+', 'P1': 'F#', 'P4': 'B', 'P5': 'C#+', 'P8': 'F#+', 'm2': 'G', 'm3': 'A', 'm5': 'C+', 'm6': 'D+', 'm7': 'E+'}
