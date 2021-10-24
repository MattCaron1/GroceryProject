import re
import string

def histogram():
    # Start writing the content to file 
    f = open("frequency.dat", "w")
     # Open the file in read mode
    text = open("txtfile.txt", "r")
  
    # Create a dictionary
    d = dict()
  
    for line in text:
        line = line.strip()
        line = line.lower()
        line = line.translate(line.maketrans("", "", string.punctuation))
        words = line.split(" ")
  
        for word in words:
            if word in d:
                d[word] = d[word] + 1
            else:
                d[word] = 1
  
    # write to the dictionary 
    for key in list(d.keys()):
        strValue = str(key)+" "+str(d[key])
        f.write(strValue+"\n")
   
    f.close()
    print("frequency.dat written Successful\n")
    print("Creating and displaying a histogram\n")
    file = open("frequency.dat", "r")

    for lines in file:
        data = lines.split()
        name = data[0]
        fre  = int(data[1])
        newString = ""
        newString = name+" "
        #print(name," "),
        for x in range(fre):
           newString +="*";

        print(newString)

    return 0
def frequency(item):
    value = 0;
    text = open("txtfile.txt", "r")
  
    # Create a dictionary
    d = dict()

    for line in text:
        line = line.strip()
        line = line.lower()
        line = line.translate(line.maketrans("", "", string.punctuation))
        words = line.split(" ")
  
        for word in words:
            if word in d:
                d[word] = d[word] + 1
            else:
                d[word] = 1
    
    if item in list(d.keys()):
        value= d[item]
    
    return value
def freq():
    text = open("txtfile.txt", "r")
  
    # Create a dictionary
    d = dict()
  
    for line in text:
        line = line.strip()
        line = line.lower()
        line = line.translate(line.maketrans("", "", string.punctuation))
        words = line.split(" ")
        for word in words:
            if word in d:
                d[word] = d[word] + 1
            else:
                d[word] = 1
  
    print("Words  : Frequency")
    for key in list(d.keys()):
        print(key, ":", d[key])
    return 0
 
