import os
import sys

root_path = "/data/serin/Projects/opticalflow_track_cpu/kia_data_for_OF/"
bmf_folder_path = "/mnt/192.168.1.3/data/serin/Projects/opticalflow_track_cpu"


def open_file(path, data, number_of_files):
	print("Writing to {}".format(path))
	f = open(path, 'w')

	# Write header
	
	f.write("{}, 1\n".format(len(data)))

	# write the file paths
	for file_path in data:
		f.write(root_path + file_path + "\n")

	f.close()


def main():
	folders = [ f.path for f in os.scandir(root_path) if f.is_dir() ]
	
	

	for i in folders:
		subfolders = [ f.path for f in os.scandir(i) if f.is_dir() ]
		for j in subfolders:
			data = []		
			for file in sorted(os.listdir(j)):
				if file.endswith(".ppm"):
					file_name = os.path.join(j, file)
					data.append(os.path.join(j, file))

			

			# File path to bmf files
			out = file_name.split("/")
			bmf_filename = bmf_folder_path + "/" + out[-3] + "_" + out[-2] + ".bmf"
			open_file(bmf_filename, data, len(data))


if __name__ == '__main__':
	main()
