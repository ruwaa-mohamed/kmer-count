# ----- Header printing ----- #
print('='*50)
print('Counting the kmers per sequence from a fasta file')
print('='*50)

# ----- Importing Libraries ----- #
import itertools as it
import argparse
import subprocess
import gzip

# ----- Getting the Variables from CLI ----- #
args = None
def get_args():
	parser = argparse.ArgumentParser(
		description="A standalone Python tool that counts the kmers per sequence in a multi-FASTA file and return the results in CSV format.",
		epilog="Ex. python kmer-count.py -f <path/to/file_in.fasta> -o <path/to/file_out_prefix_> -k <int>"
	)

	# required argument
	parser.add_argument('-f', action="store", required=True, help='Input fasta file (*.fasta)')
	parser.add_argument('-o', action="store", required=True, help='Output file prefix')
	parser.add_argument('-k', action="store", required=True, help='Length of k-mer in comma separated format (e.g. 5,6,7)')

	# optional arguments
	parser.add_argument('--version', action='version', version='%(prog)s 1.0')

	arguments = vars(parser.parse_args())
	return arguments
	
# ----- Actual Code ----- #
def main():	
	path_in = args['f']
	path_out = args['o']
	ks = [int(i) for i in args['k'].split(',')]
	n = int(int(subprocess.check_output(["wc", "-l", path_in]).split()[0])/2)

	for k in ks:
		print("k-mer size =", k, sep=' ')
		f_in = open(path_in)
		f_out = open(path_out+str(k)+'.csv', 'w')
		f_out.write("#k-mer seq,kmer count\n")
		kmers = dict()
		for i in range(n):
			print(f_in.readline())
			seq = f_in.readline()
			for j in range(len(seq)-k):
				kmer = seq[j:j+k]
				if kmer in kmers.keys():
					kmers[kmer] += 1
				else:
					kmers[kmer] = 1
		for key, val in kmers.items():
			f_out.write(','.join([key, str(val)])+'\n')
		f_out.close()
		f_in.close()
		print("="*50)
			
	#print("="*50)

# ----- main() ----- #
if __name__ == '__main__':
	args = get_args()
	main()
