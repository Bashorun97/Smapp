import re

def email_check(str):

    email_reg = re.compile(r'''
        ([a-zA-Z0-9_\-+%]+|[a-zA-Z0-9_\-+%]+(.\.))
        [@]
        [a-zA-Z0-9.-]+
        (\.[a-zA-Z]{2,4})
    ''',re.VERBOSE)
    try:
        if email_reg.search(str):
            return True
        else:
            return False
    except AttributeError:
        raise False