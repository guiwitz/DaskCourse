Small dataset
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/guiwitz/DaskCourse/ef17335d978b5ecbbeed052dc671a0ca599252d1?urlpath=lab)

Large dataset
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/guiwitz/DaskCourse/03c7b6f20a5f49156f63822778c2685571667a89?urlpath=lab)


# Introduction to Dask

This is the material used for the course "Scalable analytics with Python (DASK)" given by Science IT Support at Bern University. You can test the notebooks using the binder badge, but several datasets are not included due to their size.

## Local installation

Installation is based on conda. If you don't have conda installed yet, the simplest is to install it using [miniconda](https://docs.conda.io/en/latest/miniconda.html).

In order to install all necessary packages on your laptop or on a cluster, first clone this repository:

```
git clone https://github.com/guiwitz/DaskCourse.git
```

Then use [this environment.yml](/binder/environment.yml) file to create a dedicated conda environment:
```
conda env create -f environment.yml
```

If you want to use JupyterLab, also install the necessary extensions:
```
conda activate dask_course
jupyter labextension install dask-labextension --no-build
jupyter labextension install @jupyter-widgets/jupyterlab-manager --no-build
jupyter labextension install @bokeh/jupyter_bokeh --no-build
jupyter lab build --minimize=False
jupyter serverextension enable dask_labextension
```

Finally you can download all necessary data using the script [download_all.py](/installation/download_data.py):

```
conda activate dask_course
python download_data.py
```
