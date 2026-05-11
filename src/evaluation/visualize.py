import matplotlib.pyplot as plt



def plot_predictions(y_true, y_pred):
    plt.figure(figsize=(14,6))

    plt.plot(y_true, label='Actual')
    plt.plot(y_pred, label='Predicted')

    plt.legend()
    plt.title('Stock Price Prediction')

    plt.show()