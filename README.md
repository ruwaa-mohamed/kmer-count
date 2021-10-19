# Kmer-count
A standalone Python tool that counts the kmers per sequence in a multi-FASTA file and return the results in CSV format.

## How to install
```bash
gh repo clone ruwaa-mohamed/kmer-count
```

## How to use
```bash
python3 kmer-count/kmer-coun.py -f <path/to/file_in.fasta> -o <path/to/file_out_prefix_> -k <int>
```

### Example
```bahs
python3 kmer-count/kmer-count.py -f input.fasta -o kmers_ -k 5,6,7
```
### Main Argumrnts
* `-f <fasta_file>`: the path to the input fasta file. It can handle multi-fasta file where each record is composed of two lines (header and sequence). It doesn't work on fasta file with sequence spanning multiple lines (fixed-width fasta files).
* `-o <output_prefix_string>`: A string that would be used as a prefix for all output csv files. Each output file will be named with this prefix and the `k` used in this file.
* `-k <comma-separated-integers>`: a comma-separate list of integers (with no spaces) that will be used as length of the k-mers.
* `-h | --help`: to print the help message of the tool (the user manual). 

### Date last modified
Oct. 18, 2021
