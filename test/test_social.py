from argparse import Namespace

from mru import DEFAULT_FONT_PATH, DEFAULT_FONT_FAMILY
from mru.social import social_github_icon, social_jetbrains_icon


def test_social_github(test_dir):
    args = Namespace(colour='purple',
                     title='MrMat :: Test',
                     headline='M:T',
                     directory=test_dir,
                     font_path=DEFAULT_FONT_PATH)
    social_github_icon(args)
    img_path = test_dir.joinpath('social-github.png')
    assert img_path.exists()

def test_social_jetbrains(test_dir):
  args = Namespace(colour='yellow',
                   title='MrMat :: Test',
                   headline='M:T',
                   directory=test_dir,
                   font_family=DEFAULT_FONT_FAMILY)
  social_jetbrains_icon(args)
  img_path = test_dir.joinpath('social-jetbrains.svg')
  assert img_path.exists()
