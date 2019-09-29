seqs=["UUCGCCGACUGA","AUGCCUUGA","AUGCGGUGAUAA"]
for seq in seqs:
    print(seq)
    if seq.startswith("AUG"):
        print("Has start codon")
    if seq.count("UGA")>=0 and not seq.endswith("UGA"):
        print("Has selenocysteine")
    if seq.count("GTCATGAC")>=0 and not seq.endswith("GTCATGAC"):
        print("Has palindromic DNA")
    if seq.count("CAGTACTG")>=0 and not seq.endswith("CAGTACTG"):
        print("Has palindromic DNA")
        
        
