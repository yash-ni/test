import os
import subprocess

def sayHello():
    print("Hello World")
    warning = "::warning::" + "This is a warning"
    print(warning)
    print("::warning::This is the second warning from python file")
    output = subprocess.run("sadf", shell=True, capture_output=True, text=True)
    if output.stderr:
        # raise Exception(output.stderr)
        pass
    if output.stdout:
        print(output.stdout)

sayHello()
