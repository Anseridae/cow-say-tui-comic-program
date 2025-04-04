import subprocess


if __name__ == '__main__':
    subprocess.Popen(['python', 'panels/panel_1.py'], creationflags=subprocess.CREATE_NEW_CONSOLE)
    subprocess.Popen(['python', 'panels/panel_2.py'], creationflags=subprocess.CREATE_NEW_CONSOLE)
    subprocess.Popen(['python', 'panels/panel_3.py'], creationflags=subprocess.CREATE_NEW_CONSOLE)
    subprocess.Popen(['python', 'panels/panel_4.py'], creationflags=subprocess.CREATE_NEW_CONSOLE)
