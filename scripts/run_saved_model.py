from __future__ import annotations

import argparse
import json
from pathlib import Path

import joblib
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
MODEL_PATH = ROOT / "models" / "best_price_model.joblib"
METRICS_PATH = ROOT / "reports" / "model_training_metrics.json"
DATA_PATH = ROOT / "dataset" / "feature_engineered_dataset.csv"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Load the saved Retail Price Optimizer model and predict sample prices."
    )
    parser.add_argument(
        "--rows",
        type=int,
        default=5,
        help="Number of dataset rows to predict. Default: 5.",
    )
    parser.add_argument(
        "--start",
        type=int,
        default=0,
        help="Starting row index from the feature-engineered dataset. Default: 0.",
    )
    parser.add_argument(
        "--input-file",
        type=Path,
        default=None,
        help=(
            "Optional CSV file containing your own rows to predict. "
            "If omitted, rows are sampled from feature_engineered_dataset.csv."
        ),
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    metrics = json.loads(METRICS_PATH.read_text(encoding="utf-8"))
    feature_columns = metrics["numeric_features"] + metrics["categorical_features"]

    model = joblib.load(MODEL_PATH)
    input_path = args.input_file

    if input_path is None:
        data = pd.read_csv(DATA_PATH)
        sample = data.iloc[args.start : args.start + args.rows].copy()
        source_label = DATA_PATH
    else:
        if not input_path.is_absolute():
            input_path = ROOT / input_path
        sample = pd.read_csv(input_path).head(args.rows).copy()
        source_label = input_path

    missing_columns = [col for col in feature_columns if col not in sample.columns]
    if missing_columns:
        raise ValueError(
            "The input file is missing required model columns: "
            + ", ".join(missing_columns)
        )

    predictions = model.predict(sample[feature_columns])

    output = pd.DataFrame({"row_index": sample.index})
    if "price" in sample.columns:
        output["actual_price"] = sample["price"].round(2)
    output["predicted_price"] = [round(float(value), 2) for value in predictions]

    print(f"Loaded model: {MODEL_PATH}")
    print(f"Input data: {source_label}")
    print(f"Model type: {type(model).__name__}")
    print(f"Feature columns used: {len(feature_columns)}")
    print()
    print(output.to_string(index=False))


if __name__ == "__main__":
    main()
