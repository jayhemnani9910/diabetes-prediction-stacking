# Rehab notes

## Safe run command

```
OUT=$(mktemp -d) && uv run --no-project \
  --with scikit-learn --with pandas --with numpy \
  --with seaborn --with matplotlib \
  --with nbconvert --with nbformat --with ipykernel \
  jupyter nbconvert --to notebook --execute project.ipynb \
  --output-dir "$OUT" --ExecutePreprocessor.timeout=3600 && echo "wrote $OUT/project.ipynb"
```

This runs every cell of the notebook top to bottom in a throwaway environment and
writes the executed copy outside the repo, so the committed `project.ipynb` is not
modified. Nothing here touches the network, spends money, or publishes.

Note: the repo declares no dependencies anywhere, so the command above pins nothing.
It resolves to whatever is current. That is deliberate for a rehab run, because the
question being asked is whether the notebook still works today.

## What success looks like

Exits 0. Every cell runs with no exception. Nothing in the output says "fits failed".
The last cell prints two lines, of the form:

```
- Accuracy of 'Our Model', for Diabetes Prediction (On Training Data) is : 0.8xxxx
- Accuracy of 'Our Model', for Diabetes Prediction (On Testing Data) is : 0.7xxxx
```

Every model is seeded, so two runs give the same numbers. The current numbers live in README.md.

The stored cell outputs are the GitHub Pages demo, so re-run and commit them whenever a code cell changes.

The run takes a while. The stacking cell refits all five search objects on 4 CV folds
each, so it repeats the whole hyperparameter search several times over.

## Test command

None. This repo has no test suite, no linter config, and no CI beyond the Pages deploy.

## Do not run

- `.github/workflows/pages.yml` and anything that triggers it. It publishes to GitHub
  Pages at https://jayhemnani9910.github.io/diabetes-prediction-stacking/
- `git push`. The live demo page is built from whatever lands on `main`.

## Needs credentials

None. The dataset is committed as `diabetes.csv` and nothing reaches the network.

## Known broken, leave alone

Nothing declared yet.
