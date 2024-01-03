__all__: list[str] = [
    "email_parser",
    "q",
    "ai",
    "utils"
]
'''
    exported packages
'''

import os

__version_file__: str = f"{os.path.dirname(os.path.abspath(__file__))}/../VERSION"
''' location of the version file

    This is set at the project top level with filename _VERSION_
'''

__version__: str = ""
''' the version of this release

    The content is read from the {py:data}`_VERSION_ <__version_file__>` file
'''
with open(__version_file__) as version_file:
    __version__ = version_file.read().strip()