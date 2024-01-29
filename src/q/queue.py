from abc import ABC
import os


class queue(ABC):
    """This is a abstract class representing an interface to a queueing fabric.

    queue derives python `ABC` class and it's metadata to define two main
    methods to implement a queue:
       - **read**: to read information from the queueing fabric
       - **write**: to write information to the queueing fabric

    #### Attributes:
       - **name** (str): queue fabric interface name. This can be set using env var {envvar}`PFS_Q_NAME`
       - **q** (obj | None): queueing object (implementation specific)

    #### Environment Variables:
       - {envvar}`PFS_Q_NAME`
            environment variable to set the name of the queue (default: 'DEFAULT')
    
    #### Raises:
       - {class}`QException`: exception when errors are detected. 
    """

    @classmethod
    def __init__(self):
        '''Constructor method
        '''

        # read environement variables and instantiate the queue object here!
        self.name: str = os.getenv('PFS_Q_NAME', 'DEFAULT')
        '''the name of the queue as set using {envvar}`PFS_Q_NAME` (default: 'DEFAULT') '''
        self.q: object = None
        '''queueing object (implementation specific)'''

    
    @classmethod
    def read(self, block: bool = True) -> object | None:
        """Returns an item from the queue.
        
        This method will block by default for synchronous retrieval of item 
        until an item is available in the queue.
        
        :param bool block: if `True` block until a message is read (synchronous reading). (default: True)

        :returns (object | None): An item from the queue. Usually a dict or json encoded string where the encoding is queue specific
        
        """
        return None
    
    @classmethod
    def write(self, item: object | None = None) -> bool:
        """Writes an item to the queue.
        
        The queue parameters should be assigned during the class initialisation.

        :param (object | None) item: A queue item, Usually a dict or json encoded string where the encoding is queue specific

        :returns  bool: `True` if successful, otherwise `False`

        """
        return False


class QException(Exception):
    """Implements a simple exception for capturing {py:class}`queue` raised exceptions
    """
    pass
