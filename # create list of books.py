# create list of books
books = [['bible', 'extreme ownership', '12 rules of life', '49 laws of power', 'Epidmic', 'Comptia sec+','Blackwater']]
#input mood
print('what mode are you in?')
mood = input()
# loop throuh and find a matching mood. 
for item in books:
    if item [1] == mood:
        print (mood + ' book: '+item[0]) 