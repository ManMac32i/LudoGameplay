

def next_state(s1,s2, d):
  s = {}
  if s1 == 0 and s2 == 0:
    if d == 6:
      s=     {1: (1,0),
              2: (0,1),
              0: None}
    else:
      s=      {1: None,
              2: None,
              0: (0,0)}
  elif s2 == 0:
    if s1+d<=57:
      if d==6:
        s =    {1: (s1+6, 0),
                2: (s1, 1),
                0: None}
      else:
        s =    {1: (s1+d,0),
                2: None,
                0: None}
    else:
      if d==6:
        s =    {1: None,
                2: (s1,1),
                0: None}
      else:
        s =    {1: None,
                2: None,
                0: (s1, 0)}
  else:
    if s1+d<=57:
      s = {1: (s1+d, s2),
           2: (s1, s2+d),
           0: None}
    elif s2+d <= 57:
      s = {1: None,
           2: (s1, s2+d),
           0: None}
    else:
      s = {1: None,
           2: None,
           0: (s1,s2)}

  return {k: (tuple(sorted(v, reverse=True)) if v is not None else None)
          for k, v in s.items()}


F = 57


states = [(a, b) for a in range(F + 1) for b in range(a + 1)]
V = {(s, d): 0.0 for s in states for d in range(1, 7)}
for d in range(1, 7):
    V[((F, F), d)] = 0.0

def W(s):
    return sum(V[(s, d)] for d in range(1, 7)) / 6

while True:
    delta = 0
    for s in states:
        if s == (F, F):
            continue
        for d in range(1, 7):
            nxt_states = next_state(*s, d)
            new_v = max(-1 +W(t) for t in nxt_states.values() if t is not None)
            delta = max(delta, abs(new_v - V[(s, d)]))
            V[(s, d)] = new_v
    if delta < 1e-12:
      print(V[((0,0), 1)])
      break



