# coding: utf-8

from PyQt5.QtWidgets import QMessageBox


def show_dialog(parent_window, message, title, icon, buttons=QMessageBox.Ok):
    """
        Show a message dialog to the user.

        This function displays a message dialog with the specified message, title, icon, and buttons.
        It ensures that the dialog is only shown when tests are not running.

    :param parent_window: PyQt parent window object
        The parent emitting dialog window.
    :param message: str
        The message to display in the dialog.
    :param title: str
        The title of the dialog window.
    :param icon: QMessageBox.Icon
        The icon to display in the dialog.
    :param buttons: QMessageBox.StandardButtons, optional
        The buttons to display in the dialog. Default is QMessageBox.Ok.

    :return: int
        The result of the dialog execution, which corresponds to the button clicked by the user.
    """
    if not hasattr(parent_window, 'tests_are_running') or (hasattr(parent_window, 'tests_are_running') and not parent_window.tests_are_running):
        dlg = QMessageBox(parent_window)
        dlg.setWindowTitle(title)
        dlg.setText(message)
        dlg.setIcon(icon)
        dlg.setStandardButtons(buttons)
        return dlg.exec()


def show_info_dialog(parent_window, message, title="Ok!"):
    """
        Display an informational dialog.

    :param parent_window: PyQt parent window object
        The parent emitting dialog window.
    :param message: str
    	The main text to be displayed in the dialog box.
    :param title: str
    	The title of the informational dialog box. Default is 'Ok!'.

    :return: None
    """
    show_dialog(parent_window, message, title, QMessageBox.Icon.Information)


def show_error_dialog(parent_window, message, title="Error!"):
    """
        Displays an error dialog.

    :param parent_window: PyQt parent window object
        The parent emitting dialog window.
    :param message: str
    	A string containing the error message to be displayed in the dialog.
    :param title: str, optional
    	A string containing the title of the dialog box. Default is "Error!".

    :return: None
    """
    show_dialog(parent_window, message, title, QMessageBox.Icon.Critical)


def show_question_dialog(parent_window, message, title="Question!", buttons=QMessageBox.Yes | QMessageBox.No):
    """
        Displays a question dialog window to the user.

        This function creates and shows a modal dialog window with a question icon, a specified message, and customizable buttons.

    :param parent_window: QWidget
    	The parent window over which the dialog is shown.
    :param message: str
    	The message to be displayed in the dialog window.
    :param title: str
    	The title of the dialog window. Defaults to "Question!".
    :param buttons: QMessageBox.StandardButtons
    	The buttons to be displayed in the dialog. Defaults to Yes and No buttons.

    :return: None
    	The function returns nothing, but creates a dialog window.
    """
    return show_dialog(parent_window, message, title, QMessageBox.Icon.Question, buttons)


def show_about(parent_window, message_text):
    """
        Displays an "About" information dialog.

        This function brings up a dialog with the specified message text as an
        "About" information context in the parent window.

    :param parent_window: QMainWindow or QDialog
        The window in which the dialog will be displayed.
    :param message_text: str
        The message text to display in the about dialog.

    :return: None
        The function returns nothing, but creates an "About" dialog.
    """
    show_info_dialog(parent_window, message_text, "About")
