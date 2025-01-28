# coding: utf-8

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QAction, QMessageBox, QLabel, QButtonGroup
from PyQt5.QtCore import Qt, QSettings
from PyQt5.QtWidgets import QApplication
import sys
import os

from all_keys import ALL_KEYS
# TEMPLATES
from templates.mw import Ui_Dialog as Ui_MainWindow

# MODULES
from core import keys_from_notes, notes_for_a_key, chords_for_a_key, add_chords_for_a_cord, sus_chords_for_a_cord, seventh_chords_for_a_cord, get_closest_keys, get_intervals
from key_gen import KEYS_INTERVALS
from tools.dialog_windows import show_error_dialog, show_info_dialog

# GLOBALS
version = "0.3"
copyright = "<a href='https:www.gnu.org/licenses/gpl-3.0.html'>The GNU General Public License v3.0</a>"
author_mail = "<a href='mailto: flex.studia.dev@gmail.com'>flex.studia.dev@gmail.com</a>"
bug_support_mail = "<a href='mailto: flex.studia.help@gmail.com'>flex.studia.help@gmail.com</a>"
github_url = "https://github.com/FlexStudia/MusicHelper"
__app_name__ = "Music Helper"
__org_name__ = "Flex Studia Dev"
__org_site__ = github_url
settings = QSettings(__org_name__, __app_name__)
about_text = (f"<b>{__app_name__}</b> v.{version}"
              f"<p>Copyright: {copyright}</p>"
              f"<p><a href='{github_url}'>GitHub repository</a> (program code and more information)</p>"
              f"<p>Created by Gorbacheva Maria ({author_mail})</p>"
              f"<p>For any questions and bug reports, please, mail at {bug_support_mail}</p>"
              "<p>In case of a bug, please report it and specify your operating system, "
              "provide a detailed description of the problem with screenshots "
              "and the files used and produced, if possible. Your contribution matters to make this program better!</p>")


class KeyHelper(QtWidgets.QDialog):
    def __init__(self):
        super(KeyHelper, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # window
        self.setWindowTitle(f"{__app_name__} v.{version}")
        # menu
        self.add_menue()
        # UI handlers
        self.KeyFromNotes_handler = KeyFromNotes(self)
        self.NotesAndChords_handler = NotesAndChords(self)
        self.ClosestKeys_handler = ClosestKeys(self)
        self.IntervalsNotes_handler = IntervalsNotes(self)

    def add_menue(self):
        try:
            menubar = QtWidgets.QMenuBar(self)
            about_menu = menubar.addMenu("About")
            about_action = QtWidgets.QAction("About", self)
            about_action.triggered.connect(self.show_about)
            about_menu.addAction(about_action)
            layout = self.layout()
            layout.setMenuBar(menubar)
        except Exception as e:
            message = f"Error in add_menue:\n{e}"
            print(message)
            show_error_dialog(self, message)

    def show_about(self):
        try:
            show_info_dialog(self, about_text, "About")
        except Exception as e:
            message = f"Error in show_about:\n{e}"
            print(message)
            show_error_dialog(self, message)


class KeyFromNotes:
    def __init__(self, parent_window):
        self.parent_window = parent_window
        self.set_UI()

    def set_UI(self):
        self.parent_window.ui.btn_key_search.clicked.connect(self.find_key_notes)

    def find_key_notes(self):
        try:
            self.clean_keys_output()
            list_of_chosen_notes = self.determine_list_of_chosen_notes()
            list_of_possible_keys = self.determine_list_of_possible_keys(list_of_chosen_notes)
            filtres = self.get_filtres()
            self.output_possible_keys_on_UI(list_of_possible_keys, filtres)
        except Exception as e:
            message = f"Error in find_key_notes: {e}"
            print(message)
            show_error_dialog(self.parent_window, message)

    def clean_keys_output(self):
        try:
            while self.parent_window.ui.keys_output.count():
                item = self.parent_window.ui.keys_output.takeAt(0)
                if widget := item.widget():
                    widget.deleteLater()
        except Exception as e:
            message = f"Error in clean_keys_output: {e}"
            print(message)
            show_error_dialog(self.parent_window, message)

    def determine_list_of_chosen_notes(self):
        try:
            list_of_chosen_notes = []
            checkboxes_list = [self.parent_window.ui.note_C, self.parent_window.ui.note_Cch, self.parent_window.ui.note_D, self.parent_window.ui.note_Dch, self.parent_window.ui.note_E, self.parent_window.ui.note_F, self.parent_window.ui.note_Fch, self.parent_window.ui.note_G, self.parent_window.ui.note_Gch, self.parent_window.ui.note_A, self.parent_window.ui.note_Ach, self.parent_window.ui.note_B]
            for checkbox in checkboxes_list:
                if checkbox.isChecked():
                    list_of_chosen_notes.append(checkbox.text())
            return list_of_chosen_notes
        except Exception as e:
            message = f"Error in determine_list_of_chosen_notes: {e}"
            print(message)
            show_error_dialog(self.parent_window, message)

    @staticmethod
    def determine_list_of_possible_keys(list_of_chosen_notes):
        return keys_from_notes(list_of_chosen_notes)

    def get_filtres(self):
        try:
            CHECKBOXES = {
                "Major": self.parent_window.ui.filtre_Major,
                "Dorian": self.parent_window.ui.filtre_Dorian,
                "Phrygian": self.parent_window.ui.filtre_Phrygian,
                "Lydian": self.parent_window.ui.filtre_Lydian,
                "Mixolydian": self.parent_window.ui.filtre_Mixolydian,
                "Minor": self.parent_window.ui.filtre_Minor,
                "Locrian": self.parent_window.ui.filtre_Locrian,
            }
            filtres = []
            for checkbox in CHECKBOXES.values():
                if checkbox.isChecked():
                    filtres.append(checkbox.text())
            return filtres
        except Exception as e:
            message = f"Error in get_filtres: {e}"
            print(message)
            show_error_dialog(self.parent_window, message)

    def output_possible_keys_on_UI(self, list_of_possible_keys, filtre):
        try:
            self.parent_window.ui.keys_output.addWidget(QLabel("Label"), 0, 0)
            self.parent_window.ui.keys_output.addWidget(QLabel("Notes"), 0, 1)
            self.parent_window.ui.keys_output.addWidget(QLabel("Emotions"), 0, 2)
            self.parent_window.ui.keys_output.addWidget(QLabel("Utilization"), 0, 3)
            for index, value in enumerate(list_of_possible_keys):
                root_note = value.split(' ')[0]
                key_name = value.split(' ')[1]
                if key_name in filtre:
                    self.parent_window.ui.keys_output.addWidget(QLabel(f"{value}"), index + 1, 0)
                    self.parent_window.ui.keys_output.addWidget(QLabel(f"{' '.join(ALL_KEYS[key_name][root_note]['notes'])}"), index + 1, 1)
                    self.parent_window.ui.keys_output.addWidget(QLabel(f"{KEYS_INTERVALS[key_name]['emotions']}"), index + 1, 2)
                    self.parent_window.ui.keys_output.addWidget(QLabel(f"{KEYS_INTERVALS[key_name]['utilization']}"), index + 1, 3)
        except Exception as e:
            message = f"Error in output_possible_keys_on_UI: {e}"
            print(message)
            show_error_dialog(self.parent_window, message)


class NotesAndChords:
    def __init__(self, parent_window):
        self.parent_window = parent_window
        self.set_UI()

    def set_UI(self):
        # group notes UI in a group
        self.notes_group = QButtonGroup(self.parent_window)
        self.notes_group.addButton(self.parent_window.ui.rbtn_C)
        self.notes_group.addButton(self.parent_window.ui.rbtn_Cd)
        self.notes_group.addButton(self.parent_window.ui.rbtn_D)
        self.notes_group.addButton(self.parent_window.ui.rbtn_Dd)
        self.notes_group.addButton(self.parent_window.ui.rbtn_E)
        self.notes_group.addButton(self.parent_window.ui.rbtn_F)
        self.notes_group.addButton(self.parent_window.ui.rbtn_Fd)
        self.notes_group.addButton(self.parent_window.ui.rbtn_G)
        self.notes_group.addButton(self.parent_window.ui.rbtn_Gd)
        self.notes_group.addButton(self.parent_window.ui.rbtn_A)
        self.notes_group.addButton(self.parent_window.ui.rbtn_Ad)
        self.notes_group.addButton(self.parent_window.ui.rbtn_B)
        # group keys UI in a group
        self.keys_group = QButtonGroup(self.parent_window)
        self.keys_group.addButton(self.parent_window.ui.rbtn_Major)
        self.keys_group.addButton(self.parent_window.ui.rbtn_Dorian)
        self.keys_group.addButton(self.parent_window.ui.rbtn_Phrygian)
        self.keys_group.addButton(self.parent_window.ui.rbtn_Lydian)
        self.keys_group.addButton(self.parent_window.ui.rbtn_Mixolydian)
        self.keys_group.addButton(self.parent_window.ui.rbtn_Minor)
        self.keys_group.addButton(self.parent_window.ui.rbtn_Locrian)
        # btn slot
        self.parent_window.ui.btn_notes_and_chords_search.clicked.connect(self.find_notes_and_chords)

    def find_notes_and_chords(self):
        try:
            key_name = self.get_current_key()
            root_note = self.get_current_root_note()
            if key_name and root_note:
                notes = notes_for_a_key(key_name, root_note)
                basic_chords = chords_for_a_key(key_name, root_note)
                add_chords = self.get_add_chords(notes, basic_chords)
                sus_chords = self.get_sus_chords(notes, basic_chords)
                seventh_chords = self.get_seventh_chords(notes, basic_chords)
                self.output_notes_and_chords_on_UI(notes, basic_chords, add_chords, sus_chords, seventh_chords)
        except Exception as e:
            message = f"Error in find_notes_and_chords: {e}"
            print(message)
            show_error_dialog(self.parent_window, message)

    def get_current_key(self):
        try:
            checked_button = self.keys_group.checkedButton()
            if checked_button:
                return checked_button.text()
            return ""
        except Exception as e:
            message = f"Error in get_current_key: {e}"
            print(message)
            show_error_dialog(self.parent_window, message)

    def get_current_root_note(self):
        try:
            checked_button = self.notes_group.checkedButton()
            if checked_button:
                return checked_button.text()
            return ""
        except Exception as e:
            message = f"Error in get_current_root_note: {e}"
            print(message)
            show_error_dialog(self.parent_window, message)

    @staticmethod
    def get_add_chords(notes, basic_chords):
        try:
            add_chords = {}
            for chord in basic_chords.keys():
                add_chords[chord] = add_chords_for_a_cord(basic_chords[chord], notes)
            return add_chords
        except Exception as e:
            message = f"Error in get_add_chords: {e}"
            print(message)

    @staticmethod
    def get_sus_chords(notes, basic_chords):
        try:
            sus_chords = {}
            for chord in basic_chords.keys():
                sus_chords[chord] = sus_chords_for_a_cord(basic_chords[chord], notes)
            return sus_chords
        except Exception as e:
            message = f"Error in get_sus_chords: {e}"
            print(message)

    @staticmethod
    def get_seventh_chords(notes, basic_chords):
        try:
            seventh_chord = {}
            for chord in basic_chords.keys():
                seventh_chord[chord] = seventh_chords_for_a_cord(basic_chords[chord], notes)
            return seventh_chord
        except Exception as e:
            message = f"Error in get_seventh_chords: {e}"
            print(message)

    def output_notes_and_chords_on_UI(self, notes, basic_chords, add_chords, sus_chords, seventh_chords):
        try:
            # notes output
            self.parent_window.ui.notes_output.setText(" ".join(notes))
            # basic chords
            self.output_basic_chords_on_UI(basic_chords)
            # add chords
            self.output_add_chords_on_UI(add_chords)
            # sus chords
            self.output_sus_chords_on_UI(sus_chords)
            # seventh chords
            self.output_seventh_chords_on_UI(seventh_chords)
        except Exception as e:
            message = f"Error in output_notes_and_chords_on_UI: {e}"
            print(message)
            show_error_dialog(self.parent_window, message)

    def output_basic_chords_on_UI(self, basic_chords):
        try:
            UI_LABELS = {
                1: self.parent_window.ui.line_1,
                2: self.parent_window.ui.line_2,
                3: self.parent_window.ui.line_3,
                4: self.parent_window.ui.line_4,
                5: self.parent_window.ui.line_5,
                6: self.parent_window.ui.line_6,
                7: self.parent_window.ui.line_7,
            }
            for index, chord in enumerate(basic_chords.keys()):
                output_chord_text = f"{chord}: {' '.join(basic_chords[chord])}"
                UI_LABELS[index + 1].setText(output_chord_text)
        except Exception as e:
            message = f"Error in output_basic_chords_on_UI: {e}"
            print(message)
            show_error_dialog(self.parent_window, message)

    def output_add_chords_on_UI(self, add_chords):
        try:
            UI_LABELS = {
                1: self.parent_window.ui.add_1,
                2: self.parent_window.ui.add_2,
                3: self.parent_window.ui.add_3,
                4: self.parent_window.ui.add_4,
                5: self.parent_window.ui.add_5,
                6: self.parent_window.ui.add_6,
                7: self.parent_window.ui.add_7,
            }
            for index, chord in enumerate(add_chords.keys()):
                output_chord_text = f"{' '.join(add_chords[chord][0])}, {' '.join(add_chords[chord][1])}"
                UI_LABELS[index + 1].setText(output_chord_text)
        except Exception as e:
            message = f"Error in output_add_chords_on_UI: {e}"
            print(message)
            show_error_dialog(self.parent_window, message)

    def output_sus_chords_on_UI(self, sus_chords):
        try:
            UI_LABELS = {
                1: self.parent_window.ui.sus_1,
                2: self.parent_window.ui.sus_2,
                3: self.parent_window.ui.sus_3,
                4: self.parent_window.ui.sus_4,
                5: self.parent_window.ui.sus_5,
                6: self.parent_window.ui.sus_6,
                7: self.parent_window.ui.sus_7,
            }
            for index, chord in enumerate(sus_chords.keys()):
                output_chord_text = f"{' '.join(sus_chords[chord][0])}, {' '.join(sus_chords[chord][1])}"
                UI_LABELS[index + 1].setText(output_chord_text)
        except Exception as e:
            message = f"Error in output_sus_chords_on_UI: {e}"
            print(message)
            show_error_dialog(self.parent_window, message)

    def output_seventh_chords_on_UI(self, seventh_chords):
        try:
            UI_LABELS = {
                1: self.parent_window.ui.seven_1,
                2: self.parent_window.ui.seven_2,
                3: self.parent_window.ui.seven_3,
                4: self.parent_window.ui.seven_4,
                5: self.parent_window.ui.seven_5,
                6: self.parent_window.ui.seven_6,
                7: self.parent_window.ui.seven_7,
            }
            for index, chord in enumerate(seventh_chords.keys()):
                output_chord_text = f"{' '.join(seventh_chords[chord])}"
                UI_LABELS[index + 1].setText(output_chord_text)
        except Exception as e:
            message = f"Error in output_seventh_chords_on_UI: {e}"
            print(message)
            show_error_dialog(self.parent_window, message)


class ClosestKeys:
    def __init__(self, parent_window):
        self.parent_window = parent_window
        self.set_UI()

    def set_UI(self):
        # group notes UI in a group
        self.notes_group = QButtonGroup(self.parent_window)
        self.notes_group.addButton(self.parent_window.ui.root_C)
        self.notes_group.addButton(self.parent_window.ui.root_Cd)
        self.notes_group.addButton(self.parent_window.ui.root_D)
        self.notes_group.addButton(self.parent_window.ui.root_Dd)
        self.notes_group.addButton(self.parent_window.ui.root_E)
        self.notes_group.addButton(self.parent_window.ui.root_F)
        self.notes_group.addButton(self.parent_window.ui.root_Fd)
        self.notes_group.addButton(self.parent_window.ui.root_G)
        self.notes_group.addButton(self.parent_window.ui.root_Gd)
        self.notes_group.addButton(self.parent_window.ui.root_A)
        self.notes_group.addButton(self.parent_window.ui.root_Ad)
        self.notes_group.addButton(self.parent_window.ui.root_B)
        # group keys UI in a group
        self.keys_group = QButtonGroup(self.parent_window)
        self.keys_group.addButton(self.parent_window.ui.mode_Major)
        self.keys_group.addButton(self.parent_window.ui.mode_Dorian)
        self.keys_group.addButton(self.parent_window.ui.mode_Phrygian)
        self.keys_group.addButton(self.parent_window.ui.mode_Lydian)
        self.keys_group.addButton(self.parent_window.ui.mode_Mixolydian)
        self.keys_group.addButton(self.parent_window.ui.mode_Minor)
        self.keys_group.addButton(self.parent_window.ui.mode_Locrian)
        # btn slot
        self.parent_window.ui.btn_search_closest.clicked.connect(self.search_for_closest_keys)

    def search_for_closest_keys(self):
        try:
            root_note = self.get_root_note()
            key_mode = self.get_key_name()
            closest_keys = get_closest_keys(key_mode, root_note)
            self.output_closest_keys_on_UI(closest_keys)
        except Exception as e:
            message = f"Error in search_for_closest_keys: {e}"
            print(message)
            show_error_dialog(self.parent_window, message)

    def get_root_note(self):
        try:
            checked_button = self.notes_group.checkedButton()
            if checked_button:
                return checked_button.text()
            return ""
        except Exception as e:
            message = f"Error in get_root_note: {e}"
            print(message)
            show_error_dialog(self.parent_window, message)

    def get_key_name(self):
        try:
            checked_button = self.keys_group.checkedButton()
            if checked_button:
                return checked_button.text()
            return ""
        except Exception as e:
            message = f"Error in get_key_name: {e}"
            print(message)
            show_error_dialog(self.parent_window, message)

    def output_closest_keys_on_UI(self, closest_keys):
        try:
            # keys with the same notes
            SAME_KEYS_LABELS = {
                "Major": self.parent_window.ui.Major_notes,
                "Dorian": self.parent_window.ui.Dorian_notes,
                "Phrygian": self.parent_window.ui.Phrygian_notes,
                "Lydian": self.parent_window.ui.Lydian_notes,
                "Mixolydian": self.parent_window.ui.Mixolydian_notes,
                "Minor": self.parent_window.ui.Minor_notes,
                "Locrian": self.parent_window.ui.Locrian_notes,
            }
            for key in SAME_KEYS_LABELS.keys():
                SAME_KEYS_LABELS[key].setText(f"{closest_keys[key]['0'][1]}")
            # one note different keys
            # right: +1
            RIGHT_1_KEYS_LABELS = {
                "Major": self.parent_window.ui.Major_1_notes_left,
                "Dorian": self.parent_window.ui.Dorian_1_notes_left,
                "Phrygian": self.parent_window.ui.Phrygian_1_notes_left,
                "Lydian": self.parent_window.ui.Lydian_1_notes_left,
                "Mixolydian": self.parent_window.ui.Mixolydian_1_notes_left,
                "Minor": self.parent_window.ui.Minor_1_notes_left,
                "Locrian": self.parent_window.ui.Locrian_1_notes_left,
            }
            for key in RIGHT_1_KEYS_LABELS.keys():
                RIGHT_1_KEYS_LABELS[key].setText(f"{closest_keys[key]['+1'][1]}")
            # left: -1
            LEFT_1_KEYS_LABELS = {
                "Major": self.parent_window.ui.Major_1_notes_right,
                "Dorian": self.parent_window.ui.Dorian_1_notes_right,
                "Phrygian": self.parent_window.ui.Phrygian_1_notes_right,
                "Lydian": self.parent_window.ui.Lydian_1_notes_right,
                "Mixolydian": self.parent_window.ui.Mixolydian_1_notes_right,
                "Minor": self.parent_window.ui.Minor_1_notes_right,
                "Locrian": self.parent_window.ui.Locrian_1_notes_right,
            }
            for key in LEFT_1_KEYS_LABELS.keys():
                LEFT_1_KEYS_LABELS[key].setText(f"{closest_keys[key]['-1'][1]}")
            # right: +2
            RIGHT_2_KEYS_LABELS = {
                "Major": self.parent_window.ui.Major_2_notes_left,
                "Dorian": self.parent_window.ui.Dorian_2_notes_left,
                "Phrygian": self.parent_window.ui.Phrygian_2_notes_left,
                "Lydian": self.parent_window.ui.Lydian_2_notes_left,
                "Mixolydian": self.parent_window.ui.Mixolydian_2_notes_left,
                "Minor": self.parent_window.ui.Minor_2_notes_left,
                "Locrian": self.parent_window.ui.Locrian_2_notes_left,
            }
            for key in RIGHT_2_KEYS_LABELS.keys():
                RIGHT_2_KEYS_LABELS[key].setText(f"{closest_keys[key]['+2'][1]}")
            # left: -2
            LEFT_2_KEYS_LABELS = {
                "Major": self.parent_window.ui.Major_2_notes_right,
                "Dorian": self.parent_window.ui.Dorian_2_notes_right,
                "Phrygian": self.parent_window.ui.Phrygian_2_notes_right,
                "Lydian": self.parent_window.ui.Lydian_2_notes_right,
                "Mixolydian": self.parent_window.ui.Mixolydian_2_notes_right,
                "Minor": self.parent_window.ui.Minor_2_notes_right,
                "Locrian": self.parent_window.ui.Locrian_2_notes_right,
            }
            for key in LEFT_2_KEYS_LABELS.keys():
                LEFT_2_KEYS_LABELS[key].setText(f"{closest_keys[key]['-2'][1]}")
        except Exception as e:
            message = f"Error in output_closest_keys_on_UI: {e}"
            print(message)
            show_error_dialog(self.parent_window, message)


class IntervalsNotes:
    def __init__(self, parent_window):
        self.parent_window = parent_window
        self.set_UI()

    def set_UI(self):
        # group notes UI in a group
        self.notes_group = QButtonGroup(self.parent_window)
        self.notes_group.addButton(self.parent_window.ui.int_C)
        self.notes_group.addButton(self.parent_window.ui.int_Cd)
        self.notes_group.addButton(self.parent_window.ui.int_D)
        self.notes_group.addButton(self.parent_window.ui.int_Dd)
        self.notes_group.addButton(self.parent_window.ui.int_E)
        self.notes_group.addButton(self.parent_window.ui.int_F)
        self.notes_group.addButton(self.parent_window.ui.int_Fd)
        self.notes_group.addButton(self.parent_window.ui.int_G)
        self.notes_group.addButton(self.parent_window.ui.int_Gd)
        self.notes_group.addButton(self.parent_window.ui.int_A)
        self.notes_group.addButton(self.parent_window.ui.int_Ad)
        self.notes_group.addButton(self.parent_window.ui.int_B)
        # btn slot
        self.parent_window.ui.btn_interval_search.clicked.connect(self.search_for_intervals)

    def search_for_intervals(self):
        try:
            target_note = self.get_target_note()
            intervals = get_intervals(target_note)
            self.output_intervals_on_UI(intervals)
        except Exception as e:
            message = f"Error in search_for_intervals: {e}"
            print(message)
            show_error_dialog(self.parent_window, message)

    def get_target_note(self):
        try:
            checked_button = self.notes_group.checkedButton()
            if checked_button:
                return checked_button.text()
            return ""
        except Exception as e:
            message = f"Error in get_target_note: {e}"
            print(message)
            show_error_dialog(self.parent_window, message)

    def output_intervals_on_UI(self, intervals):
        try:
            LABELS = {
                "P1": self.parent_window.ui.P1,
                "P8": self.parent_window.ui.P8,
                "P5": self.parent_window.ui.P5,
                "P4": self.parent_window.ui.P4,
                "M3": self.parent_window.ui.M3,
                "m6": self.parent_window.ui.m6,
                "m3": self.parent_window.ui.m3,
                "M6": self.parent_window.ui.M6,
                "M2": self.parent_window.ui.M2,
                "m7": self.parent_window.ui.m7,
                "m2": self.parent_window.ui.m2,
                "M7": self.parent_window.ui.M7,
                "m5": self.parent_window.ui.m5,
            }
            for label in LABELS.keys():
                LABELS[label].setText(f"{intervals[label]}")
        except Exception as e:
            message = f"Error in output_intervals_on_UI: {e}"
            print(message)
            show_error_dialog(self.parent_window, message)


def end_of_file():
    pass

# APP RUN
if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    win = KeyHelper()
    win.setWindowFlags(Qt.WindowType.WindowMinimizeButtonHint | Qt.WindowType.WindowMaximizeButtonHint | Qt.WindowType.WindowCloseButtonHint)
    win.show()
    sys.exit(app.exec())

