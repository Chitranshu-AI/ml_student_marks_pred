import os
# Function to rename multiple files
def rename_files():
   i = 0
   path="F:/programming projects/web scrapper/text_files/"
   for filename in os.listdir(path):
      my_dest =str(i) + ".txt"
      my_source =path + filename
      my_dest =path + my_dest
      # rename() function will
      # rename all the files
      os.rename(my_source, my_dest)
      i += 1


rename_files()