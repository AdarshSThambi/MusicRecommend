from bing_image_downloader import downloader
from PIL import Image

query_string = "shape of you sheeran"
output_dir = 'dataset'
# downloader.download(query_string, limit=1, output_dir=output_dir, adult_filter_off=True, force_replace=False,
#                     timeout=20, verbose=True)
im1 = Image.open('/'.join([output_dir,query_string,'Image_1.jpg']))
im1.show()
