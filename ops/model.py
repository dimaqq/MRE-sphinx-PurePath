import typing
from pathlib import PurePath
from typing import BinaryIO, Optional, TextIO, Union

class Container:
    """blah"""

    # This is OK (assuming intersphinx is set up)
    def another(self, path: Union[str, PurePath], *, encoding: Optional[str] = 'utf-8'):
        """a docstring"""

    # In the type overload specifically, the `path` argument type is broken under py 3.12.4
    @typing.overload
    def pull(self, path: Union[str, PurePath], *, encoding: str = 'utf-8') -> TextIO: ...

    # Sphinx seems to ignore this signature if there is a type overload
    def pull(self, path: Union[str, PurePath], *, encoding: Optional[str] = 'utf-8'):
        """a docstring"""
