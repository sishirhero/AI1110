import numpy as np

def simulate_coin_toss(num_trials):
    # Toss the coin twice for all trials
    results = np.random.choice(['H', 'T'], size=(num_trials, 2))

    # Count the occurrences of at most one head
    count_at_most_one_head = np.sum(np.sum(results == 'H', axis=1) <= 1)

    # Calculate the probability
    probability = count_at_most_one_head / num_trials

    return probability

# Theoretical probability
theoretical_probability = 3/4

# Run the simulation with 1,000,000 trials
num_trials = 1000000
simulated_probability = simulate_coin_toss(num_trials)

print(f"Theoretical probability: {theoretical_probability}")
print(f"Simulated probability: {simulated_probability}")