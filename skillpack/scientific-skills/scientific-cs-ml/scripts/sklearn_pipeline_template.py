from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


@dataclass(frozen=True)
class TrainConfig:
    test_size: float = 0.2
    random_state: int = 42


def build_pipeline(numeric_features: list[str], categorical_features: list[str]):
    numeric = Pipeline(
        steps=[
            ("impute", SimpleImputer(strategy="median")),
            ("scale", StandardScaler()),
        ]
    )
    categorical = Pipeline(
        steps=[
            ("impute", SimpleImputer(strategy="most_frequent")),
            ("onehot", OneHotEncoder(handle_unknown="ignore")),
        ]
    )
    pre = ColumnTransformer(
        transformers=[
            ("num", numeric, numeric_features),
            ("cat", categorical, categorical_features),
        ]
    )

    # TODO: plug in model (e.g., LogisticRegression, RandomForestClassifier)
    return Pipeline(steps=[("preprocess", pre)])


def main():
    # TODO: load your dataframe and set X/y
    X = None
    y = None

    cfg = TrainConfig()
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=cfg.test_size, random_state=cfg.random_state, stratify=y
    )

    pipe = build_pipeline(numeric_features=[], categorical_features=[])
    pipe.fit(X_train, y_train)
    y_pred = pipe.predict(X_test)
    print(classification_report(y_test, y_pred))


if __name__ == "__main__":
    main()

