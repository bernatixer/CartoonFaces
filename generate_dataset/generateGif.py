import glob
from PIL import Image

# filepaths
# fp_in = "./photos/image_at_epoch_0*.png"
fp_in = "./celeb_raw/0*.jpg"

images = sorted(glob.glob(fp_in))
img, *imgs = [Image.open(f) for f in images]
img.save(fp="./progression_celeb.gif", format='GIF', append_images=imgs, save_all=True, duration=150, loop=0)

# images = sorted(glob.glob(fp_in))[200:400]
# img, *imgs = [Image.open(f) for f in images]
# img.save(fp="./progression2.gif", format='GIF', append_images=imgs, save_all=True, duration=75, loop=0)


# images = sorted(glob.glob(fp_in))[400:600]
# img, *imgs = [Image.open(f) for f in images]
# img.save(fp="./progression3.gif", format='GIF', append_images=imgs, save_all=True, duration=75, loop=0)


# images = sorted(glob.glob(fp_in))[600:]
# img, *imgs = [Image.open(f) for f in images]
# img.save(fp="./progression4.gif", format='GIF', append_images=imgs, save_all=True, duration=75, loop=0)
