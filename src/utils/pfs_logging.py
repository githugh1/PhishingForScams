import logging, os

logger = logging.getLogger('PhishingForSpam')

# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s:%(name)s:%(module)s:%(levelname)s:%(funcName)s:\n\t%(message)s')

# setting the log level
log_level = logging.DEBUG
env = os.getenv("PFS_ENVIRONMENT", "development")
# if env == "production":
#     log_level = logging.WARNING

print(f"debugging level is set to {log_level}")

# logging to file
log_file = os.getenv("PFS_LOG_FILE", "")
if log_file:
    fh = logging.FileHandler('log_file')
    fh.setLevel(log_level)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

# logging to console
ch = logging.StreamHandler()
ch.setLevel(log_level)
ch.setFormatter(formatter)
logger.addHandler(ch)

log = logger