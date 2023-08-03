import os
import subprocess

def sayHello():
    print("Hello World")
    output = subprocess.run(" ".join(["ls" "-la"]), shell=True, capture_output=True, text=True)
    if output.stderr:
        raise Exception(output.stderr)
    if output.stdout:
        print(output.stdout)

sayHello()