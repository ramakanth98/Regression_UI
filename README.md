UI-Based Time Series Analysis and Prediction
I have built a model for data preprocessing, time series analysis, correlation plot, regression model on some data from the web.
Technologies used: 


1. Firstly, for the UI – I used tkinter to build a UI to upload the data.xlsx file.

2. I used tk.button to create a button and used filedialog (a modle under the tkinter package) to open the file.

<img src="https://user-images.githubusercontent.com/51488881/216469234-544a1e4f-afec-48c9-aad7-4ec487483d74.png" width="200" height="200" />

3. Next, I used pandas to read the excel file and I wrote a function open_file to read the excel file and return the data in the form of a dataframe.

4. For the time series and correlation plots, I needed to preprocess the time series data.

5. For this, I wrote a function where I used the pandas.to_datetime() function to format the Year, Month, Day, Hour and Minute attributes into a single feature – ‘date_time’.

6. For the Time Series Plot, I used matplotlib to plot the data with date_time (which we obtained above) and the ‘Output’ attributes.

<img src="https://user-images.githubusercontent.com/51488881/216469478-2e3a0e0c-8b0c-4e72-a122-96a3688398f8.png" width="300" height="300" />

7. For the Correlation plot, I made use of the seaborn package and used scatterplot to plot the data.

<img src="https://user-images.githubusercontent.com/51488881/216469549-550ce719-6b69-4d9f-a573-7ab0ea474974.png" width="350" height="350" />

<img src="https://user-images.githubusercontent.com/51488881/216471325-2d1f9e9d-a5ad-4d87-a66d-4aca9d958dc2.png" width="350" height="350" />


8. As for the simple regression model (time series plot) : I used a simple Linear Regression model (Other models like RandomForestRegressor or GradientBoostingRegressor can be used).

<img src="https://user-images.githubusercontent.com/51488881/216470839-e49a4015-e16a-462d-8965-3f286364c9ae.png" width="400" height="400" />

9. I used sklearn.metrics to import r2_score and mean_squared_error.

10. I obtained an accuracy of 89% and 65% for the r2_score of train set and test set respectively.

