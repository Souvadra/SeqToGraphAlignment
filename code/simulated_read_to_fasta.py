import argparse

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

def argument_parsing():
    info=""""
        making the command line argument friendlier.
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
        "-outfile",
        "--output_file",
        type=str,
        required=True,
        help="Name of the output files"
    )

    return parser.parse_args()

if __name__ == "__main__":
    args = argument_parsing()

    input_file = args.input_file_loc
    out_dir = args.output_directory
    out_file = args.output_file

    f = open(input_file,'r')
    read_lines = []
    for line in f:
        read_lines.append(line)

    for index in range(len(read_lines)):
        read = read_lines[index]
        output_name = out_dir + out_file + str(index)
        make_fasta(read,output_name)
