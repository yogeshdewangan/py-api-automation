import pytest

from base.win_base.baseClass import WinBaseClass


class TestCreateUsers(WinBaseClass):

    @pytest.mark.Smoke
    def test_write_notepad_compare_csv(self):
        WinBaseClass.write_and_save_notepad(app_exe_or_full_exe_path="notepad.exe", text="Yogesh,Bangalore",
                                            output_file_name="data_output.csv")
