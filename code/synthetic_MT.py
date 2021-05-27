from random import randint
import argparse

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
        trial = randint(1,10)
        if trial >= 8:
            newline = []
            for char in line:
                if char != "\n":
                    newline.append(alphabet[randint(1,4)])
                else:
                    newline.append("\n")
            return newline
        else:
            return line

def argument_parsing():
    info = """
        making the command line arguments friendlier.
    """
    parser = argparse.ArgumentParser(description=info)
    parser.add_argument(
        "-infile",
        "--input_file_loc",
        type=str,
        required=True,
        help="directory of the input file"
    )
    parser.add_argument(
        "-outdir",
        "--output_directory",
        type=str,
        required=True,
        help="Enter the directory of the output file(s)"
    )
    parser.add_argument(
        "-num_files",
        "--number_of_files",
        type=int,
        required=True,
        help="Enter the number of synthetic fasta files to build"
    )
    parser.add_argument(
        "-outfile",
        "--output_file",
        type=str,
        required=True,
        help="Name of the output files, e.g. MT-synthetic"
    )

    return parser.parse_args()

if __name__ =="__main__":
    args = argument_parsing()

    num_examples = args.number_of_files
    input_file = args.input_file_loc
    out_dir = args.output_directory
    out_file = args.output_file

    # Read the MT-human file
    fR = open(input_file,'r')
    input_fasta = []
    for line in fR:
        input_fasta.append(line)

    # construct the output files 
    for i in range(num_examples):
        name = out_dir + out_file + str(i) + ".fa"
        fW = open(name,'w')
        for line in input_fasta:
            fW.writelines(randomlines(line,i))
        fW.close()
    