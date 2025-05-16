def get_book_text(file_path):
    with open(file_path, "r") as f:
        file_contents = f.read()
    return file_contents

def words_count(textt):
    count = 0
    words = textt.split()
    count = len(words)
    return count

def count_unq_char(text):
    text = text.lower()
    dict_unq = {}
    for l in text:
        if l.isalpha():
            if l not in dict_unq:
                dict_unq[l] = 1
            else:
                dict_unq[l] += 1
    
    return dict_unq

def count_num(list_dict):
    return list_dict["num"]
    
def sort_dict(dict_unq):
    
    list_dict = [{"char": key, "num": value} for key, value in dict_unq.items()]

    list_dict.sort(reverse=True, key=count_num)
    return list_dict
