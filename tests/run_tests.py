import os
import subprocess

def sayHello():
    print("Hello World")
    print("::warning ::This warning is inside python file")
    print("::warning::This is the second warning from python file")
    output = subprocess.run("sadf", shell=True, capture_output=True, text=True)
    if output.stderr:
        # raise Exception(output.stderr)
        pass
    if output.stdout:
        print(output.stdout)

sayHello()
