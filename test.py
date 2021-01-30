 
for i in range(7):
    try:
        file1 = open(f"text_files/{i}.txt","r") 
        content = file1.read()

        # finding index of 'CLASS'    will return index.
        index = content.find('CLASS')
        index_2 = index + 25
        class_ = content[index:index_2]

        print(class_)
    except Exception:
        pass