# -*- coding: utf-8 -*-
import re
from helpers import INITD, REPLACEMENTS

  
orig = ''
trans = ''

for k in INITD:
  s = INITD[k]
  for c in s:
    orig+=c
    trans+=k
     
transtable = str.maketrans(orig, trans)

  
p = re.compile(r"\\indexentry \{(.*)\|")

#hyperindexformat{\infn {8}}}
    
def process(s): 
  if s.strip()=='':
    return s
  m = p.match(s) 
  o = ''
  try:
    o = m.groups(1)[0]
  except AttributeError:
    print(repr(s))
  t = o.translate(transtable)
  
  for r in REPLACEMENTS:
    t = t.replace(r[0],r[1])
  if t == o:
    return s
  else:
    return s.replace(o,"%s@%s"%(t,o))
  
  

if __name__ == '__main__':
  fn = 'main.adx'
  lines = open(fn).readlines()
  print(len(lines))
  lines2 = list(map(process, lines))
  out = open('mainmod.adx','w')
  out.write(''.join(lines2))
  out.close()
  
  fn = 'main.sdx'
  lines = open(fn).readlines()
  print(len(lines))
  lines2 = list(map(process, lines))
  out = open('mainmod.sdx','w')
  out.write(''.join(lines2))
  out.close()
    
  fn = 'main.ldx'
  lines = open(fn).readlines()
  print(len(lines))
  lines2 = list(map(process, lines))
  out = open('mainmod.ldx','w')
  out.write(''.join(lines2))
  out.close()
  