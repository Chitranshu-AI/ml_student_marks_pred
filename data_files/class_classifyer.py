import os
import shutil


def find_class():

    for i in range(7,841):
        try:
            file1 = open(f"sequenced_text_file/{i}.txt","r") 
            content = file1.read()

            # finding index of 'CLASS'    will return index.
            index = content.find('CLASS')
            index_2 = index + 25
            sliced_string = content[index:index_2]
            print(sliced_string)
            file1.close()

        except Exception as e:
            print(e)
            print('error in 1 ')
        

        path="F:/programming projects/web scrapper/sequenced_text_file/"
        path_2="F:/programming projects/web scrapper/final_classified_txt_files"

        
        
        try:

            if 'XI' in sliced_string:
                try:
                    source = path + str(i) + '.txt'
                except:
                    print('1')
                try:
                    dest = path_2  + '/class_11/' + str(i) + '.txt'
                except:
                    print('2')
                try:
                    shutil.move(source, dest)
                except Exception as e:
                    print(e)
                    print('3')    
                    # print(f'student {i} read in 11')

            elif 'IX' in sliced_string:
                source = path + str(i) + '.txt'
                dest = path_2  + '/class_9/' + str(i) + '.txt'
                shutil.move(source, dest)
                print(f'student {i} read in 9' )

            elif 'VIII' in sliced_string:
                source = path + str(i) + '.txt'
                dest = path_2  + '/class_8/' + str(i) + '.txt'
                shutil.move(source, dest)
                print(f'student {i} read in 8' )

            elif 'VII' in sliced_string:
                source = path + str(i) + '.txt'
                dest = path_2  + '/class_7/' + str(i) + '.txt'
                shutil.move(source, dest)
                print(f'student {i} read in 7' )

            elif 'VI' in sliced_string:
                source = path + str(i) + '.txt'
                dest = path_2  + '/class_6/' + str(i) + '.txt'
                shutil.move(source, dest)
                print(f'student {i} read in 6' )

            elif 'IV' in sliced_string:
                source = path + str(i) + '.txt'
                dest = path_2  + '/class_4/' + str(i) + '.txt'
                shutil.move(source, dest)
                print(f'student {i} read in 4' )



            elif 'V' in sliced_string:
                source = path + str(i) + '.txt'
                dest = path_2  + '/class_5/' + str(i) + '.txt'
                shutil.move(source, dest)
                print(f'student {i} read in 5' )

            else :
                print("could'nt recognised")

        except:
            print('error in 3')


find_class()

