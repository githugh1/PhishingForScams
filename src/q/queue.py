from abc import ABC
import os

class queue(ABC):
    """This is a abstract class representing an interface to a queueing fabric.
    
    queue derives python `ABC` class and it's metadata to define two main methods
    to implement a queue:
    - **read** to read information from the queueing fabric
    - **write** to write information to the queueing fabric

    Attributes:
        name (str): queue fabric interface name. This can be set using env var `[PFS_Q_NAME](#pfs-q-name)`
        q (obj | None): queueing object (implementation specific)

    Environment Variables:
        {#pfs-q-name}
        PFS_Q_NAME: environment variable to set the name (default: 'DEFAULT')
    
    Raises:
        QException: 
    """

    @classmethod
    def __init__(self):
        '''Constructor method
        '''

        # read environement variables and instantiate the queue object here!
        self.name = os.getenv('PFS_Q_NAME', 'DEFAULT')
        self.q = None
    
    @classmethod
    def read(self, block=True):
        """Returns an item from the queue. This method will block by default for synchronous retrieval of item.
            This function will block until an item is available in the queue.
        
        Args:
            block (bool): if `True` block until a message is read (synchronous reading). (default: True)

        Returns:
            obj: An item from the queue. Usually a dict or json encoded string where the encoding is queue specific
        
        """
        return None
    
    @classmethod
    def write(self, item=None):
        """Writes an item to the queue. The queue parameters should be assigned during init.

        Args:
            item (obj | None): A queue item, Usually a dict or json encoded string where the encoding is queue specific

        Returns:
            bool: `True` if successful, otherwise `False`

        """
        return False


class QException(Exception):
    """Implements a simple exception for capturing {py:class}`queue` raised exceptions
    """
    pass