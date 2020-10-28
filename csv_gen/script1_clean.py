

""" clean pdb"""
def clean_pdb(pdb_input):
    import shutil, os
    with open (pdb_input, 'r') as f:
        for line in f:
           if (("ATOM" in line) or ("HETATM" in line)) and ('REVDAT' not in line) and ("REMARK" not in line) and ('CA1' not in line) and ('BARG' not in line) and ('CARG' not in line) and ('BASP' not in line) and ('BASN' not in line) and ('BMET' not in line) and ('BHIS' not in line) and ('BLYS' not in line) and ('CLYS' not in line) and ('DLYS' not in line) and ('BGLU' not in line) and ('BSER' not in line) and ('CSER' not in line) and ('BTHR' not in line) and ('BGLN' not in line) and ('BCYS' not in line) and ('BGLY' not in line) and ('BPRO' not in line) and ('BALA' not in line) and ('CMET' not in line) and ('CSER' not in line) and ('BVAL' not in line) and ('BILE' not in line) and ('BLEU' not in line) and ('BPHE' not in line) and ('BTYR' not in line) and ('BTRP' not in line) and ('CGLN' not in line) and ('CARG' not in line) and ('BMSE' not in line) and ('BFUC' not in line) and ('BNAG' not in line) and ('BGAL' not in line) and ('BPO4' not in line) and ('B1PE' not in line) and ('BEPE' not in line) and ('BGOL') not in line and ('BTSR' not in line) and ('BTRQ') not in line and ('BHOH' not in line) and ('CHOH' not in line) and ('BSO4' not in line):
              line = line.replace('AARG', ' ARG')
              line = line.replace('AASP', ' ASP')
              line = line.replace('AASN', ' ASN')
              line = line.replace('AFUC', ' FUC')
              line = line.replace('ANAG', ' NAG')
              line = line.replace('AGAL', ' GAL')
              line = line.replace('APO4', ' PO4')
              line = line.replace('A1PE', ' 1PE')
              line = line.replace('AEPE', ' EPE')
              line = line.replace('AGOL', ' GOL')
              line = line.replace('ATRS', ' TRS')
              line = line.replace('ATRQ', ' TRQ')
              line = line.replace('ASO4', ' SO4')

              line = line.replace('AMET', ' MET')
              line = line.replace('AHIS', ' HIS')
              line = line.replace('ALYS', ' LYS')
              line = line.replace('AGLU', ' GLU')
              line = line.replace('ASER', ' SER')
              line = line.replace('ATHR', ' THR')
              line = line.replace('AGLN', ' GLN')
              line = line.replace('ACYS', ' CYS')
              line = line.replace('AGLY', ' GLY')
              line = line.replace('APRO', ' PRO')
              line = line.replace('AALA', ' ALA')
              line = line.replace('AVAL', ' VAL')
              line = line.replace('AILE', ' ILE')
              line = line.replace('ALEU', ' LEU')
              line = line.replace('APHE', ' PHE')
              line = line.replace('ATYR', ' TYR')
              line = line.replace('ATRP', ' TRP')
              line = line.replace('AMSE', ' MSE')
              line = line.replace('AHOH', ' HOH')
              with open ('tmp', 'a') as g:
                  g.write(str(line))
    shutil.move ('tmp', pdb_input)            

