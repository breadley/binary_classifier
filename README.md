Requires linux

### Purpose

Train a basic classifier to test on histology images from the GDAC

Steps:
1. Curate images
2. Zip to google drive
3. Load to crestle.ai instance
4. Train, generate weights
5. Upload weights to AWS S3 bucket
6. Flask app to load weights and classify images
7. Lambda instance to host flask app

### Pytorch Installation

pip install numpy torchvision_nightly
pipenv run pip install torch_nightly -f https://download.pytorch.org/whl/nightly/cpu/torch_nightly.html

(the above works, although `pipenv lock` fails
