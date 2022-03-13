import pytest
import common.notepad as Notepad
import common.compare as Compare



class WinBaseClass:

    def write_and_save_notepad(app_exe_or_full_exe_path, text, output_file_name):
        Notepad.write_and_save_notepad(app_exe_or_full_exe_path, text, output_file_name)

    def verify_csv(input_file_path, output_file_path):
        Compare.compare_csvs(input_file_path, output_file_path)

