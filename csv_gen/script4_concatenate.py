

def concat(pdb_input):
  import shutil, os
  root = (pdb_input.replace(".pdb",""))
  root = root[-4:]
  src = os.getcwd() + "/" + root
  dst = src + "_2/"
  output = dst + "motifs.dat"
  alpha_beta = src + "/alpha_beta_motif.dat"
  asx_motif = src + "/asx_motif.dat" 
  betabulge1 = src + "/beta_bulge_loop_typeI.dat"
  betabulge2 = src + "/beta_bulge_loop_typeII.dat"
  betabulge = src + "/beta_bulges.dat"
  betaturn = src + "/beta_turn.dat"
  gammaturn = src + "/gamma_turn.dat"
  nest = src + "/nest.dat"
  niche = src + "/niche.dat"
  niche3r = src + "/niche-3r.dat"
  niche4r = src + "/niche-4r.dat"
  sch = src + "/schellman_loop.dat"
  stmotif = src + "/ST_motif.dat"
  stturn = src + "/st_turn.dat"

  with open (output, 'a') as g:
    if os.path.isfile(alpha_beta):
      with open (alpha_beta, 'r') as f:
         for line in f:
             line1 = line.strip('\n') + " alpha_beta"
             g.write(line1 + "\n")
    if os.path.isfile(asx_motif):
      with open (asx_motif, 'r') as f:
         for line in f:
             line1 = line.strip('\n') + " asx_motif"
             g.write(line1 + "\n")
    if os.path.isfile(betabulge1):
      with open (betabulge1, 'r') as f:
         for line in f:
             line1 = line.strip('\n') + " beta_bulge_loop_I"
             g.write(line1 + "\n")
    if os.path.isfile(betabulge2):
      with open (betabulge2, 'r') as f:
         for line in f:
             line1 = line.strip('\n') + " beta_bulge_loop_II"
             g.write(line1 + "\n")
    if os.path.isfile(betabulge):
      with open (betabulge, 'r') as f:
         for line in f:
             line1 = line.strip('\n') + " beta_bulge"
             g.write(line1 + "\n")
    if os.path.isfile(betaturn):
      with open (betaturn, 'r') as f:
         for line in f:
             line1 = line.strip('\n')
             line1 = line1.split()
             line1a = line1[0] + " " + line1[1] + " " + line1[2] + " " + line1[3] + " " + line1[4]
             line1b = line1[5] + "_" + line1[6]
             g.write(line1a + " beta_turn_" + line1b  + "\n")
    if os.path.isfile(gammaturn):
      with open (gammaturn, 'r') as f:
         for line in f:
             line1 = line.strip('\n')
             line1 = line.split()
             line1a = line1[0] + " " + line1[1] + " " + line1[2] + " " + line1[3]
             line1b = line1[4]
             g.write(line1a + " gamma_turn_" + line1b  + "\n") 
    if os.path.isfile(nest):
      with open (nest, 'r') as f:
         for line in f:
             line1 = line.strip('\n')
             line1 = line.split()
             line1a = line1[0] + " " + line1[1] + " " + line1[2]
             line1b = line1[3]
             g.write(line1a + " nest_" + line1b  + "\n")

    if os.path.isfile(niche):
      with open (niche, 'r') as f:
         for line in f:
             g.write(line)
    if os.path.isfile(niche3r):
      with open (niche3r, 'r') as f:
         for line in f:
             g.write(line)
    if os.path.isfile(niche4r):
      with open (niche4r, 'r') as f:
         for line in f:
             g.write(line)
    if os.path.isfile(sch):
       with open (sch, 'r') as f:
         for line in f:
             line1 = line.strip('\n')
             line1 = line.split()
             line1a = line1[0] + " " + line1[1] + " " + line1[2] + " " + line1[3] + " " + line1[4] + " " + line1[5] + " " + line1[6] + " " + line1[7]
             line1b = line1[8]
             g.write(line1a + " schellman_loop_" + line1b  + "\n")

    if os.path.isfile(stmotif):
       with open (stmotif, 'r') as f:
         for line in f:
             line1 = line.strip('\n')
             line1 = line.split()
             line1a = line1[0] + " " + line1[1] + " " + line1[2] + " " + line1[3] + " " + line1[4] + " " + line1[5] + " " + line1[6]
             g.write(line1a + " ST_motif"+ "\n")
    if os.path.isfile(stturn):
      with open (stturn, 'r') as f:
         for line in f:
             line1 = line.strip('\n') 
             line1 = line.split()
             line1a = line1[0] + " " + line1[1] + " " + line1[2] + " " + line1[3] 
             line1b = line1[4] + "_"  + line1[5]
             g.write(line1a + " ST_turn_" + line1b + "\n")
