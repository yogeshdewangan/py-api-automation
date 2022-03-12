import pytest, os, sys

from base.win_base.baseClass import WinBaseClass

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
input_file_path = os.path.join(ROOT_DIR, "inputs\data.csv").replace("tests\\", "")
output_file_path = os.path.join(ROOT_DIR, "outputs\data.csv").replace("tests\\", "")


class TestNotepadAndCompareCSV(WinBaseClass):

    @pytest.mark.Smoke
    def test_write_notepad_compare_csv(self):
        input = str(open(input_file_path, "r").readlines()).replace('[','').replace(']','').replace('\'','').replace('\\n,','\\n')

        WinBaseClass.write_and_save_notepad(app_exe_or_full_exe_path="notepad.exe", text=input,
                                            output_file_name=output_file_path)

        WinBaseClass.verify_csv(input_file_path, output_file_path)
