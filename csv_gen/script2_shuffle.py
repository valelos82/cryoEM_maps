

def shuffle_pdb(pdb_input):
    import os, shutil
    output = pdb_input.replace(".pdb","_shuffled.pdb")

    list_chains = []
    with open (pdb_input, 'r') as f:
         for line in f:
             chain = line[21:22]
             if chain not in list_chains:
                list_chains.append(chain)
    for chain in list_chains:
      with open (pdb_input, 'r') as f:
         for line in f:
             chain1 = line[21:22]
             if chain1 == chain:
                with open (output, 'a') as g:
                   g.write(line)


