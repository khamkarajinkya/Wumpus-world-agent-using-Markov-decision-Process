Fully observable stochastic version of Wumpus world -

State Space (‘S’) : All the tiles on the grid except the walls of the grid

List of actions: {‘do nothing’, ‘left’, ‘right’, ‘up’, ‘down’, ‘shoot left’, ‘shoot right’, ‘shoot up’, ‘shoot down’}.

```
‘do nothing’: This action does not change anything in the grid environment
‘left’: Move one tile to the left from current grid position
‘right’: Move one tile to the right from current grid position
‘up’: Move one tile above the current grid position
‘down’: Move one tile below the current grid position
‘shoot left’: Shoot an arrow to the left in the same row, the arrow continues till it either hits the wumpus or
the wall
‘shoot right’: Shoot an arrow to the right in the same row, the arrow continues till it either hits the wumpus
or the wall
‘shoot up’: Shoot an arrow to the up in the same column, the arrow continues till it either hits the wumpus
or the wall
‘shoot down’: Shoot an arrow to the down in the same column, the arrow continues till it either hits the
wumpus or the wall

The Transition function T: ({State,Action} → State

If the intended direction of movement is the same as the action then the transition probability is 0.9
T(S,A,S') = 0.9 iff S'_direction == A_direction
otherwise 0.1 in any of the remaining directions
T(S,A,S') = 0.1 iff S'_direction /= A_direction

If the agent moves into the wall, the action which leads the agent into the wall has a probability of 0.1
T(S,A,S')= 0 iff S'_direction == A_direction and s'_direction == wall (deterministic)

If the agent is in the same row or column as the Wumpus, agent shoots the wumpus with a probability of 1 (deterministic)

If the action is ‘do nothing’ and the agent is in the same state as goal, the function returns a probability
of 1 (deterministic)

If the agent’s moves leads it into a pit or wumpus, the action which leads the agent into the threat has
a probability of 0.1 
T( S,A,S') = 0.1 iff S'_direction == A_direction and S'_direction = pit | wumpus (undesired move)

The Reward Function:
Agent receives the award of 100 if he gets the gold
Agent receives an award of -100 if he finds himself in the tile containing the Wumpus or the tile containing the pits
Agent receives a -1 in every other state 
If the agent shoots the wumpus, the state containing the wumpus is turned into a normal state with reward of -1
```
