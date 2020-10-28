import shutil, os
import script1_clean, script2_shuffle, script3_sse
import script4_concatenate, script5_motifs, script6_merge
import script7_processPU, script8_PUs

path1 = os.getcwd()
root = "1a9x"

init_pdb = path1 + "/" + root + "/" + root + ".pdb"
newdir = path1 + "/" + root + "_2/"

if os.path.isdir(newdir) == False:
    os.mkdir(newdir)
    shutil.copy(init_pdb, newdir)
    shutil.copy('list_files.py', newdir)
pdb_input = newdir + root + ".pdb"

print ("running step 1: cleaning PDB file")
script1_clean.clean_pdb(pdb_input)
print ("pdb cleaning done")
print ("running step 2: shuffling pdb lines")
script2_shuffle.shuffle_pdb(pdb_input)
print ("pdb file rearranged")
print ("step 3: writing secondary sructure and ppII to 1st level csv - 1st part")
script3_sse.sse(pdb_input)
print ("SSE + PPII csv done")
print ("step 4: concatenating motif files to a single file")
script4_concatenate.concat(pdb_input)
print ("unique small motif files created")
print ("step 5 writing small motifs to 1st level csv - 2nd part")
script5_motifs.smallmotifs(pdb_input)
print ("small motifs done")
print ("step 6: merging csv for 1st level into a single file")
script6_merge.merge_csv(pdb_input)
print ("csv for 1st level DONE")
print ("step 7: preprocess PU output to include chains and res nr within them")
script7_processPU.process_output(pdb_input)
print ("PU ouput preprocessing done")
print ("step 8: writing two CSVs for PUs with 2 SSE and 2+ SSE")
script8_PUs.generate_csv_3rdlevel(pdb_input) 
print ("CSV for 2nd and 3rd level DONE")
