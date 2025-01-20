def longest_word(filename):
    f1=open("song.txt","r")
    f2=f1.read()
    f2=f2.split()
    longest=f2[1]
    for word in f2:
        if len(word)>len(longest):
            longest=word
        
    return longest

def song_reverse(filename):
    f1=open("song.txt","r")
    
    lst=[]
   
    for line in f1:
        word=line.rstrip().split()
        lst.append(word)
    f1.close()
    
        
    for line in lst:
        line.reverse()
       
        
    f2=open("song2.txt","w")
    str1=""
    for line in lst:
        for word in line:
            str1+=word+ " "
        str1+="\n"
    f2.write(str1)
    
    f2.close()
    print(str1)


def main():
    
    filename = 'song.txt'
    
    # Part A:
    print(longest_word(filename))
    
    # Part B:
    song_reverse(filename)
    


################################################################ 
"""
DO NOT EDIT BELOW THIS LINE
"""
main()


    

