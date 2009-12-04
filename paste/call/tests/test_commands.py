r"""Test the Paste Call command
"""

import os
import os.path
from subprocess import Popen, PIPE
import sys

paster = os.path.join(sys.exec_prefix, 'bin', 'paster')
config = os.path.join(os.getcwd(), 'paste', 'call', 'tests', 'testapp.cfg')

def test_call():
    r"""Test paste call entry point

        >>> p = Popen(paster + ' call paste.cron.tests:afoo', shell=True,
        ...     stdout=PIPE, stderr=PIPE)
        >>> stdout, stderr = p.communicate()
        >>> print stderr
        <BLANKLINE>
        >>> print stdout
        I enter
        And leave
        <BLANKLINE>
    """

def test_with_config():
    r"""Test config load before the entry point execution

        >>> ep = 'paste.call.tests.testapp:exec_in_environ'
        >>> p = Popen('%s call %s --with-config=%s' % (paster, ep, config),
        ...     shell=True, stdout=PIPE, stderr=PIPE)
        >>> stdout, stderr = p.communicate()
        >>> print stderr
        <BLANKLINE>
        >>> print stdout
        Working in app status initialized
        Using db: sqlite:///:memory:
        <BLANKLINE>
    """