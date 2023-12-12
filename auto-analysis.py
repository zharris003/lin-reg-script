import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def main():
    """This function runs the program by getting the data from the data url, makes predictions and gives a report"""
    df = pd.read_csv('auto-mpg.csv')

    # pre-processing data
    df.dropna(axis=0)

    y = df['displacement'].values
    X = df['acceleration'].values

    y=y.reshape(-1,1)
    X = X.reshape(-1,1)

    # train test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # plot training data
    fig, ax = plt.subplots(1,1)
    ax.scatter(X_train,y_train)
    plt.xlabel('displacement')
    plt.ylabel('acceleration')

    # Save the plot to a file
    fig.savefig("xtrain_accel_vs_ytrain_disp.png")

    # create and fit a lin reg model to the training data
    lr = LinearRegression()
    lr.fit(X_train,y_train)

    # Find the min and max of the test data 
    minX = X_test.min()
    maxX = X_test.max()

    miny = y_test.min()
    maxy = y_test.max()

    # predict minX & maxX using your linear model 
    [miny, maxy] = lr.predict(np.array([minX,maxX]).reshape(-1,1))

    # plot the testing data predictions
    fig, ax = plt.subplots(1,1)
    ax.plot([minX,maxX],[miny,maxy])
    plt.xlabel('displacement')
    plt.ylabel('acceleration')

    # Save the plot to a file
    fig.savefig("linear_regression.png")

    # Make a report and save to a file    
    with open("report.txt", "w") as f:
        f.write("# Data Summary\n\n")
        f.write("## df.info()\n\n")
        df.info(buf=f)
        f.write("\n\n## df.describe()\n\n")
        f.write(str(df.describe()))
        f.write("\n\n## r-squared\n\n")
        f.write(str(lr.score(X_test, y_test)))


if __name__ == "__main__":
    main()