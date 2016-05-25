# nishiTRR
parse the distance of end-to-end


USAGE   
python conv.py   

INPUT   
all files whose extension (suffix) are .trr    

OUTPUT   
hoge.gcod    



#trr バイナリファイル書式 (unit: byte)   

***********   
4 int: magic num   
4 int: i1   
4 unsigned int: version_sz   
vesion_sz char*version_sz: version   
4 int: ir_size   
4 int: e_size    
4 int: box_size in byte (3x3)   
4 int: vir_size   
4 int: pres_size   
4 int: top_size   
4 int: sym_size   
4 int: x_size in byte (coordinates?)   
4 int: v_size in byte (velocity?)  
4 int: f_size in byte (force?)   
4 int: natoms (number of atoms)   
4 int: step      
4 int: nre       
REAL_byte REAL: time   
REAL_byte REAL: lam    
REAL_byte REAL: time   
box_size REAL: box (3x3 matrix, Boundary box)
vir_size REAL: vir 
pres_size REAL: pres  
x_size REAL: x   
v_size REAL: v  
f_size REAL: f  

********** NOTICE     
REAL_byte=x_size/atoms/3   
REAL=float(REAL_byte=4) or double(REAL_byte=8)   
we dont know the total num of steps
