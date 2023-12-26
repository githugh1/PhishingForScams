__all__ = [
    "email_parser",
    "q",
    "ai",
    "utils"
]

__version_file__ = './VERSION'

__version__ = ""
with open(__version_file__) as version_file:
    __version__ = version_file.read().strip()