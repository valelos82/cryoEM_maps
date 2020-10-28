




def add_blank_lines(pdb_input, csv_output, csv_output2):
  num_lines_pdb = sum(1 for line in open(pdb_input))
  print ('generating', num_lines_pdb, 'blank lines for all lines in pdb files')
  with open(csv_output, 'a') as f:
    for i in range(1, num_lines_pdb + 1):
         f.write("\n")
  with open(csv_output2, 'a') as f:
    for i in range(1, num_lines_pdb + 1):
         f.write("\n")

def add_other(input_shuffled, csv_output, csv_output2):

   import shutil, os
   
   csv_output = input_shuffled.replace("_shuffled.pdb", "_2ndlevel_PU_2SSE.csv")
   csv_output2 = input_shuffled.replace("_shuffled.pdb", "_2ndlevel_PU_2+SSE.csv")
   root = (input_shuffled.replace("_shuffled.pdb",""))
   root = root[-4:]
   dst = root + "_2/"
   count = 0
  # input_shuffled = pdb_input.replace(".pdb","_shuffled.pdb")

   with open(csv_output, 'r') as f:
          count_csv = 0          
          for line in f:
            count_csv = count_csv + 1
          #  print (count_csv)
            if line != "\n":
                print ('line is not empty')
                with open ('tmp.dat', 'a') as g:
                     g.write(line)
            else:
                with open (input_shuffled, 'r') as h:
                    
                    count_pdb = 0
                    for line2 in h:
                         res_name = line2[17:20]
                         count_pdb = count_pdb + 1
                         if count_csv == count_pdb:
                             if 'HOH' in line2:
                                print ('water')
                                with open ('tmp.dat', 'a') as g:
                                   g.write("water\n")

                             elif (" DA" in res_name) or  (" DC" in res_name) or (" DG" in res_name) or (" DT" in res_name) or (" DI" in res_name) or (" A " in res_name) or (" C " in res_name) or (" G " in res_name) or (" U " in res_name) or (" I"  in res_name):
                                with open ('tmp.dat', 'a') as g:
                                    g.write('nucleic\n')

                             else:
                                with open ('tmp.dat', 'a') as g:
                                   print ('other (not water and not nucleic')
                                   g.write("other\n")
   shutil.move('tmp.dat', csv_output)
   print ("DONE FIRST CSV")
   with open(csv_output2, 'r') as f:
          count_csv2 = 0
          for line in f:
            count_csv2 = count_csv2 + 1
          #  print (count_csv2) 
            if line != "\n":
                with open ('tmp2.dat', 'a') as g:
                     g.write(line)
            else:
                with open (input_shuffled, 'r') as h:
                    count_pdb = 0
                    for line2 in h:
                         res_name = line2[17:20]
                         count_pdb = count_pdb + 1
                         if count_csv2 == count_pdb:
                             if 'HOH' in line2:
                                with open ('tmp2.dat', 'a') as g:
                                   g.write("water\n")
                             elif (" DA" in res_name) or  (" DC" in res_name) or (" DG" in res_name) or (" DT" in res_name) or (" DI" in res_name) or (" A " in res_name) or (" C " in res_name) or (" G " in res_name) or (" U " in res_name) or (" I"  in res_name):
                                with open ('tmp2.dat', 'a') as g:
                                    g.write('nucleic\n')
                             else:
                                with open ('tmp2.dat', 'a') as g:
                                   g.write("other\n")

   shutil.move('tmp2.dat', csv_output2)
   print ("DONE SECOND CSV")

def generate_csv_3rdlevel(pdb_input):
  import shutil, os
  csv_output = pdb_input.replace(".pdb", "_2ndlevel_PU_2SSE.csv")
  csv_output2 = pdb_input.replace(".pdb", "_2ndlevel_PU_2+SSE.csv")
  root = (pdb_input.replace(".pdb",""))
  root = root[-4:]
  dst = root + "_2/"
  count = 0
  input_shuffled = pdb_input.replace(".pdb","_shuffled.pdb")
#  with open (input_shuffled, 'r') as f:

  add_blank_lines(pdb_input, csv_output, csv_output2)
  count_topol = 0
  with open ('PUs/list_topologies', 'r') as f:
    for line in f:
       line = line.strip('\n')
       line_split = line.split(' ')
       topol = line_split[0]
       count_topol = count_topol + 1
     #  print (count_topol, topol)
       noloop = topol.replace('U','')
       noloop = noloop.replace('L','')
       noloop = noloop.replace('O','')
       curr = os.getcwd()
       mydir = curr + "/PUs/PUs_" + topol + "/" + root
       pusfile = mydir + "/" + root + ".pus"
       if os.stat(pusfile).st_size != 0:
          with open (pusfile, 'r') as g:
            for line2 in g:
                line2_split = line2.split('[')
                chain = line2_split[0].strip()
                res_list = line2_split[1].strip('\n')
                res_list = res_list.replace(']','')
                residues = res_list.split(',')
                lines_res = []
                count = 0
                with open (input_shuffled, 'r') as h:
                   for line in h:
                       count = count + 1
                       pdb_chain = line[21:22]
                       res_nr = line[22:26].strip()
                       for res in residues:
                         res = res.lstrip()
                         if (chain == pdb_chain) and (res in res_nr) and (len(res) == len(res_nr)):
                             lines_res.append(count)


                if len(noloop) == 2:
                  print ("len = 2, writing in 1st csv")
                  with open(csv_output, 'r') as file:
                    data = file.readlines()

                  for i in lines_res:
              #          print ("i=", i, "datai=", data[i], "topol=", topol)
                        i = i - 1
                        if topol not in data[i]:
                                if data[i] != "\n":
                                   data[i] = str(data[i]).strip('\n') +"," + topol + "\n"
                                else:
                                   data[i] = topol + "\n"

                  with open(csv_output, 'w') as file:
                            file.writelines( data )

                else:
                  print ("len > 2, writing in 2nd csv")
                  with open(csv_output2, 'r') as file:
                    data = file.readlines()

                  for i in lines_res:
                      #  print ("i=", i, "datai=", data[i], "topol=", topol)
                        i = i - 1
                        if topol not in data[i]:
                                if data[i] != "\n":
                                   data[i] = str(data[i]).strip('\n') +"," + topol + "\n"
                                else:
                                   data[i] = topol + "\n"

                  with open(csv_output2, 'w') as file:
                            file.writelines( data )
  print ("adding other")
  add_other(input_shuffled, csv_output, csv_output2)
  print ("done")
