# test repo

The sole purpose of this repo is to reproduce issue with prefect tasks not being picked by autodoc module when given a name and`sphinxcontrib-prefecttask` extension being installed

Steps to reproduce after clonning this repo:

    pip install -e '.[docs]'
    cd docs
    make html

Navigate to `docs/build/api/code.html`
