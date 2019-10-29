import os
import sys
import re
import collections

if __name__ == '__main__':
    #file_name = sys.argv[1]
   
    file_name = r'd:\Shagane\FirstProject\oscarwilde.txt'
    # f = open(file_name)
    read_file = open(file_name).read()
    all_words = re.findall(r'[A-Za-z\-\']+', read_file)
    words_quantity = len(all_words)
    print('1 METHOD: There are', words_quantity, 'words in the text')

    long_words = []
    words_quantity2 = 0

    for word in all_words:
        words_quantity2 += 1
        # print (word)

        if len(word) >= 3:
            long_words.append(word)

    resalt_counting = collections.Counter(all_words)
  
    print('2 METHOD: There are', words_quantity2, 'words in the text')

    print('10 all most common words in the text are: ', resalt_counting.most_common(10)) 

    print('10 long most common words are : ', collections.Counter(long_words).most_common(10))



            
            
        



