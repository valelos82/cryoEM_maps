
def preprocess_output(pusfile):
    import os, shutil
    if os.path.isfile(pusfile):
        with open (pusfile, 'r') as f:

           count = 0
           for line in f:
            count = count + 1
            line_split = line.split(' ')
            if len(line_split) > 3:  
              motif = line_split[1]
              chain = line_split[3]
              resrange = line_split[4]
              first_res = int(resrange.split('-')[0])
              posrange = line_split[5]
              first_pos = int(posrange.split('-')[0])
              diff = first_res - first_pos
              indexes = line_split[9]
              indexes_split = indexes.split('-')
              res_list = []
              for i in indexes_split:
                  index = int(i)
                  res = index + diff
                  res_list.append(res)
              with open ('tmp.dat', 'a') as g:
                 g.write(chain + " " + str(res_list) + "\n")
              shutil.move('tmp.dat', pusfile)

def process_output(pdb_input):
  import os

  root = (pdb_input.replace(".pdb",""))
  root = root[-4:]
  dst = "PUs/"
  list_file = dst + "list_topologies"
  count_topol = 0
  with open (list_file, 'r') as f:
    for line in f:
       line = line.strip('\n')
       line_split = line.split(' ')
       topol = line_split[0]
       count_topol = count_topol + 1
       noloop = topol.replace('U','')
       noloop = noloop.replace('L','')
       noloop = noloop.replace('O','')
  #     curr = os.getcwd()
       mydir = dst + "PUs_" + topol + "/" + root
       pusfile = mydir + "/" + root + ".pus"
       found = False
       with open (pusfile, 'r') as ff:
            for line  in ff:
                if "[" in line:
                    found = True
                  #  print ("True")
                    break
       if found == False:
          preprocess_output(pusfile)
