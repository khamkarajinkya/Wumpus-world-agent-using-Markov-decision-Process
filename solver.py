
class Solver:
  def __init__(self, mdp):
    # any initialisation you might likes
    self.mdp=mdp
    
  def solve(self):
    V=self.value_iteration()
    best=max(V,key = lambda s: V[s][0])
    best= {best:V[best][1]}
    V= {s:V[s][1] for s in V.keys()}
    return V
        
  def value_iteration(self, epsilon=0.0001):
    v= {s: (0,'') for s in self.mdp.S()}
    g=self.mdp.gamma()
    while True:
        d=0
        v_new = v.copy()
        for s in self.mdp.S():
            for a in self.mdp.A():
                move= self.mdp.R(s) + self.mdp.gamma()*sum([self.mdp.P(s,a,s1)*v_new[s1][0] for s1 in self.mdp.S()])
                if move>v[s][0]:
                    v[s]=(move,a)
            d = max(d, abs(v[s][0] - v_new[s][0]))
        if d < epsilon * (1 - g) / g:
            return v_new