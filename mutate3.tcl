package require psfgen

set pdb_file <pdb_to_mutate>
set filename [file rootname [file tail $pdb_file]]
alias residue HIS HSE
set a [open ${filename}_tyr_id.txt r]
set tyrid_lines [split [read $a] "\n"]
set tyrid_lines [lreplace $tyrid_lines end end]
close $a;                         

set outpdb "${filename}_mutated.pdb"
set outpsf "${filename}_mutated.psf"

resetpsf
topology charmm2lammps_all36_tip3/top_all36_prot_C2L_TIP3_OH_CLA_SOD.rtf

segment P1 {
    pdb $pdb_file
    foreach line $tyrid_lines {
       mutate $line DOPA
       }
}

coordpdb $pdb_file
guesscoord
regenerate angles dihedrals

writepdb $outpdb
writepsf $outpsf

exit