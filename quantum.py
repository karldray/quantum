import os


_FAILCODE = 55

def choice(xs):
    for x in xs:
        pid = os.fork()
        if pid == 0:
            return x
        _, code = os.waitpid(pid, 0)
        code >>= 8
        if code != _FAILCODE:
            os._exit(code)
    fail()

def fail():
    os._exit(_FAILCODE)

def assert_(cond):
    if not cond: fail()
