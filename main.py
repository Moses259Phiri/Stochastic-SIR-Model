import numpy as np
import matplotlib.pyplot as plt

# Parameters
N = 1000  # Total population
beta = 0.3  # Infection rate
gamma = 0.1  # Recovery rate
I0 = 1  # Initial number of infectious individuals
R0 = 0  # Initial number of recovered individuals
S0 = N - I0 - R0  # Initial number of susceptible individuals
days = 100  # Number of days to simulate

# Initialize arrays to track the states
S = [S0]
I = [I0]
R = [R0]

# Simulation
for _ in range(days):
    current_S = S[-1]
    current_I = I[-1]
    current_R = R[-1]
    
    # Probabilities of events
    p_infect = beta * current_I / N  # Probability a susceptible becomes infected
    p_recover = gamma  # Probability an infected person recovers

    # New infections and recoveries
    new_infections = np.sum(np.random.rand(current_S) < p_infect)
    new_recoveries = np.sum(np.random.rand(current_I) < p_recover)

    # Update states
    next_S = current_S - new_infections
    next_I = current_I + new_infections - new_recoveries
    next_R = current_R + new_recoveries

    S.append(next_S)
    I.append(next_I)
    R.append(next_R)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(S, label='Susceptible')
plt.plot(I, label='Infectious')
plt.plot(R, label='Recovered')
plt.title('Stochastic SIR Model')
plt.xlabel('Days')
plt.ylabel('Population')
plt.legend()
plt.grid()
plt.show()
