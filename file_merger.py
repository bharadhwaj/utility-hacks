import glob
import shutil

# Change the `.txt` to your required format like `.docx`, `.doc` etc.
files_available = glob.glob('*.html')


# Name of the file to which all these to be merged
with open('combined_file.txt', 'wb') as output_file:
	for file in files_available:
		with open(file, 'rb') as file_content:
			shutil.copyfileobj(file_content, output_file, 1024*1024*10)