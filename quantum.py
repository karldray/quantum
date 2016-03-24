import os


__all__ = ["choice", "fail", "assert_"]


ANSWER = 42

def choice(xs):
    for x in xs:
        pid = os.fork()
        if pid == 0:
            return x
        _, code = os.waitpid(pid, 0)
        code >>= 8
        if code != ANSWER:
            os._exit(code)
    fail()

def fail():
    os._exit(ANSWER)

def assert_(cond):
    if not cond: fail()
