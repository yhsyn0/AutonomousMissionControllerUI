
from subprocess import call
call(["python3", "try2.py"])

from subprocess import Popen
Popen(["python3", "try2.py"])

import inspect

def f1():
    print("Caller is " + inspect.stack()[1][3])


def f2():
    f1()

f2()