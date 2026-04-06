from loguru import logger

def inform(message):
    logger.opt(raw=True, colors=True).info(f"<light-blue>[INFO] {message}</light-blue>\n")

def inform_error(message):
    logger.opt(raw=True, colors=True).info(f"<light-red>[ERROR] {message}</light-red>\n")

def inform_file(message):
    logger.opt(raw=True, colors=True).info(f"<fg 117>[FILE]===> {message}</fg 117>\n")


def inform_warning(message):
    logger.opt(raw=True, colors=True).info(f"<light-yellow>[WARNING] {message}</light-yellow>\n")


def inform_ok(message):
    logger.opt(raw=True, colors=True).info(f"<light-green>[ERROR] {message}</light-green>\n")