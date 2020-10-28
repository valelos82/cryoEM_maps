def merge_csv(pdb_input):

  import os
  root = (pdb_input.replace(".pdb",""))
  root = root[-4:]
  dst =  os.getcwd() + "/" + root + "_2/"
  file1 = dst + root + "_1stlevel_ss.csv"
  file2 = dst + root + "_1stlevel_motifs.csv"
  file3 = dst + root + "_1stlevel.csv"
  with open(file3, 'w') as file3:
    with open(file1, 'r') as file1:
        with open(file2, 'r') as file2:
            for line1, line2 in zip(file1, file2):
                print(line1.strip(), line2.strip(), sep=",", file=file3) 

