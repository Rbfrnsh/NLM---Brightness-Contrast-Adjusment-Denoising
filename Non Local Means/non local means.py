


## Denoising filters 
from skimage.restoration import denoise_nl_means, estimate_sigma
from skimage import img_as_ubyte, img_as_float
from matplotlib import pyplot as plt
from skimage import io
import numpy as np
import glob,os




## path yang digunakan 
root_path_testing = 'data/*.jpg' ## di path mana gambar akan di blend
root_path_saving = 'NLM/'  ## dimana gambar akan disave
file_path = glob.glob(root_path_testing)

#make new directory
os.makedirs(root_path_saving, exist_ok = True)

for path in file_path:
    img = img_as_float(io.imread(path))
    img=cv2.imread(path)
    sigma_est = np.mean(estimate_sigma(img, multichannel=True))
    patch_kw = dict(patch_size=5,      
                patch_distance=3,  
                multichannel=True)
    denoise_img = denoise_nl_means(img, h=1.15 * sigma_est, fast_mode=False,
                               patch_size=5, patch_distance=3, multichannel=True)
    # split filename
    filename = path.split('\\')[-1]
    cv2.imwrite(root_path_saving + filename,denoise_img)


