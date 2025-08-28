import yaml

def load_rules(file):
    with open(file) as f:
        return yaml.safe_load(f)

def check_spacing(blocks, min_spacing):
    violations = []
    for i in range(len(blocks) - 1):
        spacing = abs(blocks[i+1] - blocks[i])
        if spacing < min_spacing:
            severity = "Critical" if spacing < min_spacing * 0.8 else "Warning"
            msg = f"[{severity}] Spacing violation between block {i} and {i+1}: {spacing:.3f} < {min_spacing}"
            print(msg)
            violations.append(msg)
    return violations

def write_report(violations, filename="violations.txt"):
    with open(filename, "w") as f:
        f.write("DRC Violation Report\n\n")
        for v in violations:
            f.write(v + "\n")
        f.write(f"\nTotal Violations: {len(violations)}")

if __name__ == "__main__":
    rules = load_rules("rules.yaml")
    layout_blocks = [0.0, 0.1, 0.25, 0.35]
    violations = check_spacing(layout_blocks, rules["spacing_min"])
    write_report(violations)
