# SeqToGraphAlignment
This repository contains all the necessary codes, data and instructions to show the advantage of using graph as a refernce genome over string based genomes. This is part of my DS202-2020 final project and contains instruction to replicate the experiment I performed to prove the above-mentioned hypothesis in my final report. I have implemented this on a Debian GNU/Linux 10 (buster) on Windows 10 x86_64 Operating System.

## Pre-requisites
- [vg toolkit](https://github.com/vgteam/vg)
- [minigraph](https://github.com/lh3/minigraph)

## Steps to replicate the experimental result
1. Clone the SeqToGraphAlignment repository by typing
```sh
git clone https://github.com/Souvadra/SeqToGraphAlignment.git
```

2. Download the `vg-toolkit` and relocate the executable for ease of use
```sh
wget https://github.com/vgteam/vg/releases/download/v1.33.0/vg
chmod +x vg
mv vg SeqToGraphAlignment/
```

3. Download the `minigraph` repository and relocate teh executable for ease of use
```sh
git clone https://github.com/lh3/minigraph
cd minigraph && make
cd ..
cp minigraph/minigraph SeqToGraphAlignment/
```

4. Make synthetic FASTA files, based on any of the input FASTA files (`MT-human.fa` was chosen in this case)
```sh
cd SeqToGraphAlignment/
mkdir synDNA
python3 code/synthetic_MT.py -infile data/MT-human.fa -outdir synDNA/ -num_files 10 -outfile MT-syn
```

5. Build the reference grpah based on the input and the synthetically generated FASTA files using `minigraph`
```sh
./minigraph -xggs -l10k data/MT.gfa data/MT-chimp.fa data/MT-orangA.fa data/MT-human.fa synDNA/MT-syn0.fa synDNA/MT-syn1.fa synDNA/MT-syn2.fa synDNA/MT-syn3.fa synDNA/MT-syn4.fa synDNA/MT-syn5.fa synDNA/MT-syn6.fa synDNA/MT-syn7.fa synDNA/MT-syn8.fa synDNA/MT-syn9.fa > MT-graph.gfa
```

6. Simulate reads from the constructed reference graph using `vg-toolkit` (we have chosen to construct ten reads each 500 nucleotide long for this example)
```sh
./vg view MT-graph.gfa > MT-graph.vg
./vg index -x x.xg -g x.gcsa -k 16 MT-graph.vg
./vg sim -n 10 -l 500 -x x.xg > read.sim.txt
```

7. Create separate FASTA files from the simulated reads (so that we can directly use those for alignment using default functionalities of `minigraph`
```sh
mkdir sim_reads
python3 code/simulated_read_to_fasta.py -infile read.sim.txt -outdir sim_reads/ -outfile sim_read
```

8. Perform the sequence-to-sequence and sequence-to-graph alignment, both using the default functions of `minigraph`
```sh
mkdir seq2seq seq2graph
for i in {0..9}
do
./minigraph data/MT-human.fa sim_reads/sim_read"$i".fa > seq2seq/out_seq"$i".paf
./minigraph MT-graph.gfa sim_reads/sim_read"$i".fa > seq2graph/out_graph"$i".gaf
done
```

9. The `.paf` and `.gaf` files contain enough information to get to know about how the alignment algorithm performed in both the seq-to-graph and seq-to-seq alignment. In my report, I have shown the the `number of residue matches` which can be known from the `10-th` column of both the `.paf` and `.gaf` files. For more information regarging these file formats, the reader can refer to [GAF](https://github.com/lh3/gfatools/blob/master/doc/rGFA.md#the-graph-alignment-format-gaf) and [PAF](https://github.com/lh3/miniasm/blob/master/PAF.md).
