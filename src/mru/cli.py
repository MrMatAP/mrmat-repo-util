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

import sys
import pathlib
import argparse
from cgi import maxlen

from mru import __version__, palette, DEFAULT_FONT_PATH, DEFAULT_FONT_FAMILY, DEFAULT_DIRECTORY, \
  MAX_TITLE_LENGTH, MAX_HEADLINE_LENGTH
from mru.social import social_github_icon, social_jetbrains_icon


def main() -> int:
  parser = argparse.ArgumentParser(add_help=True, description=f'mrmat-repo-util - {__version__}')
  subparsers = parser.add_subparsers(dest='func')

  social_github_icon_parser = subparsers.add_parser('social-github-icon',
                                                    help='Create a GitHub social icon')
  social_github_icon_parser.set_defaults(func=social_github_icon)
  social_github_icon_parser.add_argument('-c', '--colour',
                                         dest='colour',
                                         type=str,
                                         required=False,
                                         default='purple',
                                         choices=palette.keys(),
                                         help='Background color')
  social_github_icon_parser.add_argument('--font-path',
                                         dest='font_path',
                                         type=pathlib.Path,
                                         required=False,
                                         default=DEFAULT_FONT_PATH,
                                         help=f'Path to the font to use. Defaults to {DEFAULT_FONT_PATH}')
  social_github_icon_parser.add_argument('-t', '--title',
                                         dest='title',
                                         type=str,
                                         required=True,
                                         maxlen=MAX_TITLE_LENGTH,
                                         help='Title on the top-left corner')
  social_github_icon_parser.add_argument('--headline',
                                         dest='headline',
                                         type=str,
                                         required=True,
                                         maxlen=MAX_HEADLINE_LENGTH,
                                         help='Headline on the right')
  social_github_icon_parser.add_argument('-d', '--directory',
                                         dest='directory',
                                         type=pathlib.Path,
                                         required=False,
                                         default=DEFAULT_DIRECTORY,
                                         help=f'Directory to save the images to. Defaults to {DEFAULT_DIRECTORY}')

  social_jetbrains_icon_parser = subparsers.add_parser('social-jetbrains-icon',
                                                       help='Create a Jetbrains social icon')
  social_jetbrains_icon_parser.set_defaults(func=social_jetbrains_icon)
  social_jetbrains_icon_parser.add_argument('-c', '--colour',
                                            dest='colour',
                                            type=str,
                                            required=False,
                                            default='purple',
                                            choices=palette.keys(),
                                            help='Background color')
  social_jetbrains_icon_parser.add_argument('--font-family',
                                            dest='font_family',
                                            type=str,
                                            required=False,
                                            default=DEFAULT_FONT_FAMILY,
                                            help=f'Font family to use. Defaults to {DEFAULT_FONT_FAMILY}')
  social_jetbrains_icon_parser.add_argument('-t', '--title',
                                            dest='title',
                                            type=str,
                                            required=True,
                                            maxlen=MAX_TITLE_LENGTH,
                                            help='Title on the top-left corner')
  social_jetbrains_icon_parser.add_argument('--headline',
                                            dest='headline',
                                            type=str,
                                            required=True,
                                            maxlen=MAX_HEADLINE_LENGTH,
                                            help='Headline on the right')
  social_jetbrains_icon_parser.add_argument('-d', '--directory',
                                            dest='directory',
                                            type=pathlib.Path,
                                            required=False,
                                            default=DEFAULT_DIRECTORY,
                                            help=f'Directory to save the images to. Defaults to {DEFAULT_DIRECTORY}')
  parsed_args = parser.parse_args(sys.argv[1:])
  try:
    if parsed_args.func is not None:
      return parsed_args.func(parsed_args)
    parser.print_help()
  except KeyboardInterrupt:
    pass
  return 1


if __name__ == "__main__":
  sys.exit(main())
