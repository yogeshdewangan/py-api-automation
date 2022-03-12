from pywinauto import application
import os


def write_and_save_notepad(app_exe_or_full_exe_path='notepad.exe', text="something", output_file_name="random.csv"):
    app= application.Application()
    app.start(app_exe_or_full_exe_path)
    app.Notepad.Edit.type_keys(text, with_newlines=True, with_tabs=True, with_spaces=True)
    app.Notepad.menu_select("File->SaveAs")
    app.SaveAs.Edit.set_edit_text(output_file_name)
    app.SaveAs.save.click(double=True)
    os.system("TASKKILL /F /IM notepad.exe")

