r"""Test the Paste Call command
"""

import os
import os.path
from subprocess import Popen, PIPE
import sys

paster = os.path.join(sys.exec_prefix, 'bin', 'paster')
config = os.path.join(os.path.dirname(__file__), 'testapp.cfg')

def test_call():
    r"""Test paste call entry point

        >>> p = Popen(paster + ' call tests:afoo', shell=True,
        ...     stdout=PIPE, stderr=PIPE)
        >>> stdout, stderr = p.communicate()
        >>> print stderr
        <BLANKLINE>
        >>> print stdout
        I enter
        I leave
        <BLANKLINE>

    We can give parameters to functions

        >>> p = Popen(paster + ' call tests:afoo "ho ho" boy',
        ...     shell=True, stdout=PIPE, stderr=PIPE)
        >>> stdout, stderr = p.communicate()
        >>> print stderr
        <BLANKLINE>
        >>> print stdout
        I enter
        I say ho ho, boy!
        I leave
        <BLANKLINE>

    If the function returns any output, PasteCall will print it to stdout

        >>> p = Popen(paster + ' call tests:areturningfoo',
        ...     shell=True, stdout=PIPE, stderr=PIPE)
        >>> stdout, stderr = p.communicate()
        >>> print stderr
        <BLANKLINE>
        >>> print stdout
        I will return!
        <BLANKLINE>
        
    """

def test_with_config():
    r"""Test config load before the entry point execution

        >>> ep = 'tests.testapp:exec_in_environ'
        >>> p = Popen('%s call %s --with-config=%s' % (paster, ep, config),
        ...     shell=True, stdout=PIPE, stderr=PIPE)
        >>> stdout, stderr = p.communicate()
        >>> print stderr
        <BLANKLINE>
        >>> print stdout
        Working in app status initialized
        Using db: sqlite:///:memory:
        <BLANKLINE>

    You can also give parameters

        >>> ep = 'tests.testapp:exec_in_environ'
        >>> p = Popen('%s call %s --with-config=%s Opening' % (paster, ep,
        ...     config), shell=True, stdout=PIPE, stderr=PIPE)
        >>> stdout, stderr = p.communicate()
        >>> print stderr
        <BLANKLINE>
        >>> print stdout
        Working in app status initialized
        Opening db: sqlite:///:memory:
        <BLANKLINE>
    """
