# MrMat :: Repository Utility

A utility to manage code repositories.

[![Build](https://github.com/MrMatAP/mrmat-repo-util/actions/workflows/build.yml/badge.svg)](https://github.com/MrMatAP/mrmat-repo-util/actions/workflows/build.yml)

## How to install this

Download the wheel from the releases page on GitHub or build it locally as per the interactive build section below. It
is recommended to install the tool in some virtual environment.

```shell
$ python -m venv /path/to/venv
$ pip install /path/to/downloaded/wheel
```

## How to use this

This is a utility for managing repositories in GitHub and Gitlab and the Jetbrains suite of IDEs. At this time, it
only has two implemented functions, to generate the social media icons in GitHub and a custom project icon for the 
Jetbrains suite of ideas. There's limited means to customise those icons for now, they're the way I like them to be.

### Getting help

A simple command help system is provided.

```shell
$ mrmat-repo-util -h
usage: mrmat-repo-util [-h] {social-github-icon,social-jetbrains-icon} ...

mrmat-repo-util - 0.0.0.dev0

positional arguments:
  {social-github-icon,social-jetbrains-icon}
    social-github-icon  Create a GitHub social icon
    social-jetbrains-icon
                        Create a Jetbrains social icon

options:
  -h, --help            show this help message and exit
```

### social-github-icon

The tool will a social icon you can upload to GitHub in PNG format at a size of 1280x640px. The icon features
a title of a maximum of 13 characters on the top-left and a headline of a maximum of 4 characters on the bottom right.

```shell
$ mrmat-repo-util social-github-icon -h
usage: mrmat-repo-util social-github-icon [-h] [-c {purple,red,orange,yellow,blue}] [--font-path FONT_PATH] -t TITLE --headline HEADLINE [-d DIRECTORY]

options:
  -h, --help            show this help message and exit
  -c {purple,red,orange,yellow,blue}, --colour {purple,red,orange,yellow,blue}
                        Background color
  --font-path FONT_PATH
                        Path to the font to use. Defaults to /System/Library/Fonts/HelveticaNeue.ttc
  -t TITLE, --title TITLE
                        Title on the top-left corner
  --headline HEADLINE   Headline on the right
  -d DIRECTORY, --directory DIRECTORY
                        Directory to save the images to. Defaults to /Users/imfeldma/build

$ mrmat-repo-util social-github-icon -c purple -t "RepoUtil" --headline RU
Generated GitHub social icon at /Users/imfeldma/build/social-github.png
```

![GitHub Social Icon](var/images/social-github.png)

# social-jetbrains-icon

You can create a project icon for Jetbrains IDEs in SVG format. The icon has a 1024x1024 pixel size. The icon features
a title of a maximum of 13 characters on the top-left and a headline of a maximum of 4 characters on the bottom right.

```shell
$ mrmat-repo-util social-jetbrains-icon -h
usage: mrmat-repo-util social-jetbrains-icon [-h] [-c {purple,red,orange,yellow,blue}] [--font-family FONT_FAMILY] -t TITLE --headline HEADLINE [-d DIRECTORY]

options:
  -h, --help            show this help message and exit
  -c {purple,red,orange,yellow,blue}, --colour {purple,red,orange,yellow,blue}
                        Background color
  --font-family FONT_FAMILY
                        Font family to use. Defaults to Helvetica
  -t TITLE, --title TITLE
                        Title on the top-left corner
  --headline HEADLINE   Headline on the right
  -d DIRECTORY, --directory DIRECTORY
                        Directory to save the images to. Defaults to /Users/imfeldma/build

$ mrmat-repo-util social-jetbrains-icon -c purple -t "RepoUtil" --headline RU
Generated Project icon at /Users/imfeldma/build/social-jetbrains.svg
```

![IDEA/Gitlab Icon](var/images/social-jetbrains.svg)

## How to build this

### Interactively

The general sequence for building interactively is to install the necessary dependencies and build a wheel:

```shell
$ pip install -r requirements.dev.txt
$ pip install -r requirements.txt
$ PYTHONPATH=$(pwd)/src python -m build -n --wheel
```

> Modifying the PYTHONPATH is necessary so the dynamic version in `src/ci` can be found during the build process.

An interactive build will default its version to '0.0.0.dev0', which is a relevant piece of information telling us that
this was not a build that was produces in a (slightly) more trusted CI environment. Builds produced within a CI context
have 'real' version numbers based on the build number injected by GitHub.

### CI

GitHub Actions will trigger a build upon a push and as part of a pull request. If the build is the result of a merge 
onto the merge branch then it is considered to be a release build, which will cause a tag to be created. The version 
is suffixed with '.dev0' for any non-release build.

The build version is relayed via the 'MRMAT_VERSION' environment variable from the 'MAJOR', 'MINOR' operational 
variables as well as the 'GITHUB_RUN_NUMBER'. 'MAJOR' and 'MINOR' are meant to be adjusted manually because those are 
conscious version bumps that are expected to happen far less frequently than individual builds. The 'GITHUB_RUN_NUMBER' 
is injected by GitHub Actions itself, resulting in a discrete version of the product for each build.

The version constructed at build time is relayed by using a Python module in src/ci, which is referred to by 
pyproject.toml and explicitly excluded from the resulting distribution. Pythons importlib.metadata is then used in the 
top-level __init__.py for relaying the version into the runtime.

## Limitations

* It is not currently possible to specify custom colours beyond the hardcoded palette
* PNG and Pillow need the path to a TrueType font, SVG wants the name of the font face. It would be nice not having to specify the font twice
* We might as well use the GitHub/Gitlab APIs to upload the images directly instead of storing them locally
