import pytest, os

from base.win_base.baseClass import WinBaseClass
from modules import other

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
input_file_path = os.path.join(ROOT_DIR, "inputs\data.csv").replace("tests\\", "")
output_file_path = os.path.join(ROOT_DIR, "outputs\data.csv").replace("tests\\", "")


class TestNotepadAndCompareCSV(WinBaseClass):

    @pytest.mark.Smoke
    def test_write_notepad_compare_csv(self,setup):

        input_str = other.normalize(str(open(input_file_path, "r").readlines()))

        # WinBaseClass.write_and_save_notepad(app_exe_or_full_exe_path="notepad.exe", text=input_str,
        #                                     output_file_name=output_file_path)

        WinBaseClass.verify_csv(input_file_path, output_file_path)
