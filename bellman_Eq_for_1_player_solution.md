If we make a model where reward is -1 for any move, and we backpropagate from final state with V^T = 0, solution will be policy that moves toward highest value (smallest negative).

Current state is described by position of horses p = [position horse 1, position horse 2] and last roll of the dice, n = 1,2,3,4,5,6

                reward                 probability     Value of next state, position dependant on last roll and action. 
Q(s) = Q(p, n) = -1 +  sum_{ i =1->6} (     1/6      *  V(p'(p, n, a), i))

V(s) = max_{a}( Q(s))


So if we can find p'(p,n,a), this can be solved. should be possible to do from our horse class. 

if not, a function p'(p,n,a) can just be constructed as p' = p + a * n, if a = [1 if actions is use horse 1, 1 if horse 2], and then also addressing every edgecase, p = [0,0], p = [x, 0], or  p +n > F, F is final length of board.

I've tried this in main_Victor.py, but a bit ugly implemented



