from logging import getLogger
import os 
import sys

logger = getLogger(__name__)

def debug_requests(f):

    def inner(*args, **kwargs):
        try:
            logger.info(f'\nTRYING TO USE:\t {f.__name__}\n')
            return f(*args, **kwargs)
        except Exception:
            logger.exception(f'Shit happend with {f.__name__}')
            raise

    return inner






def load_config():
    conf_name = os.environ.get("TG_CONF")
    if conf_name is None:
        conf_name = "development"
    try:
        return logger.debug("Loaded config \"{}\" - OK".format(conf_name))
    except (TypeError, ValueError, ImportError):
        logger.error("Invalid config \"{}\"".format(conf_name))
        sys.exit(1)