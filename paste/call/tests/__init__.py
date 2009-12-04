def afoo(what=None, who=None):
    r"""A simple python function to test entry points
    """
    print 'I enter'
    if what and who:
        print 'I say %s, %s!' % (what, who)
    print 'I leave'

def setup():
    pass

def teardown():
    pass
