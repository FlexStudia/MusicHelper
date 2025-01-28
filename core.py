# coding: utf-8
from colorama.ansi import clear_screen

from all_keys import ALL_KEYS

INTERVALS = {
    "P1": 0,
    "P8": 12,
    "P5": 7,
    "P4": 5,
    "M3": 4,
    "m6": 8,
    "m3": 3,
    "M6": 9,
    "M2": 2,
    "m7": 10,
    "m2": 1,
    "M7": 11,
    "m5": 6,
}


def notes_for_a_key(key_name: str, root_note: str) -> list:
    return ALL_KEYS[key_name][root_note]["notes"]


def chords_for_a_key(key_name: str, root_note: str) -> dict:
    return ALL_KEYS[key_name][root_note]["chords"]


def add_chords_for_a_cord(chord: list, key_notes: list) -> tuple:
    key_notes_extended = key_notes * 2
    middle_note_index = key_notes.index(chord[1])
    new_note_1 = key_notes_extended[middle_note_index - 1]
    add_1 = chord[:1] + [new_note_1] + chord[1:]
    new_note_2 = key_notes_extended[middle_note_index + 1]
    add_2 = chord[:2] + [new_note_2] + chord[2:]
    return add_1, add_2


def sus_chords_for_a_cord(chord: list, key_notes: list) -> tuple:
    add_chord_1, add_chord_2 = add_chords_for_a_cord(chord, key_notes)
    sus_chord_1 = add_chord_1[:2] + add_chord_1[3:]
    sus_chord_2 = add_chord_2[:1] + add_chord_2[2:]
    return sus_chord_1, sus_chord_2


def seventh_chords_for_a_cord(chord: list, key_notes: list) -> list:
    key_notes_extended = key_notes * 2
    last_note_index = key_notes.index(chord[2])
    new_note = key_notes_extended[last_note_index + 2]
    return chord[:] + [new_note]


def keys_from_notes(notes_list: list) -> list:
    possible_keys = []
    for key_name in ALL_KEYS.keys():
        for root_note in ALL_KEYS[key_name].keys():
            if (set(notes_list) == set(ALL_KEYS[key_name][root_note]["notes"]) or
                    set(notes_list).issubset(set(ALL_KEYS[key_name][root_note]["notes"])) or
                    set(ALL_KEYS[key_name][root_note]["notes"]).issubset(set(notes_list))):
                possible_keys.append(f"{root_note} {key_name}")
    return possible_keys


def get_similar_keys(target_key_name: str, target_key_root: str) -> dict:
    similar_keys = {
        "Major": {  # Ionian
            "identical": (),
            "similar": [],
        },
        "Dorian": {
            "identical": "",
            "similar": [],
        },
        "Phrygian": {
            "identical": (),
            "similar": [],
        },
        "Lydian": {
            "identical": (),
            "similar": [],
        },
        "Mixolydian": {
            "identical": (),
            "similar": [],
        },
        "Minor": {  # Aeolian
            "identical": (),
            "similar": [],
        },
        "Locrian": {
            "identical": (),
            "similar": [],
        },
    }
    target_key_notes = ALL_KEYS[target_key_name][target_key_root]["notes"]
    target_set = set(target_key_notes)
    for key in ALL_KEYS.keys():
        for root_note in ALL_KEYS[key].keys():
            current_key_notes = ALL_KEYS[key][root_note]["notes"]
            current_set = set(current_key_notes)
            difference = target_set.symmetric_difference(current_set)
            if len(difference) == 0:
                similar_keys[key]["identical"] = (key, root_note)
            elif len(difference) == 2:
                similar_keys[key]["similar"].append((key, root_note))
    return similar_keys


def get_closest_keys(target_key_name: str, target_key_root: str) -> dict:
    closest_keys = {
        "Major": {  # Ionian
            "+2": None,
            "+1": None,
            "0": None,
            "-1": None,
            "-2": None,
        },
        "Dorian": {
            "+2": None,
            "+1": None,
            "0": None,
            "-1": None,
            "-2": None,
        },
        "Phrygian": {
            "+2": None,
            "+1": None,
            "0": None,
            "-1": None,
            "-2": None,
        },
        "Lydian": {
            "+2": None,
            "+1": None,
            "0": None,
            "-1": None,
            "-2": None,
        },
        "Mixolydian": {
            "+2": None,
            "+1": None,
            "0": None,
            "-1": None,
            "-2": None,
        },
        "Minor": {  # Aeolian
            "+2": None,
            "+1": None,
            "0": None,
            "-1": None,
            "-2": None,
        },
        "Locrian": {
            "+2": None,
            "+1": None,
            "0": None,
            "-1": None,
            "-2": None,
        },
    }
    similar_keys = get_similar_keys(target_key_name, target_key_root)
    # identical keys in all modes
    for key in similar_keys.keys():
        closest_keys[key]["0"] = similar_keys[key]["identical"]
    # first level for the given mode
    closest_keys[target_key_name]["+1"] = similar_keys[target_key_name]["similar"][0]
    closest_keys[target_key_name]["-1"] = similar_keys[target_key_name]["similar"][1]
    # other first levels
    key_name = closest_keys[target_key_name]["+1"][0]
    key_root = closest_keys[target_key_name]["+1"][1]
    target_set = set(ALL_KEYS[key_name][key_root]["notes"])
    for key in similar_keys.keys():
        if key != target_key_name:
            key_name = similar_keys[key]["similar"][0][0]
            key_root = similar_keys[key]["similar"][0][1]
            current_set = set(ALL_KEYS[key_name][key_root]["notes"])
            if target_set == current_set:
                closest_keys[key]["+1"] = (key_name, key_root)
                closest_keys[key]["-1"] = (similar_keys[key]["similar"][1][0], similar_keys[key]["similar"][1][1])
            else:
                closest_keys[key]["+1"] = (similar_keys[key]["similar"][1][0], similar_keys[key]["similar"][1][1])
                closest_keys[key]["-1"] = (key_name, key_root)
    # second level -2
    key_name = closest_keys[target_key_name]["-1"][0]
    key_root = closest_keys[target_key_name]["-1"][1]
    first_level_closest_keys = get_similar_keys(key_name, key_root)
    for key in closest_keys.keys():
        if first_level_closest_keys[key]["similar"][0] != closest_keys[key]["0"]:
            closest_keys[key]["-2"] = first_level_closest_keys[key]["similar"][0]
        else:
            closest_keys[key]["-2"] = first_level_closest_keys[key]["similar"][1]
    # second level +2
    key_name = closest_keys[target_key_name]["+1"][0]
    key_root = closest_keys[target_key_name]["+1"][1]
    first_level_closest_keys = get_similar_keys(key_name, key_root)
    for key in closest_keys.keys():
        if first_level_closest_keys[key]["similar"][0] != closest_keys[key]["0"]:
            closest_keys[key]["+2"] = first_level_closest_keys[key]["similar"][0]
        else:
            closest_keys[key]["+2"] = first_level_closest_keys[key]["similar"][1]
    return closest_keys


def get_intervals(target_bote: str) -> dict:
    double_notes_list = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    target_note_index = double_notes_list.index(target_bote)
    intervals = {}
    for interval_name in INTERVALS.keys():
        current_note_index = target_note_index + INTERVALS[interval_name]
        intervals[interval_name] = f"{double_notes_list[current_note_index]}{'+' if current_note_index > 11 else ''}"
    return intervals

