import typing
from pathlib import PurePath
from typing import BinaryIO, Optional, TextIO, Union

class Container:
    """blah"""

    # The `path` argument type, in the type overload specifcally is broken under py 3.12.4
    @typing.overload
    def pull(self, path: Union[str, PurePath], *, encoding: str = 'utf-8') -> TextIO: ...

    def pull(self, path: Union[str, PurePath], *, encoding: Optional[str] = 'utf-8'):
        """blah. body removed, not needed by sphinx"""
        pass
