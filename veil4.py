import random,sys
H={'a':['4','@'],'e':['3','&'],'i':['1','!'],'o':['0','*'],'s':['5','$'],'t':['7','+'],'g':['9','G'],'l':['1','|'],'z':['2','Z'],'n':['||','N'],'r':['I','R']}
def mut(w):
 return ''.join(random.choice(H.get(c.lower(),[c])) if c.lower() in H and random.random()<0.6 else c for c in w)
def mutate_code(src):
 out=[]
 for line in src.split('\n'):
  out.append(' '.join(mut(w) if w.isidentifier() else w for w in line.split(' ')))
 return '\n'.join(out)
def run_veil(filename):
 src=open(filename).read()
 print("=== CLEAN CODE ===")
 print(src)
 print("=== MUTATED (AI cannot read) ===")
 print(mutate_code(src))
 print("=== EXECUTING ===")
 exec(compile(src,'<veil>','exec'),{'__name__':'__main__'})
if len(sys.argv)<2:
 print("|  VeilLang -- Layer 4  |")
 print("|  Full Python Support  |")
 print("Usage: python veil4.py yourcode.py")
else:
 run_veil(sys.argv[1])
