[![Live Demo](https://img.shields.io/badge/Live%20Demo-Open-2ea44f?style=for-the-badge)](https://jayhemnani9910.github.io/diabetes-prediction-stacking/)

# Diabetes Prediction using Stacking (Stacked Generalization)

- The architecture of a stacking model involves two or more base models, often referred to as level-0 models, and a meta-model that combines the predictions of the base models, referred to as a level-1 model.

- We have used the following models as level-0 models:
1. Gaussian Naive Bayes Classifier
2. Random Forest Classifier (With hyperparameter tuning, 10-fold CV with 3 repeats)
3. Decision Tree Classifier (With hyperparameter tuning, 10-fold CV with 3 repeats)
4. SVM Classifier (With hyperparameter tuning, 10-fold CV with 3 repeats)
5. ANN Model (With hyperparameter tuning, 10-fold CV with 3 repeats)
6. Logisitic Regression (With hyperparameter tuning, 10-fold CV with 3 repeats)

- Logistic Regression, SVM and ANN scale the features first (StandardScaler), since all three are sensitive to feature scale. The tree models and Naive Bayes use the raw features.

- We have used a "Random Forest" Model (from python's 'scikit' module) as the level-1 model, with 4-fold CV.

- Every model now sets `random_state = 42`, so the notebook gives the same answer every time. This was checked by running it twice and comparing all 19 reported numbers.

- Test accuracy: Decision Tree 75.76%, SVM 74.46%, Gaussian NB 74.03%, Random Forest 74.03%, Logistic Regression 73.59%, "Our Model" 71.43%, ANN 68.40%.

- So stacking did not beat the 6 individual models here. It comes below five of them. Earlier, before the seeds were fixed, "Our Model" ranged from 72% to 77% across runs and its position in that list moved with it.

- Worth knowing why the ranking is not worth much either way. The test set is 231 rows, so one percentage point is about 2 patients. Most of these models sit inside a couple of points of each other, which is noise at this size. This dataset and this setup are not enough to declare a winner, and the interesting part of the project is the stacking construction rather than the score.

## Contributors & Authors

Vinay Khilwani, Vasu Gondaliya, Shreya Patel, Jay Hemnani & Bhuvan Gandhi
