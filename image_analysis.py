from PIL import Image
import os


class ImageAnalysis:

	containing_dir_path = os.path.dirname(os.path.realpath(__file__))

	# def: fetch list of image names from current dir

	def fetch_image_file_names(self):
		print(self.containing_dir_path)
		for file in os.listdir(''.join([self.containing_dir_path, '/time_covers'])):
		    if file.endswith(".jpeg"):
		        img = Image.open(file)

		return img

	# def: generator to yield each image

	# def: (image data, function) -> analysis output
	# def: color_distribution: gets sorted tuples of rgb frequences


def main():
    # IA = ImageAnalysis()
    
    # print(os.path.dirname(os.path.realpath(__file__)) + 'time_covers' + 'musk.jpeg')
  	# img = Image.open(os.path.dirname(os.path.realpath(__file__)) + '/time_covers/' + 'musk.jpeg')
  	img = Image.open(os.path.dirname(os.path.realpath(__file__)) + '/time_covers/' + 'musk.jpeg')
  	for prop in dir(img):
  		print(prop)

  	print("\n")
  	print(img.getcolors())
  	print(img.getexif())
  	print(img.size)
  	print(img.quantization)
  	print(img.getpalette())


  	# print(img.palette)
  	# print(img.histogram())


    # print(IA.fetch_image_file_names())


if __name__ == "__main__":
    main()

