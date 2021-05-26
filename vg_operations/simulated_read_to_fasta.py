
def make_fasta(read,name):
    f = open(name + ".fa",'w')
    f.writelines(">" + name + "\n")
    start = 0
    size = 69
    while (start+size < len(read)):
        f.writelines(read[start:start+size] + "\n")
        start += size
    f.writelines(read[start:len(read)] + "\n")
    f.close()


input_file_dir = "read.sim.txt"
f = open(input_file_dir,'r')
read_lines = []
for line in f:
    read_lines.append(line)

for index in range(len(read_lines)):
    read = read_lines[index]
    output_name = "simulated_read_" + str(index)
    make_fasta(read,output_name)
