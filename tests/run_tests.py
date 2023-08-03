import os
import subprocess

def sayHello():
    print("Hello World")
    output = subprocess.run("sadf", shell=True, capture_output=True, text=True)
    if output.stderr:
        # raise Exception(output.stderr)
        pass
    if output.stdout:
        print(output.stdout)

sayHello()