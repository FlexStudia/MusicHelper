# coding: utf-8
import copy

FROM_NUMBER_TO_LETTER = {0: "C", 1: "C#", 2: "D", 3: "D#", 4: "E", 5: "F", 6: "F#", 7: "G", 8: "G#", 9: "A", 10: "A#", 11: "B"}

def twelve_down(tones_list: list) -> list:
    downed_list = copy.deepcopy(tones_list)
    for i, v in enumerate(tones_list):
        while downed_list[i] > 11:
            downed_list[i] -= 12
    return downed_list

def from_list_of_numbers_to_letters(list_of_tones: list) -> list:
    list_of_letters = copy.deepcopy(list_of_tones)
    for i, v in enumerate(list_of_tones):
        list_of_letters[i] = FROM_NUMBER_TO_LETTER[v]
    return list_of_letters
