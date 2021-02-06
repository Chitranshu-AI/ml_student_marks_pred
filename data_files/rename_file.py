# this py file changes name of file in sequence in ascending or 1,2,3,4...... in a file (path)

import os
# Function to rename multiple files
def rename_files():
   i = 0
   path="F:/programming projects/web scrapper/data_files/final_classified_txt_files/class_11/"
   for filename in os.listdir(path):
      my_dest = str(i) + ".txt"
      my_source =path + filename
      print(my_source)
      my_dest =path + my_dest
      print(my_dest)

      # rename() function will
      # rename all the files
      os.rename(my_source, my_dest)
      i += 1


rename_files()