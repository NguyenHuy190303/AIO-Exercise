def precision(tp, fp):
    if tp + fp == 0:
        return 0  # Avoid division by 0
    else:
        return tp / (tp + fp)

def recall(tp, fn):
    if tp + fn == 0:
        return 0  # Avoid division by 0
    else:
        return tp / (tp + fn)

def f1_score(precision, recall):
    if precision + recall == 0:
        return 0  # Avoid division by 0
    else:
        return 2 * (precision * recall) / (precision + recall)

def evaluate_model(tp, fp, fn):
    # Check input types
    if not isinstance(tp, int):
        print("tp must be int")
        return
    if not isinstance(fp, int):
        print("fp must be int")
        return
    if not isinstance(fn, int):
        print("fn must be int")
        return

    # Check input values
    if any(x <= 0 for x in [tp, fp, fn]):
        print("tp, fp, and fn must be greater than zero")
        return

    # Calculate and display results
    p = precision(tp, fp)
    r = recall(tp, fn)
    f1 = f1_score(p, r)

    print(f"precision is {p}")
    print(f"recall is {r}")
    print(f"f1-score is {f1}")

def get_input():
    tp = int(input("Enter tp: "))
    fp = int(input("Enter fp: "))
    fn = int(input("Enter fn: "))
    return tp, fp, fn

# Usage example
tp, fp, fn = get_input()
evaluate_model(tp, fp, fn)