# Source: https://github.com/fastai/course-v3/blob/master/nbs/dl1/lesson1-pets.ipynb

from fastai import *
from fastai.vision import *


bs = 64


def download():
    help(untar_data)
    path = untar_data(URLs.PETS)
    print(f'pet files loaded at {path}')
    path_anno = path/'annotations'
    path_img = path/'images'
    fnames = get_image_files(path_img)
    print(f'here are some filenames {fnames[:5]}')
    np.random.seed(2)
    pat = re.compile(r'/([^/]+)_\d+.jpg$')
    data = ImageDataBunch.from_name_re(path_img, 
                                            fnames, 
                                            pat, 
                                            ds_tfms=get_transforms(), 
                                            size=224, 
                                            bs=bs).normalize(imagenet_stats)
    data.show_batch(rows=3, figsize=(7,6))
    print(f'Here are some classes {data.classes}')
    print(f'Number of classes: {len(data.classes),data.c}')

def train_resnet_34():
    help(untar_data)
    path = untar_data(URLs.PETS)
    print(f'pet files loaded at {path}')
    path_anno = path/'annotations'
    path_img = path/'images'
    fnames = get_image_files(path_img)
    print(f'here are some filenames {fnames[:5]}')
    np.random.seed(2)
    pat = re.compile(r'/([^/]+)_\d+.jpg$')
    data = ImageDataBunch.from_name_re(path_img, 
                                            fnames, 
                                            pat, 
                                            ds_tfms=get_transforms(), 
                                            size=224, 
                                            bs=bs,
                                            num_workers=0).normalize(imagenet_stats)
    data.show_batch(rows=3, figsize=(7,6))

    print(f'Here are some classes {data.classes}')
    print(f'Number of classes: {len(data.classes),data.c}')
    print('training now--------------------')
    learn = create_cnn(data, models.resnet34, metrics=error_rate)
    learn.fit_one_cycle(4)
    learn.save('stage_1')

    # Get results
    print('results time')
    interp = ClassificationInterpretation.from_learner(learn)
    inter.plot_top_losses(9, figsize=(15,11))
    doc(interp.plot_top_losses)
    interp.plot_confusion_matrix(figsize=(12,12), dpi=60)
    interp.most_confused(min_val=2)
    
def more_training():
    learn.ufreeze()
    learn.fit_one_cycle(1)
    learn.lr_find()
    learn_recorder.plot()
    learn.unfreeze()
    learn.fit_one_cycle(2, max_lr=slice(1e-6,1e-4))

def train_resnet_50():
    data = ImageDataBunch.from_name_re(path_img, 
                        fnames, 
                        pat, 
                        ds_tfms=get_transforms(),
                        size=299,bs=bs//2,
                        num_workers=0 # I added this to allow the DataLoader to work
                        ).normalize(imagenet_stats)
    learn = creat_cnn(data, models.resent50, metrics=error_rate)
    learn.lr_find()
    learn.recorder.plot()
    learn.fit_one_cycle(8)
    learn.save('stage-1-50')
    learn.unfreeze()
    learn.fit_one_cycle(3, max_lr=slice(1e-6,1e-4))
    learn.oad('stage-1-50')
    interp = ClassificationInterpretation.from_learner(learn)
    interp.most_confused(min_val=2)


if __name__=="__main__":
    train_resnet_34()
