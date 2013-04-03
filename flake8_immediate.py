
__version__ = '0.2'

import pep8


class ImmediateReport(pep8.BaseReport):
    '''Collect and print the results of the checks.'''

    def __init__(self, options):
        super(ImmediateReport, self).__init__(options)
        self._fmt = pep8.REPORT_FORMAT.get(options.format.lower(),
                                           options.format)
        self._repeat = options.repeat
        self._show_source = options.show_source
        self._show_pep8 = options.show_pep8

    def error(self, line_number, offset, text, check):
        '''Report an error, according to options.'''
        code = super(ImmediateReport, self).error(line_number, offset,
                                                  text, check)
        if code and (self.counters[code] == 1 or self._repeat):
            print(self._fmt % {
                'path': self.filename,
                'row': self.line_offset + line_number, 'col': offset + 1,
                'code': code, 'text': text[5:],
            })
        return code


class Immediate(object):

    name = 'flake8-immediate'
    version = __version__

    def __init__(self):
        pass

    @classmethod
    def add_options(cls, parser):
        parser.add_option('--immediate', action='store_true',
                          help='don\'t cache the error output until EOF')

    @classmethod
    def parse_options(cls, options):
        if options.immediate:
            options.report = ImmediateReport(options)
