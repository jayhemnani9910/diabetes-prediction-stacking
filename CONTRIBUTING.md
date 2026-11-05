# Contributing

This repo is the code for one paper, so most useful changes are fixes to the notebook, its numbers or its explanations.

## Setup

```
git clone https://github.com/jayhemnani9910/diabetes-prediction-stacking.git
cd diabetes-prediction-stacking
python -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
```

## Run and check

```
jupyter nbconvert --to notebook --execute project.ipynb --output-dir out
python tests/check_results.py out/project.ipynb
ruff check project.ipynb tests
```

The first command runs every cell and writes the executed copy to `out/`, so the committed notebook is left alone. It takes a few minutes, most of it in the stacking cell. The second checks the test accuracies against the README. CI runs all three on every push and pull request.

## Changing results

Every model is seeded, so the numbers should not move unless the code does. If your change moves them, update in one pull request:

- the stored outputs in `project.ipynb` (copy over the executed notebook from `out/`)
- the results table in the notebook's second cell and in `README.md`
- `EXPECTED` in `tests/check_results.py`

The stored outputs are also what the GitHub Pages site shows.

## Style

Keep the existing code style in the notebook. One change per pull request, on a branch, against `main`. Say in the description what changed and whether the numbers moved.

## Bugs

Open an issue with the bug template. Include the error or the numbers you got, your Python and scikit-learn versions, and the commit.

I try to reply to issues within a few days.
