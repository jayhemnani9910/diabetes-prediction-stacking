"""Check that an executed copy of project.ipynb reports the test accuracies in the README.

Usage: python tests/check_results.py path/to/executed/project.ipynb
"""
import json
import re
import sys

EXPECTED = {
    "Decision Tree Classifier": 0.75758,
    "Support Vector Machine": 0.74459,
    "Gaussian NB": 0.74026,
    "Random Forest Classifier": 0.74026,
    "Logistic Regression Classifier": 0.73593,
    "Our Model": 0.71429,
    "ANN": 0.68398,
}

PATTERN = re.compile(r"Accuracy of '(.+?)', for Diabetes Prediction \(On Testing Data\) is : ([0-9.]+)")


def main(path):
    with open(path, encoding="utf-8") as f:
        nb = json.load(f)
    found = {}
    for cell in nb["cells"]:
        for out in cell.get("outputs", []):
            if out.get("output_type") == "error":
                sys.exit(f"cell raised {out['ename']}: {out['evalue']}")
            for name, value in PATTERN.findall("".join(out.get("text", ""))):
                found[name] = float(value)
    failed = False
    for name, want in EXPECTED.items():
        got = found.get(name)
        ok = got is not None and abs(got - want) < 1e-5
        failed |= not ok
        print(f"{'ok  ' if ok else 'FAIL'} {name}: expected {want}, got {got}")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main(sys.argv[1])
