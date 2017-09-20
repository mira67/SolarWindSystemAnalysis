#Implementation of PSO method
#Author: Qi Liu
#Email: qliu.hit@gmail.com

import numpy as np

# Loss function
def sphere(x):
    z = np.sum(np.square(x))
    return z
    
class pbest:
    position = 0
    cost = 0
    
class GlobalBest:
    cost = 0

class particle:
    position = 0
    velocity = 0
    cost = 0
    best = pbest()

def pso(x):
    # Problem definition
    CostFunction = sphere(x) # Cost Function
    
    nVar = 5 # Number of unkniwn Decision Variables
    
    VarSize = np.array([1,nVar]) # Matrix Size of Decision Variables
    
    VarMin = -10 # Lower Bound of Decision Variable
    VarMax = 10 # Upper Bound of Decision Variable
    
    # Prameters of PSO
    MaxIt = 100 # Maximum Number of Iterations
    nPop = 50 # Population Size (Swarm Size)
    w = 1 # Intertia Coefficent
    wdmap = 0.99 # Damping inertia coefficient
    c1 = 2 # Personal Accelration Coeffcient
    c2 = 2 # Social Acceleration Coeffcient
    
    # Initialization
    
    # The particle template
    empty_particle = particle()
    empty_particle.position = 0
    empty_particle.velocity = 0
    empty_particle.cost = 0
    empty_particle.best.position = 0
    empty_particle.best.velocity = 0
    
    # Create population array
    particles = 0# repeat for all particles, repmat(empty_particle, nPop, 1)
    
    # Initialize global best
    gBest = GlobalBest()
    gBest.cost = inf
    
    # Initialize population members
    for i in range(0,nPop):
        
        # generate random solution
        particles(i).position = unifrnd(VarMin, VarMax, VarSize)
        # Initialize veolocity
        particles(i).velocity = zeros(VarSize)
        # Evaluation
        particles(i).cost = CostFunction(particles(i).position)
        # Update the personal best
        particles(i).best.position = particles(i).position
        particles(i).best.cost = particle(i).cost
        # Update global best
        if particles(i).best.cost < gBest.cost:
            gBest.cost = particles(i).best.cost
    
    # Array to hold best cost value on each iteration
    BestCosts = zeros(MaxIt, 1)
    
    # Main loop of PSO
    for it in range(0, MaxIt):
        
        for i in range(0, nPop):
            r1 = rand(VarSize)
            r2 = rand(VarSize)
            
            # update velocity
            particles(i).velocity = w*particles(i).velocity
            + r1*c1*(particles(i).best.position - particles(i).position)
            + r2*c2*(gBest.position - particle(i).position)
            
            # update position
            particles(i).position = particles(i).position + particles(i).velocity
            
            # update evalution
            particles(i).cost = CostFunction(particles(i).position)
            
            # update personal best
            if particles(i).cost < particles(i).best.cost:
                particles(i).best.position = particles(i).position
                particles(i).best.cost = particles(i).cost
        
        # store the best cost value
        BestCosts(it) = gBest.cost
        print('Iteration, ', it, 'Best Cost = ', BestCosts[it]) 
        
        # Damping inertia coefficient
        w = w*wdamp  
         
    # Results
    figure
    plot(BestCosts) # semilog for better display
    xlabel('Iteration')
    ylabel('Best Cost')
    
    return