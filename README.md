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

## Example
```bahs
python3 kmer-count/kmer-count.py -f input.fasta -o kmers_ -k 5,6,7
```
