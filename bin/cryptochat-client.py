import sys

def show_error_and_exit(error_text):
    raise NotImplementedError()

def check_requirements():
    raise NotImplementedError()

def setup_logging():
    log = logging.getLogger()

    # If we're running uninstalled and from Git, turn up the logging level
    if uninstalled and devel:
        log.setLevel(logging.INFO)
    else:
        log.setLevel(logging.CRITICAL)

    handler = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s %(levelname)s "
                                  "%(name)s: %(message)s")
    handler.setFormatter(formatter)
    log.addHandler(handler)

if __name__ == '__main__':
    setup_logging()
    import cryptochatclient.cryptochatclientapp

    status = cryptochatclient.app.run()
    sys.exit(status)
