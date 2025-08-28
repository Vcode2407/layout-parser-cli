import yaml

def load_rules(file):
    with open(file) as f:
        return yaml.safe_load(f)

def check_spacing(blocks, min_spacing):
    for i in range(len(blocks) - 1):
        if abs(blocks[i+1] - blocks[i]) < min_spacing:
            print(f"Violation: spacing too small between block {i} and {i+1}")

if __name__ == "__main__":
    # Example usage with dummy layout block positions
    rules = load_rules("rules.yaml")
    layout_blocks = [0.0, 0.1, 0.25, 0.35]
    check_spacing(layout_blocks, rules["spacing_min"])
