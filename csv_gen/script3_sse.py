

def sse(pdb_input):

  import shutil, os
  csv_output = pdb_input.replace(".pdb", "_1stlevel_ss.csv")
#  print(pdb_input)
  root = (pdb_input.replace(".pdb",""))
#  print ("root1=", root)
  root = root[-4:]
#  print ("root=", root) 
  src = os.getcwd() + "/" + root
  dst = src + "_2/"
#  print ("dst=", dst)
  ss_file = src + "/sse_ppII.dat"
  shutil.copy(ss_file, dst)
  ss_file = dst + "sse_ppII.dat"
#  print ("ss_file=", ss_file)
  count = 0
  input_shuffled = pdb_input.replace(".pdb","_shuffled.pdb")
  with open (input_shuffled, 'r') as f:
     for line in f:
         count = count + 1
         chain = line[21:22]
         res_nr = line[22:26]
         res_nr = res_nr.strip()
         with open (ss_file, 'r') as ff:
             for line2 in ff:
                 fields = line2.split()
                 chain1 = fields[0]
                 res_nr1 = fields[1]
                 label = fields[2]
                 found = False
                 if chain == chain1 and res_nr == res_nr1:
                    found = True
                    with open (csv_output, 'a') as g:
                         g.write(label + "\n")
                         break
         if found == False:
            res_name = line[17:20]
      #      print ("resname=", res_name)
            atom_name =line[13:16]
            if (" DA" in res_name) or  (" DC" in res_name) or (" DG" in res_name) or (" DT" in res_name) or (" DI" in res_name) or (" A " in res_name) or (" C " in res_name) or (" G " in res_name) or (" U " in res_name) or (" I"  in res_name):
               label = 'nucleic'
            elif 'HOH' in res_name:
               label = 'water'
            else:
                label = 'other'

            with open (csv_output, 'a') as g:
                         g.write(label + "\n")
         



