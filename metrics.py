from sklearn.metrics import accuracy_score, f1_score


def metrics(y_true, y_pred):
    """
    Calculation of 4 metrics:
        Acc - vanilla Accuracy score
        F1 macro - the macro-averaged F1 score
        F1 +- macro - the macro-averaged F1 score ignoring neutral class
        F1 +- micro - the micro-averaged F1 score ignoring neutral class
    :param y_true: actual labels
    :param y_pred: predicted labels
    :return: 4 values in tuple
    """
    acc = round(accuracy_score(y_true, y_pred) * 100, 2)
    f1_macro = round(f1_score(y_true, y_pred, average='macro') * 100, 2)

    y_true_neutral = []
    y_pred_neutral = []

    for i in range(len(y_true)):
        if y_true[i] != 0:
            y_true_neutral.append(y_true[i])
            y_pred_neutral.append(y_pred[i])

    f1_posneg_macro = round(f1_score(y_true_neutral, y_pred_neutral, average='macro') * 100, 2)
    f1_posneg_micro = round(f1_score(y_true_neutral, y_pred_neutral, average='micro') * 100, 2)

    return acc, f1_macro, f1_posneg_macro, f1_posneg_micro