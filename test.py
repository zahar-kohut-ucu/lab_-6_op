with open('en.txt', 'r') as en:
    with open('en1.txt', 'w') as en1:
        en_cont = en.readlines()
        for _i in en_cont:
            if len(_i.strip()) >= 4:
                en1.write(_i)
            