"""
Toy problem 1: Formulate and solve flow optimization toy problem as MINLP and QUBO
Obj Fcn: Minimize the total cost of flow
Constraints:
    1. Flow conservation: The flow into each node equals the flow out of each node
    2. At crossroads, the flow must take one of the two possible paths (binary constraint)

"""

import pyomo.environ as pyo
import numpy as np 

## MINLP Formulation

# Problem data 
flow_network = {'s1_s2': ('s1', 's2'), 's2_s3': ('s2', 's3'), 
                's3_s4': ('s3','s4'), 's3_s5': ('s3', 's5'), 
                's4_s6': ('s4', 's6'), 's5_s6': ('s5', 's6'),
                's6_s7': ('s6', 's7')}

flow_cost = {'s1_s2': 1, 's2_s3': 1, 's3_s4': 3, 's3_s5': 8, 's4_s6': 4, 's5_s6': 9, 's6_s7': 1}

# penalty weights for binary constraints
Ky = 10
Kz = 4

# Model
model = pyo.ConcreteModel(doc='Flow Optimization Problem')

# Sets
model.nodes = pyo.Set(initialize=['s1', 's2', 's3', 's4', 's5', 's6', 's7'], doc='nodes') 
model.edges = pyo.Set(initialize=flow_network.keys(), doc='edges')

# Decision Variables  
model.f = pyo.Var(model.edges, domain=pyo.NonNegativeReals, doc='flow on each edge')
model.y = pyo.Var(domain=pyo.Binary, doc='binary decision variable for s3 to s4 path')
model.z = pyo.Var(domain=pyo.Binary, doc='binary decision variable for s3 to s5 path')

# Parameters
model.fcost = pyo.Param(model.edges, initialize=flow_cost, doc='cost of flow on each edge')

# Objective Function (minimize cost)
model.totalcost = pyo.Objective(expr=sum(model.f[e]*model.fcost[e] for e in model.edges) + Ky*model.y + Kz*model.z, sense=pyo.minimize)

# Constraints 

# Disjunction Constraint
def disjunction_rule(model):
    return model.y + model.z <= 1
model.disjunction = pyo.Constraint(rule=disjunction_rule, doc='disjunction constraint')


# Flow Conservation Constraints
def flow_conservation_rule(model, node):
    inflow = sum(model.f[edge] for edge in model.edges if flow_network[edge][1] == node)
    outflow = sum(model.f[edge] for edge in model.edges if flow_network[edge][0] == node)
    if node == 's1':
        return outflow == 10  # source node
    elif node == 's7':
        return inflow == 10  # sink node
    else:
        return inflow == outflow  # intermediate nodes

model.flow_conservation = pyo.Constraint(model.nodes, rule=flow_conservation_rule, doc='flow conservation constraints')

# Linking binary variables with flow
model.crossroad1 = pyo.Constraint(expr=model.f['s3_s4'] <= model.y * 1e6, doc='linking y with s3 to s4')
model.crossroad2 = pyo.Constraint(expr=model.f['s3_s5'] <= model.z * 1e6, doc='linking z with s3 to s5')

# Ensure there is no flow in the path that is not chosen
model.crossroad3 = pyo.Constraint(expr=model.f['s3_s4'] >= model.y * 1e-6, doc='linking y with s3 to s4 lower bound')
model.crossroad4 = pyo.Constraint(expr=model.f['s3_s5'] >= model.z * 1e-6, doc='linking z with s3 to s5 lower bound')


# Solve the model using a solver
solver = pyo.SolverFactory('gurobi',solver_io='python')
results = solver.solve(model, tee=True)

model.display()