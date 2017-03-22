import re
import os
for path, dirs, files in os.walk(r'E:\K\Audio Ministry\Voicce recordings\kkk'):
	for file in files:
		print(file)
		# print (file[3:8])

