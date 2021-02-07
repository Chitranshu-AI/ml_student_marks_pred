import pandas as pd
import os

data_file = open("data.txt", "a")   
  


path_c4 = "F:/programming projects/web scrapper/data_files/final_classified_txt_files/class_9/"
for file in os.listdir(path_c4)[-1:]:
    file1 = open(path_c4+file, "r") 
    content = file1.read()
    
    subject = ['ENGLISH','HINDI','MATHEMATICS','SCIENCE','SOCIAL SCIENCE']
    
    class_ = path_c4[]
    data_file.write(f'{class_},')
    def sub_marks():
        for i in subject:
            x = content.find(i)
            sub_len = len(i)
            index_1_sub = x+sub_len+1
            index_2_sub = x+sub_len+4
            sub_periodic = content[index_1_sub:index_2_sub]
            print(sub_periodic)
            print(f'type of {sub_periodic} is {type(sub_periodic)}')
           
            data_file.write(sub_periodic+',')
    sub_marks()
    
    def percentage_():
        per = content.find('PERCENTAGE')
        per_len = len('PERCENTAGE')
        index_1_per = per+per_len+3
        index_2_per = per+per_len+7
        percentage = content[index_1_per:index_2_per]
        print('percentage:'+percentage)
        data_file.write(percentage) 
    percentage_()
    data_file.write("\n") 


        
print()