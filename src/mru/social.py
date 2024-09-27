import argparse

from PIL import Image, ImageDraw, ImageFont

from mru import console, palette


def social_github_icon(args: argparse.Namespace):
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
  github_social_icon_file = args.directory.joinpath('social-github.png')
  with open(github_social_icon_file, mode='wb') as f:
    out.save(f, format='PNG')
  console.print(f'Generated GitHub social icon at {github_social_icon_file}')


def social_jetbrains_icon(args: argparse.Namespace):
  colour = palette[args.colour]
  svg_icon = f'''
  <svg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'
       version='1.1'
       viewbox='0 0 1024 1024'
       width='1024'
       height='1024'>
    <rect width="1024px" height="1024px" fill="{colour['bg']}" />
    <text x='20' y='140'
          font-size='10em'
          font-family='{args.font_family}'>{args.title}</text>
    <text x='1000' y='950'
          text-anchor='end'
          font-size='20em'
          font-family='{args.font_family}'>{args.headline}</text>
  </svg>
  '''
  project_icon_file = args.directory.joinpath('social-jetbrains.svg')
  project_icon_file.write_text(svg_icon, encoding='utf-8')
  console.print(f'Generated Project icon at {project_icon_file}')
