import pytest

import pathlib

@pytest.fixture
def test_dir():
  d = pathlib.Path(__file__).parent.parent.joinpath('build').joinpath('test')
  d.mkdir(exist_ok=True, parents=True)
  yield d
