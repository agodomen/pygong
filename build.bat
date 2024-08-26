@echo off
:: pip install --user --upgrade setuptools wheel
:: pip install --upgrade twine
:: python -m pip install --user pipenv
:: python -m pip install --index-url https://test.pypi.org/simple/ --no-deps example-package-YOUR-USERNAME-HERE
del /S /Q build
del /S /Q dist
del /S /Q pygong.egg-info
del /S /Q src/pygong/pygong.egg-info
@REM python -m build --wheel
@REM python setup.py sdist build
@REM python setup.py bdist_wheel --universal
python -m build
python -m twine upload --repository testpypi dist/* --skip-existing
python -m twine upload --repository pypi dist/* --skip-existing
:: python -m twine upload --repository testpypi dist/* --skip-existing

