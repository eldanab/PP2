def solve(numheads, numlegs):
 r = (numlegs - 2*numheads)/2
 c = numheads - r
 print("Rabbits:", int(r))
 print("Chickens:", int(c))
solve(35, 94)