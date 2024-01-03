import logging
import os

_logger = logging.getLogger('PhishingForSpam')

# create formatter and add it to the handlers
_formatter = logging.Formatter('%(asctime)s:%(name)s:%(module)s: \
                              %(levelname)s:%(funcName)s:\n\t%(message)s')

# setting the log level
log_level: int = logging.DEBUG
''' logging level is set to _WARNING_ for **production** 
    environment, otherwise _DEBUG_     
'''


env: str = os.getenv("PFS_ENVIRONMENT", "development")
''' the environment can be set using env var {envvar}`PFS_ENVIRONMENT` (Default: development)'''

if env == "production":
    log_level = logging.WARNING

print(f"debugging level is set to {log_level}")

# logging to file
_log_file = 'pfs_log_file.log' if env != 'production' else ''
log_file: str = os.getenv("PFS_LOG_FILE", _log_file)
''' a log file can be set using env var {envvar}`PFS_LOG_FILE` in production (Default: not set!).

    if the environment is not production, then by default logs will be writted to *pfs_log_file.log*
'''

if log_file != "":
    fh = logging.FileHandler(log_file)
    fh.setLevel(log_level)
    fh.setFormatter(_formatter)
    _logger.addHandler(fh)

# logging to console
_con = logging.StreamHandler()
_con.setLevel(log_level)
_con.setFormatter(_formatter)
_logger.addHandler(_con)

log: logging.Logger = _logger
'''
    python logger
'''