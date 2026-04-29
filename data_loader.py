
import pandas as pd
import openml
from IPython.display import display
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder


def load_openml_df(dataset_id):
    dataset = openml.datasets.get_dataset(dataset_id)

    X, y, _, _ = dataset.get_data(
        target=dataset.default_target_attribute
    )

    df = X.copy()
    df[dataset.default_target_attribute] = y

    return df, dataset.default_target_attribute


class Dataset:

    def __init__(self, problem_type):

        if problem_type == "regression":
            self.df, target_col = load_openml_df(537)

            self.df[target_col] = self.df[target_col] / 100000

        elif problem_type == "binary classification":
            self.df, target_col = load_openml_df(15)

            self.df[target_col] = LabelEncoder().fit_transform(self.df[target_col])

        elif problem_type == "multiclass classification":
            self.df, target_col = load_openml_df(61)

            self.df[target_col] = LabelEncoder().fit_transform(self.df[target_col])

        else:
            raise ValueError(
                "Choose between regression, binary classification, or multiclass classification"
            )

        self.df.dropna(inplace=True)

        self.X = self.df.drop(columns=[target_col]).values
        self.y = self.df[target_col].values

    def display(self):

        pd.set_option("display.max_columns", 6)

        display(self.df)


    def load_split_data(self):

        X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, test_size=0.2, shuffle=True, random_state=1)

        return X_train, X_test, y_train, y_test


def standardize(X_train, X_test):

    scaler = StandardScaler()

    scaler.fit(X_train)

    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)

    return X_train, X_test
