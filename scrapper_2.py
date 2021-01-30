import os


def find_class():

    for i in range(0,7):

        # opening txt file
        file1 = open(f"text_files/{i}.txt","r") 
        content = file1.read()

        # finding index of 'CLASS'    will return index.
        index = content.find('CLASS')

        # f_index is first index    l_index is last index
        f_index = index + 17
        l_index = index + 20


        class_stud = content[f_index:l_index]
        print(class_stud)

        print(f'{i}.txt')

        if 'XI' in class_stud:
            print('student read in class 11')
            path="F:/programming projects/web scrapper/text_files/"
            my_source =str(i) + ".txt"
            my_dest =path + f'class_11_{i}.txt'
            my_dest =path + my_dest

            # os.rename(f"text_files/{i}.txt", f'text_files/class_11_{i}.txt')
            print('')
        elif 'X' in class_stud:
            print('student read in class 10')
            print('')
        else:
            print('student is not in 10 or 11')
            print('')


find_class()

