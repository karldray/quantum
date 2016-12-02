import os


__all__ = ["choice", "fail", "assert_"]


FAILCODE = 55

def choice(xs=(False, True)):
    for x in xs:
        pid = os.fork()
        if pid == 0:
            return x
        _, code = os.waitpid(pid, 0)
        code >>= 8
        if code != FAILCODE:
            os._exit(code)
    fail()

def fail():
    os._exit(FAILCODE)

def assert_(cond):
    if not cond: fail()
