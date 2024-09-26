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
import xml.etree.ElementTree as ET

import rich.console
from PIL import Image, ImageDraw, ImageFont

from mru import __version__

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


def social_icons(args: argparse.Namespace):
  if len(args.headline) > 4:
    print("Headline must be at most 4 characters long")
    return
  if args.colour not in palette:
    print("You must pick one of the palette colours")
    return
  colour = palette[args.colour]
  out = Image.new("RGB", (1280, 640), color=colour['bg'])
  d = ImageDraw.Draw(out)
  d.text((10, 10),
         args.title,
         font=ImageFont.truetype(args.font_path, 100),
         fill=colour['fg'])
  d.text((1200, 500),
         args.headline,
         font=ImageFont.truetype(args.font_path, 400),
         fill=colour['fg'],
         anchor='rb')
  args.directory.mkdir(exist_ok=True, parents=True)
  github_social_icon_file = args.directory.joinpath('github-social.png')
  with open(github_social_icon_file, mode='wb') as f:
    out.save(f, format='PNG')
  console.print(f'Generated GitHub social icon at {github_social_icon_file}')

  idea_icon = ET.Element('svg', {
    'xmlns': 'http://www.w3.org/2000/svg',
    'xmlns:xlink': 'http://www.w3.org/1999/xlink',
    'version': '1.1',
    'viewbox': '0 0 1024 1024',
    'width': '1024px',
    'height': '1024px',
    'style': f'background-color: {colour["bg"]}'
  })
  title = ET.SubElement(idea_icon, 'text', {
    'x': '10',
    'y': '100',
    'fill': colour['fg'],
    'font-size': '100',
    'font-family': args.font_family,
  })
  title.text = args.title
  headline = ET.SubElement(idea_icon, 'text', {
    'x': '1000',
    'y': '700',
    'fill': colour['fg'],
    'font-size': '400',
    'font-family': args.font_family,
    'text-anchor': 'end'
  })
  headline.text = args.headline
  tree = ET.ElementTree(idea_icon)
  idea_icon_file = args.directory.joinpath('idea-icon.svg')
  tree.write(idea_icon_file)
  console.print(f'Generated icon at {idea_icon_file}')


def main() -> int:
  parser = argparse.ArgumentParser(add_help=True, description=f'mrmat-repo-util - {__version__}')
  subparsers = parser.add_subparsers(dest='func')

  social_icon_parser = subparsers.add_parser('social-icons', help='GitHub Social Icons')
  social_icon_parser.set_defaults(func=social_icons)
  social_icon_parser.add_argument('-c', '--colour',
                                  dest='colour',
                                  type=str,
                                  required=False,
                                  default='purple',
                                  choices=palette.keys(),
                                  help='Background color')
  social_icon_parser.add_argument('--font-path',
                                  dest='font_path',
                                  type=pathlib.Path,
                                  required=False,
                                  default=DEFAULT_FONT_PATH,
                                  help=f'Path to the font to use. Defaults to {DEFAULT_FONT_PATH}')
  social_icon_parser.add_argument('--font-family',
                                  dest='font_family',
                                  type=str,
                                  required=False,
                                  default=DEFAULT_FONT_FAMILY,
                                  help=f'Font family to use. Defaults to {DEFAULT_FONT_FAMILY}')
  social_icon_parser.add_argument('-t', '--title',
                                  dest='title',
                                  type=str,
                                  required=True,
                                  help='Title on the top-left corner')
  social_icon_parser.add_argument('--headline',
                                  dest='headline',
                                  type=str,
                                  required=True,
                                  help='Headline on the right')
  social_icon_parser.add_argument('-d', '--directory',
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
