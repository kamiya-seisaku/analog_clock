import subprocess
import sys
+ import platform

def install_pyinstaller():
    ...

def create_executable(script_name):
+   separator = ";" if platform.system() == "Windows" else ":"
    try:
-       subprocess.run([sys.executable, "-m", "PyInstaller", "--onefile --add-data", script_name])
+       subprocess.run([sys.executable, "-m", "PyInstaller", "--onefile", f"--add-data=default_clock.gif{separator}.", script_name])
    except Exception as e:
        ...

if __name__ == "__main__":
    ...
