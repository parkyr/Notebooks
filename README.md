# Notebooks / Repository to track learnings

# Toy problem 1 : Flow Optimization
## Problem Details
Formulate and solve flow optimization toy problem as MINLP and QUBO <br><br>
<img src=toy1.png>

Obj Fcn: Minimize the total cost of flow <br> 
Constraints: <br>
&nbsp; 1. Flow conservation: The flow into each node equals the flow out of each node <br>
&nbsp; 2. At crossroads, the flow must take one of the two possible paths (binary constraint) <br>

### Solution
Best known objective value: 30 
Flow path: 
        f : flow on each edge
            Size=7, Index=edges
            Key : Lower : Value : Upper : Fixed : Stale : Domain
             f1 :     0 :   2.0 :  None : False : False : NonNegativeReals
             f2 :     0 :   2.0 :  None : False : False : NonNegativeReals
             f3 :     0 :   2.0 :  None : False : False : NonNegativeReals
             f4 :     0 :   0.0 :  None : False : False : NonNegativeReals
             f5 :     0 :   2.0 :  None : False : False : NonNegativeReals
             f6 :     0 :   0.0 :  None : False : False : NonNegativeReals
             f7 :     0 :   2.0 :  None : False : False : NonNegativeReals
        y : binary decision variable for s3 to s4 path
            Size=1, Index=None
            Key  : Lower : Value : Upper : Fixed : Stale : Domain
            None :     0 :   1.0 :     1 : False : False : Binary
        z : binary decision variable for s3 to s5 path
            Size=1, Index=None
            Key  : Lower : Value : Upper : Fixed : Stale : Domain
            None :     0 :  -0.0 :     1 : False : False : Binary


