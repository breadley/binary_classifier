[inspiration](https://github.com/CancerDataScience/SCNN)

### Purpose

We aim to train a basic classifier to test on histology images from the GDC

Steps:
1. Curate images
2. Zip to google drive
3. Load to crestle.ai instance
4. Train, generate weights
5. Upload weights to AWS S3 bucket
6. Flask app to load weights and classify images
7. Lambda instance to host flask app

## Curate images
Inspired by [this paper](https://github.com/CancerDataScience/SCNN)

### Either by downloading the Docker image with the curated tiles
Install docker, then `docker pull cancerdatascience/scnn:1.0` 

### Or by manually getting the whole slide images from GDC
First we download [GDC case manifest](https://portal.gdc.cancer.gov/legacy-archive/search/f?filters=%7B%22op%22:%22and%22,%22content%22:%5B%7B%22op%22:%22in%22,%22content%22:%7B%22field%22:%22files.data_format%22,%22value%22:%5B%22SVS%22%5D%7D%7D%5D%7D)

Then extract the files that are relevant
`cut -d$'\t' -f 2 gdc_manifest.txt | grep -E '\.*-DX[^-]\w*.'1`

Then use the [GDC api](https://gdc.cancer.gov/developers/gdc-application-programming-interface-api) to download the relevant images

Then curate the images manually or with the script provided in the docker


## Zip to google drive

## Load to [crestle](crestle.ai) instance

## Train, generate weights

## Upload weights to AWS S3 bucket

## Flask app to load weights and classify images

## Lambda instance to host flask app

## Installation / requirements
Fastai v1.0 requires linux because it uses pytorch v1.0

`pip install numpy torchvision_nightly`
`pipenv run pip install torch_nightly -f https://download.pytorch.org/whl/nightly/cpu/torch_nightly.html`
`pipenv instal fastai`

(the above works, although `pipenv lock` fails)
