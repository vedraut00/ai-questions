import numpy as np

# Define the conditional probabilities for the Bayesian Belief Network
P_A = {'yes': 0.8, 'no': 0.2}
P_C = {'yes': 0.5, 'no': 0.5}

# Conditional probabilities for Grade (G) given Aptitude Skills (A) and Coding Skills (C)
P_G_given_A_C = {
    ('Good', 'yes', 'yes'): 0.9,
    ('Good', 'yes', 'no'): 0.7,
    ('Good', 'no', 'yes'): 0.6,
    ('Good', 'no', 'no'): 0.3,
    ('OK', 'yes', 'yes'): 0.1,
    ('OK', 'yes', 'no'): 0.3,
    ('OK', 'no', 'yes'): 0.4,
    ('OK', 'no', 'no'): 0.7,
}

# Monte Carlo simulation function
def monte_carlo_simulation(target_grade, num_samples=10000):
    count_target_grade = 0

    for _ in range(num_samples):
        # Sample Aptitude Skills (A) and Coding Skills (C)
        aptitude = 'yes' if np.random.rand() < P_A['yes'] else 'no'
        coding = 'yes' if np.random.rand() < P_C['yes'] else 'no'

        # Determine Grade (G) based on sampled A and C
        p_grade_good = P_G_given_A_C[('Good', aptitude, coding)]
        grade = 'Good' if np.random.rand() < p_grade_good else 'OK'

        # Count if the grade matches the target grade
        if grade == target_grade:
            count_target_grade += 1

    # Estimate probability of the target grade
    return count_target_grade / num_samples

# Run the Monte Carlo simulation
target_grade = 'Good'
estimated_probability = monte_carlo_simulation(target_grade, num_samples=10000)
print(f"Estimated P(Grade={target_grade}): {estimated_probability:.4f}")
