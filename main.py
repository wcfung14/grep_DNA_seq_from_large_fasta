import re
import os
import sys

os.chdir(os.path.dirname(sys.argv[0]))

fasta_file = "./Trigoniulus_corallinus_hic.gff3.longest-gene.proteins.fa"

pattern_file = "./DEG_gene_id.txt"

output_counter = 0
pattern_counter = 0
with open("./output.txt", "w") as output:
    with open(pattern_file, "r") as pf:
        for pattern in pf:
            pattern_counter += 1
            print(pattern.strip())
            with open(fasta_file, "r") as ff:
                for line in ff:
                    if re.search(pattern.strip(), line):
                        print("yes")
                        output_counter += 1
                        #print(line)
                        #print(next(file))
                        output.write(line)
                        output.write(next(ff))
        print(output_counter)
        print(pattern_counter)
        assert pattern_counter == output_counter
