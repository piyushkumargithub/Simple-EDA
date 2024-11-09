from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

import matplotlib.pyplot as plt


def linearRegression(X,Y,Xdata, Ydata, test_size):
            X_train, X_test, y_train, y_test = train_test_split(
                Xdata, Ydata, test_size=test_size, random_state=0)
            regressor = LinearRegression()
            regressor.fit(X_train, y_train)
            y_pred = regressor.predict(X_test)

            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
            fig.tight_layout(pad=5)
            ax1.scatter(X_train, y_train)
            ax1.plot(X_train, regressor.predict(X_train))
            ax1.set_title((X+" vs " + Y))
            ax1.set_xlabel(X)
            ax1.set_ylabel(Y)
            ax2.scatter(X_test, y_test)
            ax2.plot(X_test, y_pred)
            ax2.set_title((X + " vs " + Y))
            ax2.set_xlabel(X)
            ax2.set_ylabel(Y)
            # st.pyplot(fig)
            return fig
            # plt.show(ax1)
            # part still to implement