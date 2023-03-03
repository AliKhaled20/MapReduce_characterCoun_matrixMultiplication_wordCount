import string
def occurance(text):
    alphabet=string.printable
    for i in alphabet:
        count = 0
        for j in text:
            if i==j:
                count=count+1
            else:
                continue
        if count!=0:
            print(i,'-',count)
        else:
            pass

path=input("Enter the file name with path\n:")
fread=open('%s'%path,'r')
text=fread.read()
splitting=text.split(' ')
word_count=len(splitting)
fread.close()

print('Word Count= ',word_count,'\n')
print('Occurance of letters')
occurance(text)
input('Press ENTER to exit')