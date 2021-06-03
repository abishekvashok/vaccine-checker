# vaccine-checker
Light weight Scripts and Apps for checking availability of Covid Vaccines in India. Notifies when vaccine becomes avialable in your area.

## Python script

Command line based program written in python, that continuously checks CoWIN portal based on the specified information
Operating system detailed running instructions are described below.

### Windows

Either [download the latest release](https://github.com/abishekvashok/vaccine-checker/releases/download/0.01/exe.win-amd64-3.9.rar) (https://github.com/abishekvashok/vaccine-checker/releases/download/0.01/exe.win-amd64-3.9.rar), extract it, and run vaccine_checker.exe

Or follow the instructions as same for Linux and MacOS to run the python script.

### Linux and MacOS (running the python script)

#### Downloading

Clone the repo using command line
```
git clone https://github.com/abishekvashok/vaccine-checker/
```
Or, download using the GitHub web interface.

#### Install prerequisites

```
python3 install -r requirements.txt
```

#### Run the script

```
python3 vaccine_checker.py
```

Enter the information, and start checking.

#### Build a executable
Optionally build an executable for your specific system (intended for developers)

```
python3 setup.py build
```
