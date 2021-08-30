# Chandra Data Science 3ML Tutorial (*Under Construction!*)
A tutorial for the [Chandra data science meeting](https://cxc.harvard.edu/cdo/cds2021/)

This tutorial covers the basics of:

1) model building and fitting in 3ML
2) x-ray analysis with the OGIPLike plugin
3) advanced examples with joint fits of different plugins and advanced models

Examples make use of both Bayesian and maximum likelihood fitting techinques with a variety of packages. By the end of the tutorial you should have a basic idea of how to import x-ray data into 3ML, build models, perform fits, and save the results of an analysis to disk for distribution. 


## Running the tutorial

There are three ways you can run the tutorial ranging from easy to less easy.

### Easy (Binder)

The tutorials live on a pre-built binder which has all the software installed and all the data needed already available. Just click the binder link below.

You can launch the binder here:
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/threeML/binder_env/master?urlpath=git-pull?repo=https://github.com/threeML/cds_tutorial)

### Easy and Local (Docker)

You can install the 3ML notebook docker with the following instructions.

1) To run this docker first pull it

```bash
docker pull threeml/notebook:latest
```

2) Now clone this repo in a directory of your choosing:

```bash 
git clone https://github.com/threeML/cds_tutorial.git
cd cds_tutorial
```


3) Now you activate the docker with this command (note your choice of local port, here 8008)

```bash
docker run -it --rm -p 8008:8888 -v $PWD:/workdir -w /workdir threeml/notebook
```

then paste `localhost:8008` in your browser and you are all set.


### Advanced (install 3ML and dependencies)

Please do this before the tutorial. You can follow the installation instructions for 3ML and astromodels [here](https://threeml.readthedocs.io/en/latest/notebooks/installation.html)

You can go with conda or pip, but I recommend some form of virtualenv to isolate your install. 

If you go with conda, please use this enironment file:

```yaml
name: threeml
channels:
  - conda-forge
  - threeml
  - xspecmodels
  - fermi
dependencies:
  - astropy<4.3
  - numpy
  - scipy
  - ultranest
  - pygmo
  - fermitools
  - fermipy
  - matplotlib
  - dill
  - pandas
  - astromodels
  - threeml
  - xspec-modelsonly
  - root==6.22
  - pip
  - pip:
      - twopc
      - jupyterthemes
      - gbmgeometry
      - gbm_drm_gen
      - root_numpy

```
to ensure that you have all the required pacakges. Thus,

```bash 
conda env create -f environment.yml
conda activate threeml
```
If you decided to go with pip, you will need to have all the external components you wish to use for the tutorials already installed. 3ML will warn you of things that are missing, e.g., multinest, ROOT, etc. You will also need to have a working installation of XSPEC installed if you wish to demo models comming from XSPEC. The tutorials can be run without these extra components. And you can always try them in the binder link above. 

After installation, you can download the tutorial notebooks and start jupyter with:

```bash 
git clone https://github.com/threeML/cds_tutorial.git
cd cds_tutorial
```

## Questions

If you have questions, please post them as issues in this repo or email me jburgess@mpe.mpg.de


