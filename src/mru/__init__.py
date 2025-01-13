#  MIT License
#
#  Copyright (c) 2022 Mathieu Imfeld
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import importlib.metadata
import pathlib

import rich.console

try:
  __version__ = importlib.metadata.version('mru')
except importlib.metadata.PackageNotFoundError:
  # You have not yet installed this as a package, likely because you're hacking on it in some IDE
  __version__ = '0.0.0.dev0'
console = rich.console.Console()
palette = dict(
  purple=dict(bg='#a8216b', fg='#ffffff'),
  red=dict(bg='#f1184c', fg='#ffffff'),
  orange=dict(bg='#f36943', fg='#262626'),
  yellow=dict(bg='#f7dc66', fg='#262626'),
  blue=dict(bg='#2e9599', fg='#121212')
)
DEFAULT_FONT_PATH = pathlib.Path('/System/Library/Fonts/HelveticaNeue.ttc')
DEFAULT_FONT_FAMILY = "Helvetica"
DEFAULT_DIRECTORY = pathlib.Path('~/build').expanduser()
MAX_TITLE_LENGTH = 13
MAX_HEADLINE_LENGTH = 4
