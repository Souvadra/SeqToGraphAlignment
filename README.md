# SeqToGraphAlignment
Final project for DS202. 

## Pre-requisites
- [AStarix](https://github.com/eth-sri/astarix)

git clone https://github.com/Souvadra/SeqToGraphAlignment.git

wget https://github.com/vgteam/vg/releases/download/v1.33.0/vg
chmod +x vg
mv vg SeqToGraphAlignment/

git clone https://github.com/lh3/minigraph
cd minigraph && make
cp minigraph/minigraph SeqToGraphAlignment/

mkdir synDNA
python3 code/synthetic_MT.py -infile data/MT-human.fa -outdir synDNA/ -num_files 10 -outfile MT-syn

./minigraph -xggs -l10k data/MT.gfa data/MT-chimp.fa data/MT-orangA.fa data/MT-human.fa synDNA/MT-syn0.fa synDNA/MT-syn1.fa synDNA/MT-syn2.fa synDNA/MT-syn3.fa synDNA/MT-syn4.fa synDNA/MT-syn5.fa synDNA/MT-syn6.fa synDNA/MT-syn7.fa synDNA/MT-syn8.fa synDNA/MT-syn9.fa > MT-graph.gfa

./vg view MT-graph.gfa > MT-graph.vg
./vg index -x x.xg -g x.gcsa -k 16 MT-graph.vg
./vg sim -n 10 -l 500 -x x.xg > read.sim.txt

python3 code/simulated_read_to_fasta.py -infile read.sim.txt -outdir sim_reads/ -outfile sim_read

mkdir seq2seq seq2graph

for i in {0..9}
do
./minigraph data/MT-human.fa sim_reads/sim_read"$i".fa > seq2seq/out_seq"$i".paf
./minigraph MT-graph.gfa sim_reads/sim_read"$i".fa > seq2graph/out_graph"$i".gaf
done
