# pyucn

This is a Python wrapper for the [IUCN Red List API](https://apiv3.iucnredlist.org/api/v3/docs).

I should have implemented all of the endpoints listed on the API website, but there may be
some missing.

## install

This package should work on any `Python >= 3.6`. You can install it using `pip` by running:
```
--editable=git+https://github.com/barnabywalker/pyucn.git#egg=pyucn
```

This should install directly from this repo.

The package includes a `html` progress bar for using in Jupyter notebooks. At some point it would
make sense for me to just replace this with `tqdm`.

To make the progress bar widget work, you need to:
1. install nodejs
```
conda install nodejs
```

2. install widget extension
```
jupyter labextension install @jupyter-widgets/jupyterlab-manager
```
