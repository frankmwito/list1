#return a list of strings that start woth 'a'

n1 = int(input("Enter the size of your list:"))
words = list()

for i in range(n1): 
    words.append(str(input(f"Enter any word {i+1}:")))
    
print("your new word list is", words)


def string_list (words: str)-> list:
    my_list = list()
    for word in words:
        if word.startswith('a'):
            my_list.append(word)
            
    return my_list
        
    
return_list = string_list(words)
print(return_list)