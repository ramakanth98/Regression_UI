import tkinter as tk
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection  import train_test_split
import seaborn as sns
import numpy as np
from sklearn.metrics import r2_score, mean_squared_error


def open_file():
    filepath = filedialog.askopenfilename()
    data = pd.read_excel(filepath)
    #print(data)
    return data

def data_preprocessing(data):
    data["YY"] = data["YY"].astype(str)
    data["MM"] = data["MM"].astype(str)
    data["DD"] = data["DD"].astype(str)
    data["HH"] = data["HH"].astype(str)
    data["mm"] = data["mm"].astype(str)

    data["date_time"] = data['YY'] + "-" + data['MM'] + "-" + data['DD'] + ":" + data['HH'] + ":" + data['mm']
    data["date_time"] = pd.to_datetime(data["date_time"], format='%Y-%m-%d:%H:%M')
    #data.head()
    return data

def time_series_plot(data):
    plt.plot(data['date_time'], data['Output'])
    plt.show()
    return data

def train_regression(data):
    x_train, x_test, y_train, y_test = train_test_split(data[['SW', 'WS', 'TP']], data["Output"], test_size=0.2,
                                                        shuffle=False)
    Linear_regressor = LinearRegression()
    Linear_regressor.fit(x_train, y_train)

    LR_train_pred = Linear_regressor.predict(x_train)
    LR_test_pred = Linear_regressor.predict(x_test)

    LR_r2_score_train = r2_score(y_train, LR_train_pred)
    #LR_mse_train = mean_squared_error(y_train, LR_train_pred)

    LR_r2_score_test = r2_score(y_test, LR_test_pred)
    #LR_mse_test = mean_squared_error(y_test, LR_test_pred)

    print("R2 Score for Train set: ", LR_r2_score_train)
    print("R2 Score for Test set: ", LR_r2_score_test)

    data_pred = data[(data.index > np.percentile(data.index, 80))]
    data_pred['predictions'] = LR_test_pred
    data_pred.plot(x="date_time", y=["Output", "predictions"], kind="line", figsize=(10, 10))
    plt.show()


def correlation_plot(data):
    sns.scatterplot(data=data, x='date_time', y='Output', hue='SW')
    plt.show()
    sns.scatterplot(data=data, x='date_time', y='Output', hue='WS')
    plt.show()
    sns.scatterplot(data=data, x='date_time', y='Output', hue='TP')
    plt.show()
    dataplot = sns.heatmap(data.corr(), cmap="YlGnBu", annot=True)
    plt.show()


root = tk.Tk()
root.title("File Upload")
upload_button = tk.Button(text="Upload File", command=open_file)
upload_button.pack()
df = open_file()
#print(df.corr())
data = data_preprocessing(df)

time_series_button = tk.Button(text="Time Series Plot", command=lambda: time_series_plot(data))
time_series_button.pack()

correlation_button = tk.Button(text="Correlation Plot", command=lambda: correlation_plot(data))
correlation_button.pack()

regression_button = tk.Button(text="Train Regression Model", command=lambda: train_regression(data))
regression_button.pack()

root.mainloop()
