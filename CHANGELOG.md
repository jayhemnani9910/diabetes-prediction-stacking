# Changelog

All notable changes to this project are listed here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Added
- CI that lints the notebook, runs every cell and checks the test accuracies against the README.
- `requirements.txt` with the versions the notebook was last run with.
- Contributing guide, issue and pull request templates.

## 2026-10-06

### Fixed
- Logistic Regression, SVM and ANN now scale features first.
- Every search uses 10-fold CV with 3 repeats.
- The ROC plot includes SVM.
- README and notebook numbers match the stored run.

### Added
- Results table at the top of the notebook.

## 2026-08-28

### Fixed
- Test set is imputed with training statistics, and Pregnancies is no longer imputed.
- Removed invalid values from the SVM and decision tree grids, and the deprecated Logistic Regression penalty parameter.
- Naive Bayes learns class priors from the data.
- Removed lines that scored each model against itself.
- Every model is seeded, so two runs give the same numbers.
- README reported 82.68% and named the wrong meta model. It now reports the measured result: stacking does not beat the base models.
- The Pages workflow had invalid YAML and never ran.

## 2025-12-18

### Added
- Notebook, dataset and README from the 2021 paper.
- GitHub Pages workflow that publishes the executed notebook.
