def first_order_decay(initial_concentration, rate_constant, time_steps):
    """
    Simulates chemical reaction kinetics and exponential decay.
    C(t) = C0 * exp(-k * t)
    """
    import math
    profile = []
    for t in time_steps:
        conc = initial_concentration * math.exp(-rate_constant * t)
        profile.append((t, round(conc, 5)))
    return profile

if __name__ == "__main__":
    c0 = 1.0       # Initial concentration (mol/L)
    k = 0.05       # Reaction rate constant (s^-1)
    times = [0, 5, 10, 15, 20, 30]
    
    simulation = first_order_decay(c0, k, times)
    for step, val in simulation:
        print(f"Time: {step}s -> Concentration: {val} M")
