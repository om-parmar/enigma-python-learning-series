p1={'L':1,'R':1}
p2={'L':1,'R':1}

def check(p):
  val=list(p.values())
  if val[0]==0 and val[-1]==0:
    return True
  if val[0]==5 and val[-1]==0:
    return True
  if val[0]==0 and val[-1]==5:
    return True
  return False




def status(p1,p2):
  p1val=list(p1.values())
  p2val=list(p2.values())
  print('Current status:')
  print('player 1:', *p1val)
  print('player 2:',*p2val)

  
def attack(c,p1,p2):
  com=list(map(str,c.strip().split(' ')))
  p2[com[1]]+=p1[com[0]]
  if p2[com[1]]==5:
    p2[com[1]]=0
  return p2


def splt(m,p):
  com=list(map(str,m.strip().split(' ')))
  
  p['L'],p['R']=int(com[1]),int(com[-1])
  return p


while True:

  status(p1,p2)
  m=input('enter move for player 1: ')
  c=input('enter combination: ')
  if m=='A':
    p2=attack(c,p1,p2)

  if m=='S':
    p1=splt(c,p1)
  if check(p1):
    print('player 2 wins')
    break

 
  status(p1,p2)
  m=input('enter move for player 2: ')
  c=input('enter combination: ')
  if m=='A':
    p1=attack(c,p2,p1)

  if m=='S':
    p2=splt(c,p2)
  if check(p2):
    print('player 1 wins')
    break
