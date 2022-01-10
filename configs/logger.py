import qlogging

from configs.constants import LOG_PATH

logger = qlogging.get_logger(level='debug', logfile=LOG_PATH, loggingmode='long', format_date="%(asctime)")
