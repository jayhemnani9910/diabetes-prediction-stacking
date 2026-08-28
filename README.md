[![Live Demo](https://img.shields.io/badge/Live%20Demo-Open-2ea44f?style=for-the-badge)](https://jayhemnani9910.github.io/diabetes-prediction-stacking/)

# Diabetes Prediction using Stacking (Stacked Generalization)

- The architecture of a stacking model involves two or more base models, often referred to as level-0 models, and a meta-model that combines the predictions of the base models, referred to as a level-1 model.

- We have used the following models as level-0 models:
1. Gaussian Naive Bayes Classifier (With hyperparameter tuning) 
2. Random Forest Classifier (With hyperparameter tuning & 3-fold CV)
3. Decision Tree Classifier (With hyperparameter tuning & 3-fold CV)
4. SVM Classifier (With hyperparameter tuning & 3-fold CV)
5. ANN Model (With hyperparameter tuning & 3-fold CV)
6. Logisitic Regression (With hyperparameter tuning & 3-fold CV)

- We have used a "Random Forest" Model (from python's 'scikit' module) as the level-1 model, with 4-fold CV.

- How well does the stacking model do? The honest answer is that it moves a lot. Two runs of identical code gave 77.49% and 72.29% test accuracy. On the first it beat all 6 individual models. On the second, 4 of the 6 beat it.

- That spread comes from the models setting no random seed, so every execution gives a different answer. Read any single number in this notebook as one sample rather than a result. The saved cell outputs are from one run, and they are what the demo page shows. `REHAB.md` has the command to run it yourself.

## Contributors & Authors

Vinay Khilwani, Vasu Gondaliya, Shreya Patel, Jay Hemnani & Bhuvan Gandhi
