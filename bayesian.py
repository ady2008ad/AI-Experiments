import itertools

# Define CPTs
P_Raining = {True: 0.3, False: 0.7}
P_HasWeapon = {True: 0.6, False: 0.4}

# CPT for EnemyAttack: P(Attack | Raining, HasWeapon)
P_EnemyAttack = {
    (True, True): 0.9,
    (True, False): 0.6,
    (False, True): 0.7,
    (False, False): 0.1
}

def compute_joint_distribution():
    """Compute the full joint distribution P(R, W, A)."""
    joint = {}
    for R, W, A in itertools.product([True, False], repeat=3):
        # Compute P(R, W, A)
        p_r = P_Raining[R]
        p_w = P_HasWeapon[W]
        p_a = P_EnemyAttack[(R, W)] if A else (1 - P_EnemyAttack[(R, W)])
        joint[(R, W, A)] = p_r * p_w * p_a
    return joint

def compute_marginal_attack():
    """Compute P(EnemyAttack=True)"""
    joint = compute_joint_distribution()
    p_attack_true = sum(prob for (R, W, A), prob in joint.items() if A)
    return p_attack_true

if __name__ == "__main__":
    joint = compute_joint_distribution()
    print("🧮 Joint Probability Distribution (P(R, W, A)):\n")
    for k, v in joint.items():
        print(f"Raining={k[0]}, Weapon={k[1]}, Attack={k[2]}  →  P={v:.4f}")
    
    p_attack = compute_marginal_attack()
    print(f"\n🔹 Marginal Probability: P(EnemyAttack=True) = {p_attack:.4f}")
