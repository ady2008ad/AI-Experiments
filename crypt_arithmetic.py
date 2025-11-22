import itertools

# =======================
# PART 1: CRYPTARITHMETIC
# =======================

def is_valid(mapping):
    S, E, N, D, M, O, R, Y = [mapping[c] for c in "SENDMORY"]
    if S == 0 or M == 0:
        return False
    send = 1000 * S + 100 * E + 10 * N + D
    more = 1000 * M + 100 * O + 10 * R + E
    money = 10000 * M + 1000 * O + 100 * N + 10 * E + Y
    return send + more == money

def solve_cryptarithmetic():
    letters = "SENDMORY"
    for perm in itertools.permutations(range(10), len(letters)):
        mapping = dict(zip(letters, perm))
        if is_valid(mapping):
            send = 1000*mapping['S'] + 100*mapping['E'] + 10*mapping['N'] + mapping['D']
            more = 1000*mapping['M'] + 100*mapping['O'] + 10*mapping['R'] + mapping['E']
            money = 10000*mapping['M'] + 1000*mapping['O'] + 100*mapping['N'] + 10*mapping['E'] + mapping['Y']
            print("\n🧮 CRYPTARITHMETIC SOLUTION:")
            print(f"SEND + MORE = MONEY")
            print(f"{send} + {more} = {money}")
            print(f"Mapping: {mapping}")
            return money
    return None


# =================================
# PART 2: INFERENCE (RULE-BASED AI)
# =================================

# Forward Chaining
def forward_chaining(facts, rules):
    inferred = set(facts)
    changed = True
    print("\n🔁 FORWARD CHAINING PROCESS:")
    while changed:
        changed = False
        for premises, conclusion in rules:
            if all(p in inferred for p in premises) and conclusion not in inferred:
                print(f"Inferred: {conclusion} (from {premises})")
                inferred.add(conclusion)
                changed = True
    return inferred

# Backward Chaining
def backward_chaining(goal, facts, rules, indent=0):
    print("  " * indent + f"Trying to prove: {goal}")
    if goal in facts:
        print("  " * indent + f"✔ {goal} is a known fact.")
        return True
    for premises, conclusion in rules:
        if conclusion == goal:
            print("  " * indent + f"Using rule: {premises} → {conclusion}")
            if all(backward_chaining(p, facts, rules, indent+1) for p in premises):
                print("  " * indent + f"✔ Proven {goal} using {premises}")
                return True
    print("  " * indent + f"❌ Cannot prove {goal}")
    return False


# ===================================
# PART 3: COMBINED AI PUZZLE SCENARIO
# ===================================

def main():
    print("🧩 Welcome to CRYPTO-CHAIN AI 🧩")
    print("Step 1: Solving the cryptarithmetic puzzle...")
    money_value = solve_cryptarithmetic()

    # Convert the cryptarithmetic result into symbolic facts
    facts = set()
    if money_value:
        print(f"\nDetected MONEY value: {money_value}")
        if money_value > 10000:
            facts.add("large_money")
        else:
            facts.add("small_money")

    # Define rules for inference
    rules = [
        (["large_money"], "vault_opens"),
        (["vault_opens"], "alarm_triggers"),
        (["alarm_triggers"], "guards_alerted")
    ]

    # Forward chaining reasoning
    inferred_facts = forward_chaining(facts, rules)
    print("\n✅ Final inferred facts:", inferred_facts)

    # Backward chaining reasoning
    print("\n🔙 Backward chaining: Is the vault opened?")
    goal = "vault_opens"
    result = backward_chaining(goal, facts, rules)
    print("\nFinal verdict:", "Vault opens ✅" if result else "Vault remains closed ❌")


if __name__ == "__main__":
    main()
