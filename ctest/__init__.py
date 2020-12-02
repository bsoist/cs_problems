import check50
import check50.c

@check50.check()
def grades0_exists():
    filename = 'grades0.c'
    """%s exists.""" % filename
    check50.exists(filename)

@check50.check()
def grades1_exists():
    filename = 'grades1.c'
    """%s exists.""" % filename
    check50.exists(filename)

@check50.check()
def powers_exists():
    filename = 'powers.c'
    """%s exists.""" % filename
    check50.exists(filename)

@check50.check()
def while_exists():
    filename = 'while.c'
    """%s exists.""" % filename
    check50.exists(filename)


