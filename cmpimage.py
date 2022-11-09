# run this in any directory
# pip before running -->
# pip install Pillow

# import required libraries
import os
import sys
from PIL import Image

# function definition for compressing an image
def compressimage(file, verbose = False):
	
	# Get the path of the file
	fpath = os.path.join(os.getcwd(),
							file)
	
	# open up the image
	picture = Image.open(fpath)
	
	# This Pillow library function ssaves and compresses the image with desired quality
	# To change the quality of image,cset the quality variable at your desired level, The more the value of quality variable 
    # the lesser the compression
	picture.save("Compressed_"+file,
				"JPEG",
				optimize = True,
				quality = 50)
	return

# Define a main function
def main():
	
	verbose = False
	
	# checks for verbose flag
	if (len(sys.argv)>1):
		
		if (sys.argv[1].lower()=="-v"):
			verbose = True
					
	# finds current working dir
	cwd = os.getcwd()

	formats = ('.jpg', '.jpeg')
	
	# looping through all the files
	# in a current directory
	for file in os.listdir(cwd):
		
		# If the file format is JPG or JPEG
		if os.path.splitext(file)[1].lower() in formats:
			print('compressing', file)
			compressimage(file, verbose)

	print("Done")

# Driver code
if __name__ == "__main__":
	main()
