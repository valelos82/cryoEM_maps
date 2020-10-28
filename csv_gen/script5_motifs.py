

def smallmotifs(pdb_input):
  import shutil, os
  csv_output = pdb_input.replace(".pdb", "_1stlevel_motifs.csv")
  root = (pdb_input.replace(".pdb",""))
  root = root[-4:]
  dst = os.getcwd() + "/" + root + "_2/"
  motifs_file = dst + "motifs.dat"
  count = 0
  input_shuffled = pdb_input.replace(".pdb","_shuffled.pdb")
  with open (input_shuffled, 'r') as f:



     for line in f:
         to_write = ""
         found = False
         count = count + 1
         chain = line[21:22]
         res_nr = line[22:26]
         res_nr = res_nr.strip()
         with open (motifs_file, 'r') as ff:
             for line2 in ff:
               
               if "alpha_beta" in line2:
                 fields = line2.split()
                 chain1 = fields[0]
                 res_nr1 = fields[1]
                 res_nr2 = fields[2]
                 res_nr3 = fields[3]
                 res_nr4 = fields[4]
                 res_nr5 = fields[5]
                 label = "alpha-beta"
                 if chain == chain1 and ((res_nr == res_nr1) or (res_nr == res_nr2) or (res_nr == res_nr3) or (res_nr == res_nr4) or (res_nr == res_nr5)):
                    found = True
                    to_write = to_write + label
                  #  print ("to_write_1=", to_write)
               elif "asx_motif" in line2:
                 fields = line2.split()
                 chain1 = fields[0]
                 res_nr1 = fields[1]
                 res_nr2 = fields[2]
                 res_nr3 = fields[3]
                 res_nr4 = fields[4]
                 res_nr5 = fields[5]
                 label = "asx_motif"
                 if chain == chain1 and ((res_nr == res_nr1) or (res_nr == res_nr2) or (res_nr == res_nr3) or (res_nr == res_nr4) or (res_nr == res_nr5)):
                    found = True
                    if to_write == "":
                       to_write = label
                    else:
                       to_write = to_write + "," + label
                   # print ("to_write_2=", to_write)
               elif ("beta_bulge" in line2) and ("loop" not in line2):
                 fields = line2.split()
                 chain1 = fields[0]
                 res_nr1 = fields[1]
                 res_nr2 = fields[2]
                 res_nr3 = fields[3]
                 label = "beta_bulge"
                 if chain == chain1 and ((res_nr == res_nr1) or (res_nr == res_nr2) or (res_nr == res_nr3)):
                    found = True
                    if to_write == "":
                       to_write = label
                    else:
                       to_write = to_write + "," + label
               elif "beta_bulge_loop" in line2:
                 fields = line2.split()
                 chain1 = fields[0]
                 res_nr1 = fields[1]
                 res_nr2 = fields[2]
                 res_nr3 = fields[3]
                 label = fields[4]
                 if chain == chain1 and ((res_nr == res_nr1) or (res_nr == res_nr2) or (res_nr == res_nr3)):
                    found = True
                    if to_write == "":
                       to_write = label
                    else:
                       to_write = to_write + "," + label


               elif "beta_turn" in line2:
                 fields = line2.split()
                 chain1 = fields[0]
                 res_nr1 = fields[1]
                 res_nr2 = fields[2]
                 res_nr3 = fields[3]
                 res_nr4 = fields[4]
                 label = fields[5]
                 if chain == chain1 and ((res_nr == res_nr1) or (res_nr == res_nr2) or (res_nr == res_nr3) or (res_nr == res_nr4)):
                    found = True
                    if to_write == "":
                       to_write = label
                    else:
                       to_write = to_write + "," + label


               elif "gamma_turn" in line2:
                 fields = line2.split()
                 chain1 = fields[0]
                 res_nr1 = fields[1]
                 res_nr2 = fields[2]
                 res_nr3 = fields[3]
                 label = fields[4]
                 if chain == chain1 and ((res_nr == res_nr1) or (res_nr == res_nr2) or (res_nr == res_nr3)):
                    found = True
                    if to_write == "":
                       to_write = label
                    else:
                       to_write = to_write + "," + label

               elif "nest" in line2:
                 fields = line2.split()
                 chain1 = fields[0]
                 res_nr1 = fields[1]
                 res_nr2 = fields[2]
                 label = fields[3]
                 if chain == chain1 and ((res_nr == res_nr1) or (res_nr == res_nr2) ):
                    found = True
                    if to_write == "":
                       to_write = label
                    else:
                       to_write = to_write + "," + label

               elif "niche" in line2:
                 fields = line2.split()
                 chain1 = fields[0]
                 res_nr1 = fields[1]
                 res_nr2 = fields[2]
                 res_nr3 = fields[3]
                 label = fields[4]
                 if chain == chain1 and ((res_nr == res_nr1) or (res_nr == res_nr2) or (res_nr == res_nr3)):
                    found = True
                    if to_write == "":
                       to_write = label
                    else:
                       to_write = to_write + "," + label


               elif "schellman" in line2:
                 fields = line2.split()
                 chain1 = fields[0]
                 res_nr1 = fields[1]
                 res_nr2 = fields[2]
                 res_nr3 = fields[3]
                 res_nr4 = fields[4]
                 res_nr5 = fields[5]
                 res_nr6 = fields[6]
                 res_nr7 = fields[7]
                 label = fields[8]
                 if chain == chain1 and ((res_nr == res_nr1) or (res_nr == res_nr2) or (res_nr == res_nr3) or (res_nr == res_nr4) or (res_nr == res_nr5) or (res_nr == res_nr6) or (res_nr == res_nr7)):
                    found = True
                    if to_write == "":
                       to_write = label
                    else:
                       to_write = to_write + "," + label

               elif "ST_motif" in line2:
                 fields = line2.split()
                 chain1 = fields[0]
                 res_nr1 = fields[1]
                 res_nr2 = fields[2]
                 res_nr3 = fields[3]
                 res_nr4 = fields[4]
                 res_nr5 = fields[5]
                 res_nr6 = fields[6]
                 label = fields[7]
                 if chain == chain1 and ((res_nr == res_nr1) or (res_nr == res_nr2) or (res_nr == res_nr3) or (res_nr == res_nr4) or (res_nr == res_nr5) or (res_nr == res_nr6)):
                    found = True
                    if to_write == "":
                       to_write = label
                    else:
                       to_write = to_write + "," + label


               elif "ST_turn" in line2:
                 fields = line2.split()
                 chain1 = fields[0]
                 res_nr1 = fields[1]
                 res_nr2 = fields[2]
                 res_nr3 = fields[3]
                 label = fields[4]
                 if chain == chain1 and ((res_nr == res_nr1) or (res_nr == res_nr2) or (res_nr == res_nr3)):
                    found = True
                    if to_write == "":
                       to_write = label
                    else:
                       to_write = to_write + "," + label


         if found == False:
                res_name = line[17:20]
      #      print ("resname=", res_name)
                atom_name =line[13:16]
                if (" DA" in res_name) or  (" DC" in res_name) or (" DG" in res_name) or (" DT" in res_name) or (" DI" in res_name) or (" A " in res_name) or (" C " in res_name) or (" G " in res_name) or (" U " in res_name) or (" I"  in res_name):
                   to_write = 'nucleic'
                elif 'HOH' in res_name:
                   to_write = 'water'
                else:
                   to_write = 'other'

         with open (csv_output, 'a') as g:
                         g.write(to_write + "\n")
         

         



