@echo off
:: pip install --user --upgrade setuptools wheel
:: python -m pip install --user pipenv
:: python -m pip install --index-url https://test.pypi.org/simple/ --no-deps example-package-YOUR-USERNAME-HERE
del /S /Q build
del /S /Q dist
del /S /Q pygong.egg-info
python -m build --wheel
python setup.py sdist build
python setup.py bdist_wheel --universal
python -m twine upload --repository testpypi dist/* --skip-existing
:: python -m twine upload --repository testpypi dist/* --skip-existing

