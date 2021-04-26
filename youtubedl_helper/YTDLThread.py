import threading


class StoppableThread(threading.Thread):
    """
    Thread class with a stop() method. The thread itself has to check
    regularly for the stopped() condition.
    """

    def __init__(self, *args, **kwargs):
        super(StoppableThread, self).__init__(*args, **kwargs)
        self._stop_event = threading.Event()

    def stop(self):
        self._stop_event.set()
        print(f"{type(self).__name__} has stopped")

    def stopped(self):
        return self._stop_event.is_set()


def ProgressHook(hook):
    pass


class YDTLThread(StoppableThread):
    def __init__(self, url, options, logger, debug=False):
        super(YDTLThread, self).__init__()

        self.debug = debug

        self.url = url
        self.options = options
        self.options["progress_hooks"] = ProgressHook
        self.logger = logger

    def start(self):
        pass

