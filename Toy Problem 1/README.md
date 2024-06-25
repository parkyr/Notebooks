## Toy problem 1 : Flow Optimization
### Problem Details
Formulate and solve flow optimization toy problem as MINLP and QUBO <br><br>
<img src=toy1.png>

Obj Fcn: Minimize the total cost of flow <br> 
Constraints: <br>
&nbsp; 1. Flow conservation: The flow into each node equals the flow out of each node <br>
&nbsp; 2. At crossroads, the flow must take one of the two possible paths (binary constraint) <br>

### Solution
***MINLP*** <br>
(solver: Gurobi) <br> 
Best known objective value: 30 <br>
Optimal solution values: <br>
|  Variables | f1 | f2 | f3 | f4 | f5 | f6 | f7 | y | z |
|------------|----|----|----|----|----|----|----|---|---|
|    Value   | 2  | 2  | 2  | 0  | 2  | 0  | 2  | 1 | 0 |

