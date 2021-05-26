from random import randint

# A Global dictionary 
alphabet = dict()
alphabet[1] = "A"
alphabet[2] = "T"
alphabet[3] = "G"
alphabet[4] = "C"

# A Global set 
# alpha_set = {"A","T","G","C"}

def randomlines(line,index):
    if line[0] == ">": 
        return (">MT-synthetic"+str(index)+"\n")
    else:
        newline = []
        for char in line:
            if char != "\n":
                newline.append(alphabet[randint(1,4)])
            else:
                newline.append("\n")
        return newline

# Read the MT-human file
fR = open("MT-human.fa",'r')
mt_human = []
for line in fR:
    mt_human.append(line)

num_examples = 2

for i in range(num_examples):
    name = "MT-synthetic" + str(i) + ".fa"
    fW = open(name,'w')
    for line in mt_human:
        fW.writelines(randomlines(line,i))
    fW.close()
    


