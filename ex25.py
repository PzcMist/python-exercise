def break_words(stuff):
    """This function will break up words for us."""
    #嘿嘿嘿，这里用的是三引号来进行注释的
    words = stuff.split(' ') #所得到的值就是以列表的形式呈现的
    return words

def sort_words(words):
    """Sorts the words"""
    return sorted(words) #排序，升序；但是并不会改变words

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)   #这里是删除第一个元素，且返回被删除的值
    print(word)

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)   #这里是删除最后一个元素，同时返回删除的值
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words"""
    words = break_words(sentence)
    return sort_words(words)  #进行了排序

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)   #排序后截取的值
    print_first_word(words)
    print_last_word(words)
