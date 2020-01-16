# Installation

The files Pipfile and Pipfile.lock have been created to ease the installation of the software on the google-colab platform. Python 3.6 should be used, as it is the current version.

## Local installation

To have a local virtual environment, specified by Pipfile.lock mirroring the colab platform environment
```bash
pipenv install --ignore-pipfile
```

## Colab platform update

The pinning of the package versions is complicated by the fact that the package google-colab 1.0.0 may not be the same on PyPi and on the platform, even if they have the same version number. For example, as of 15/01/2020, PyPi's google-colab 1.0.0 requires pandas 0.24.0 whereas the (more up-to-date) package on the platform requires pandas 0.25.0. As a consequence, we cannot rely on pinning the lastest version of the package available in PyPi: we need to pin the google-colab individual dependencies with the version expected on the platform (pandas, requests, six).

When such a package is updated on the platform due to an update of google-colab, the installation procedure on the platform will break. To fix it, the new version should be updated. For example:
```bash
pipenv install pandas==0.26
pipenv lock -r >| requirements.txt
```

## LVC package update
To know which packages can be updated:
```bash
pipenv update --outdated
```
Then, to test a new version of a package:
```bash
pipenv update <package_name>
pipenv lock -r >| requirements.txt
```
