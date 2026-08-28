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

- On a fresh run of the notebook, "Our Model" reaches 77.49% test accuracy, which is higher than every one of the 6 individual models: Naive Bayes 74.03%, Random Forest 74.03%, Logistic Regression 74.03%, SVM 73.59%, ANN 71.86%, Decision Tree 71.43%.

- The base models are built without a fixed random seed, so these figures move by a point or two from run to run. The cell outputs saved inside `project.ipynb` come from an older run on an older scikit-learn and no longer match the current code. Run the notebook yourself to regenerate them. `REHAB.md` has the command.

## Contributors & Authors

Vinay Khilwani, Vasu Gondaliya, Shreya Patel, Jay Hemnani & Bhuvan Gandhi
