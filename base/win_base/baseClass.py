import pytest
import common.notepad as Notepad


class WinBaseClass:

    def write_and_save_notepad(app_exe_or_full_exe_path, text, output_file_name):
        Notepad.write_and_save_notepad(app_exe_or_full_exe_path, text, output_file_name)
