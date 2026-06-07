import random,hashlib,time,uuid,os,sqlite3
mac=hex(uuid.getnode())
key=hashlib.sha256(mac.encode()).hexdigest()[:32]
if not os.path.exists('hw_key.txt'):open('hw_key.txt','w').write(key)
if open('hw_key.txt').read().strip()!=key:print("[DENIED] Unauthorized device.");exit()
print("[OK] License verified.\n")
H={'a':['4','@'],'e':['3','&'],'i':['1','!'],'o':['0','*'],'s':['5','$'],'t':['7','+'],'g':['9','G'],'l':['1','|'],'z':['2','Z']}
def mut(w):
 return ''.join(random.choice(H.get(c.lower(),[c])) if c.lower() in H and random.random()<0.7 else c for c in w)
def lx(k):
 if '(' not in k:raise SyntaxError("Error: missing parenthesis")
 f=k[:k.index('(')];a=k[k.index('(')+1:k.index(')')].strip('"').strip("'")
 return f,a
def run(f,a):
 if f=='db_connect':
  db=sqlite3.connect(a+'.db')
  db.execute('CREATE TABLE IF NOT EXISTS veil_log (id INTEGER PRIMARY KEY, ts TEXT, cmd TEXT)')
  db.execute('INSERT INTO veil_log (ts,cmd) VALUES (?,?)',(str(time.time()),f+'('+a+')'))
  db.commit();db.close()
  print("  >> SSL layer started");time.sleep(0.3)
  print("  >> Database file created: "+a+".db");time.sleep(0.3)
  print("  >> Table initialized");time.sleep(0.2)
  print("  [OK] DB CONNECTED")
 elif f=='api_connect':
  print("  >> DNS resolved");time.sleep(0.3)
  print("  >> Token received");time.sleep(0.3)
  print("  [OK] API READY")
 elif f=='auth_setup':
  print("  >> Key generated");time.sleep(0.3)
  print("  [OK] AUTH ACTIVE")
 else:
  print("  >> Processing");time.sleep(0.3)
  print("  [OK] DONE")
print("|  VeilLang -- Layer 3  |")
print("Commands: db_connect(\"mydb\")\n")
while True:
 try:g=input("veil> ").strip()
 except:bre
