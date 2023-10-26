import subprocess
import sys
import platform

def install_pyinstaller():
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "pyinstaller"])
    except Exception as e:
        print(f"An error occurred while installing PyInstaller: {e}")
        sys.exit(1)

def create_executable(script_name):
    separator = ";" if platform.system() == "Windows" else ":"
    try:
        subprocess.run([sys.executable, "-m", "PyInstaller", "--onefile", f"--add-data=default_clock.gif{separator}.", script_name])
    except Exception as e:
        print(f"An error occurred while creating the executable: {e}")
        sys.exit(1)

if __name__ == "__main__":
    script_name = "analog_clock.py"
    install_pyinstaller()
    create_executable(script_name)
