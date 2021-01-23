import os
import settings
import pandas as pd
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
from sklearn import metrics


def read():
    train = pd.read_csv(os.path.join(settings.PROCESSED_DIR, "train.csv"))
    return train


def cross_validate(train):
    clf = LogisticRegression(random_state=1, class_weight="balanced", solver='saga', n_jobs=-1, dual=False, tol=0.01)

    # Get the names of the columns to use as predictors
    predictors = train.columns.tolist()
    predictors = [p for p in predictors if p not in settings.NON_PREDICTORS]

    predictions = model_selection.cross_val_predict(estimator=clf, X=train[predictors], y=train[settings.TARGET],
                                                    cv=settings.CV_FOLDS, n_jobs=-1)

    return predictions


def compute_error(target, predictions):
    return metrics.accuracy_score(target, predictions)


def compute_false_negatives(target, predictions):
    """Compute the false negatives rate:
    FNR=FN/(FN+TP)=FN/P, where:
    FN: false negatives, TP: true positives, P: positives"""
    df = pd.DataFrame({"target": target, "predictions": predictions})
    return df[(df["target"] == 1) & (df["predictions"] == 0)].shape[0] / (df[(df["target"] == 1)].shape[0] + 1)


def compute_false_positives(target, predictions):
    """Compute the false positives rate (false alarm rate):
    FPR=FP/(TN+FP)=FP/N, where:
    FP: false positives, TN: true negatives, N: negatives"""
    df = pd.DataFrame({"target": target, "predictions": predictions})
    return df[(df["target"] == 0) & (df["predictions"] == 1)].shape[0] / (df[(df["target"] == 0)].shape[0] + 1)


if __name__ == "__main__":
    train = read()
    predictions = cross_validate(train)
    error = compute_error(train[settings.TARGET], predictions)
    fn = compute_false_negatives(train[settings.TARGET], predictions)
    fp = compute_false_positives(train[settings.TARGET], predictions)
    print("Accuracy Score: {}".format(error))
    print("False Negatives: {}".format(fn))
    print("False Positives: {}".format(fp))
