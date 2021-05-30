from cx_Freeze import setup, Executable

base = None    

executables = [Executable("vaccine_notifier.py", base=base)]

packages = ["requests", "time", "playsound"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "Vaccine Notifier",
    options = options,
    version = "v1.0",
    description = 'A simple program that notifies you when a vaccines are avilable in your area',
    executables = executables
)