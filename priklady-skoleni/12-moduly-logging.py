import logging
import datetime
import getpass	# Pro zjisteni uzivatele

logger = logging.getLogger(__name__)
FORMAT = "%(levelname)-8s [%(asctime)-15s] [%(user)-8s] [%(process)d] [%(funcName)-14s] - %(message)s"

logging.basicConfig(filename='log_{0}.log'.format(
    datetime.date.today()), format=FORMAT)
logger.setLevel("INFO")	# Co reálně logovat
d = {'user': getpass.getuser()}

logger.debug("Podrobne info", extra=d)	# Nezaloguje se
logger.info("Zakladni info", extra=d)	# Zalohuje se
