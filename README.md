Used an optimal value function to find the optimal policy for a set of states. The value function is
defined using an iterative algorithm V alueIteration that can be shown to converge to the correct V ∗ value.
The action associated with the optimal value is the optimal action for that state.
The algorithm uses the Bellman equation and works in the following manner

```
  Repeat
  U ← U' ; ρ ← 0
  for each state S in S do the following
  U'[s] ← R(s) + γ max_a(sum (P (s'|s,a) U[s']))
  if [U'[s] − U[s]] > ρ then ρ ← [U'[s] − U[s]]
  Until ρ < epsilon*((1 − γ)/γ)
  return U
```

epsilon is the maximum error allowed in the utility of any state

ρ is the maximum change in utility of any state in an iteration.

It is not obvious when to stop the value iteration algorithm. We continue to perform the algorithm till
difference in the successive value function states does not fall below a certain set threshold using ```epsilon*((1 − γ)/γ)```, if
the successive value function values for a certain state fall below the threshold, we are certain that the value
function for a state is not changing.
The value vector stores a tuple of state action and state value and this eases retrieval of the best action
associated with every state using the following action
```
Q'[s,a] ← R(s) + γ max_a(sum (P (s'|s,a) U[s']))
π`(s) = argmax_ Q*(s,a) #all possible statregies
π`is the optimal policy.
```
