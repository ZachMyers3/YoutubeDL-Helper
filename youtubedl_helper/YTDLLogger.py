class YTDLLogger(object):
    """
    Generic object to pass to youtube dl
    Currently only passing error messages to stdout
    """

    def debug(self, _):
        pass

    def warning(self, _):
        pass

    def error(self, msg):
        print(msg)
