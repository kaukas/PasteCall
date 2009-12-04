
from paste.deploy import loadapp
from paste.script.command import Command
from pkg_resources import EntryPoint


class CallEP(Command):
    min_args = 1

    usage = 'entry.point:foo'
    summary = 'Execute the supplied entry point'

    parser = Command.standard_parser(verbose=True)
    parser.add_option('--with-config', dest='config',
        help='load environment described in this config file')
    
    def command(self):
        r"""Run the actual function.
        """
        ep_str = self.args[0]
        opts = self.options
        ep = EntryPoint.parse('%s=%s' % ('NA', ep_str))
        callable = ep.load(require=False)
        if self.options.config:
            self.load_config(self.options.config)
        callable(*self.args[1:])

    def load_config(self, config):
        self.app = loadapp('config:' + config)
