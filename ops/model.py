import typing
from pathlib import PurePath
from typing import BinaryIO, Optional, TextIO, Union

class Container:
    """blah"""

    @typing.overload
    def pull(self, path: Union[str, PurePath], *, encoding: None) -> BinaryIO: ...

    @typing.overload
    def pull(self, path: Union[str, PurePath], *, encoding: str = 'utf-8') -> TextIO: ...

    def pull(
        self, path: Union[str, PurePath], *, encoding: Optional[str] = 'utf-8'
    ) -> Union[BinaryIO, TextIO]:
        """blah. body removed, not needed by sphinx"""
        pass
