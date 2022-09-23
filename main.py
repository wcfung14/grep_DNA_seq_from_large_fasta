import re
import os
import sys

os.chdir(os.path.dirname(sys.argv[0]))

fasta = "./Trigoniulus_corallinus_hic.gff3.longest-gene.proteins.fa"

pattern_file = "./DEG_gene_id.txt"

output_counter = 0
pattern_counter = 0
with open("./output.txt", "w") as output:
    with open(pattern_file, "r") as pattern_file:
        for pattern in pattern_file:
            pattern_counter += 1
            print(pattern.strip())
            with open(fasta, "r") as file:
                for line in file:
                    if re.search(pattern.strip(), line):
                        print("yes")
                        output_counter += 1
                        #print(line)
                        #print(next(file))
                        output.write(line)
                        output.write(next(file))
        print(output_counter)
        print(pattern_counter)
        assert pattern_counter == output_counter
