# MRE for Sphinx regression(?) under Python 3.12.4

- install `pyenv` globally
- install `tox` globally
- install 3.12.3 and 3.12.4 from pyenv
- build the docs using these two python versions


```
pyenv install 3.12.3
pyenv install 3.12.4
tox -e docs-3.12.3  # OK
tox -e docs-3.12.4  # Error
```

Docs are built successfully under Python 3.12.3.

There's an error under Python 3.12.4:

```
/code/operator/ops/model.py:docstring of ops.model.Container.pull:1: WARNING: py:class reference target not found: PurePath
/code/operator/ops/model.py:docstring of ops.model.Container.pull:1: WARNING: py:class reference target not found: PurePath
```

The code in question looks like this:

```py
import typing
from pathlib import PurePath
from typing import BinaryIO, Optional, TextIO, Union

class Container:
    """blah"""

    # The `path` argument type, in the type overload specifcally is broken under py 3.12.4
    @typing.overload
    def pull(self, path: Union[str, PurePath], *, encoding: str = 'utf-8') -> TextIO: ...

    # This, however is OK
    def pull(self, path: Union[str, PurePath], *, encoding: Optional[str] = 'utf-8'):
        """blah. body removed, not needed by sphinx"""
        pass
```

Note that `PurePath` is resolved correctly in other uses in the same file.

The pinned dependencies are the same.
