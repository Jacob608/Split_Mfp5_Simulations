import sys
 

# Arguments passed
print("\nName of Python script:", sys.argv[0])

# pdb file name
pdb_file=sys.argv[1]

# read pdb file
pdb_read = open(pdb_file, "r")
name=pdb_file.split(".")[0]

# find amino acid id to mutate
tyr_id_list=[]
try:
    for l in pdb_read.readlines():
        if "TYR" in l:
            tyr_id_list.append(int(l.split()[5]))
except IndexError:
    print(l)
    pass
tyr_id_list=list(set(tyr_id_list))
tyr_id_list=sorted(tyr_id_list)

pdb_read.close()

# output the list
list_file = open(str(name)+"_tyr_id.txt", "w")
for i in tyr_id_list:
    list_file.write("%s\n" % i)
list_file.close()
