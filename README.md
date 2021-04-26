# YoutubeDL Helper

## Description

Helper python script to ease automation with Youtube DL

## Features

* TODO

## Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and [this](http://gitlab.woosterbrush.com/zachmyers/cookiecutter-python-package) project template.

## Running Development Application

```bash
# install dependencies
$ poetry install
# run application cli interface without script
$ poetry run python youtubedl-helper/cli.py --help
```

## Running Tests Using Pytest

```bash
# install dependencies (if needed)
$ poetry install
# run pytest through poetry
$ poetry run pytest
```

## Building CLI Executable

```bash
# run build script, pyinstaller is required
$ ./scripts/build.ps1
```

<<<<<<< HEAD
An executable should then be available at ```./dist/youtubedl-helper/youtubedl-helper.exe```

## Publishing Package to Local PyPi

```bash
# add the local pypi repository to poetry
$ poetry config repositories.wbc http://pypi.dokku2.woosterbrush.com/
# build the wheels for publishing
$ poetry build
# publish to pypi specifying our new repository
$ poetry publish -r wbc
```

You can verify the list of packages after deployment [here](http://pypi.dokku2.woosterbrush.com/packages/).
=======
An executable should then be available at ```./dist/youtubedl-helper/youtubedl-helper.exe
>>>>>>> more qol changes
