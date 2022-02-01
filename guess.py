

running = True

while running:
    f_1 = open("textfiles/wordle_combined.txt", "r")
    words = input("Included words: ")
    words_list = []
    words_list = list(words)
    
    print(words_list)
    words_1 = []
    for i in f_1:

        if len(words_list) == 5:
            if words_list[0] in i and words_list[1] in i and words_list[2] in i and words_list[3] in i and words_list[4] in i:
                print(i)
        if len(words_list) == 4:
            if words_list[0] in i and words_list[1] in i and words_list[2] in i and words_list[3] in i:
                print(i)
        if len(words_list) == 3:
            if words_list[0] in i and words_list[1] in i and words_list[2] in i:
                print(i)
        if len(words_list) == 2:
            if words_list[0] in i and words_list[1] in i:
                print(i)
        if len(words_list) == 1:
            if words_list[0] in i:
                print(i)
        '''
        if words_list[0] in i and words_list[1] in i and words_list[2] in i and words_list[3] in i and words_list[4] in i:
            print(i)
        
        if words_list[0] in i and words_list[1] in i:
            print(i)
        '''
        '''
        if words_list[0] in i:
            words_1.append(i)
            '''
    f_1.close()
    '''
    words_2 = []
    words_3 = []
    words_4 = []
    words_5 = []
    words_print = []
    prnt = 1
    
    
    words_2 = []
    for i in words_1:
        if len(words_list) >= 2 and words_list[1] in i:
            words_2.append(i)
        else: words_print = words_2
    
    for i in words_2:
        if len(words_list) >= 3 and words_list[2] in i:
            words_3.append(i)
        else: words_print = words_3
    
    for i in words_3:
        if len(words_list) >= 4 and words_list[3] in i:
            words_4.append(i)
        else: words_print == words_4
    
    for i in words_4:
        if len(words_list) >= 5 and words_list[4] in i:
            words_5.append(i)
            prnt = 0
    
    if prnt == 0:
        for i in words_5:
            print(i)
    elif prnt == 1:
        for i in words_print:
            print(i)
            
        
    '''

    
        
        
    
