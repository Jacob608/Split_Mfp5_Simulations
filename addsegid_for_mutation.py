import sys


# Arguments passed
print("\nName of Python script:", sys.argv[0])

# pdb file name
pdb_in=sys.argv[1]

segid='P1'
chainid='A'

with open(pdb_in) as pdbfile:
    lines = pdbfile.readlines()
    i = 0
    index = 1
    index_blank = "     "
    if lines[1][:4] == 'ATOM':
        out_name = "add_seg"+pdb_in
        pdb_out = open(out_name, "wt") # open new pdb file to be written to
        index_str = str(index)
        index_len = len(index_str)
        segid_len = len(segid)
        # stitch together line as string with incremented index
        new_line = lines[i][:6] + index_blank[:5-index_len] + index_str + lines[i][11:21] + chainid + lines[i][22:72] + segid + lines[i][76-(4-segid_len):]
        pdb_out.write(new_line)
        for i in range(len(lines)-3):
            i += 1
            index += 1
            index_str = str(index)
            index_len = len(index_str)
            # stitch together line as string with incremented index
            new_line = lines[i][:6] + index_blank[:5-index_len] + index_str + lines[i][11:21] + chainid + lines[i][22:72] + segid + lines[i][76-(4-segid_len):]
            pdb_out.write(new_line)
        ter_line = lines[len(lines)-2][:21] + chainid + lines[len(lines)-2][22:]
        pdb_out.write(ter_line)
        pdb_out.write("END")
        pdb_out.close()
