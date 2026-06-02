
# Retail Price Optimizer ML

This repository version is for the final model-training work for the ARTI 308 Retail Price
Optimizer project. It uses the feature-engineered dataset prepared in the
data-prep work, trains regression models, saves the best model, and exports the
results for the final report and presentation.

## Branch Purpose

- Branch: `main` final version
- Dataset source of truth: `dataset/feature_engineered_dataset.csv`
- Best trained model: Random Forest Regressor
- Target column: `price`
- Best holdout result: MAE `22.54 BRL`, RMSE `53.09 BRL`, R2 `0.775`

## Main Files To Open

| Path | Purpose |
| --- | --- |
| `notebooks/03_model_training_results.ipynb` | Main executed notebook for model training, evaluation, comments, plots, and exported results. |
| `notebooks/04_test_saved_model.ipynb` | Notebook for loading the saved `.joblib` model and testing your own values. |
| `reports/model_training_results.html` | Browser-friendly HTML version of the notebook results. |
| `models/best_price_model.joblib` | Saved trained sklearn pipeline. Use this file to test predictions. |
| `reports/model_training_metrics.json` | Full metrics summary used by the report and presentation. |
| `reports/model_performance.csv` | Holdout MAE, RMSE, and R2 for each tested model. |
| `reports/cross_validation_results.csv` | Cross-validation results for the ensemble models. |
| `reports/feature_subset_results.csv` | Feature-subset comparison results. |
| `reports/feature_importance.csv` | Random Forest feature importance values. |
| `reports/figures/` | Exported plots used in the report and HTML file. |
| `TEAM_PRESENTATION_QA.md` | Bilingual English/Arabic preparation questions and answers for the final presentation. |
| `scripts/create_training_notebook.py` | Script that creates/updates the model-training notebook. |
| `scripts/update_final_report_results.py` | Script that updates the final Word report using the latest metrics. |

## Dataset Files

| Path | Purpose |
| --- | --- |
| `dataset/cleaned_base_dataset.csv` | Cleaned base dataset from the data-preparation stage. |
| `dataset/price_outliers_removed_dataset.csv` | Dataset after removing price outliers. |
| `dataset/feature_engineered_dataset.csv` | Final prepared dataset used for model training. |
| `dataset/manual_test_input.csv` | Small template CSV where you can type your own values and predict prices. |
| `dataset/olist_customers_dataset.csv` | Original customer dataset kept for reference, not used in the corrected training features. |

## Features Used For Training

The corrected training notebook uses only the prepared feature-engineered data
and does not add extra customer, date, or logistics features during training.

Numeric features:

- `order_item_id`
- `freight_value`
- `product_name_lenght`
- `product_description_lenght`
- `product_photos_qty`
- `product_weight_g`
- `product_length_cm`
- `product_height_cm`
- `product_width_cm`
- `product_volume_cm3`
- `product_demand_count`
- `category_demand_count`

Categorical features:

- `product_category_name_english`
- `freight_level`
- `product_size_level`

Target-leakage columns excluded from training:

- `total_order_item_value`
- `freight_ratio`
- `freight_ratio_percent`
- `price_range`
- `category_avg_price`
- `category_median_price`
- `price_vs_category_median`

## Models Tested

| Model | Role | Values Tested | Final Setting |
| --- | --- | --- | --- |
| Linear Regression | Baseline | No grid search | Baseline only |
| Random Forest Regressor | Best model | `n_estimators`: 80, 140; `max_depth`: 14, None; `min_samples_leaf`: 1 | `n_estimators=140`, `max_depth=None`, `min_samples_leaf=1` |
| Gradient Boosting Regressor | Comparison ensemble | `n_estimators`: 80, 140; `learning_rate`: 0.05, 0.10; `max_depth`: 2 | `n_estimators=140`, `learning_rate=0.10`, `max_depth=2` |

## Final Results

| Model | MAE (BRL) | RMSE (BRL) | R2 |
| --- | ---: | ---: | ---: |
| Random Forest Regressor | 22.54 | 53.09 | 0.775 |
| Gradient Boosting Regressor | 52.89 | 87.29 | 0.393 |
| Linear Regression Baseline | 57.86 | 92.85 | 0.313 |

## How To Test The Saved Model

Run this from the repo root:

```powershell
.\venv\Scripts\python.exe scripts\run_saved_model.py --rows 3
```

To test your own values, edit `dataset/manual_test_input.csv`, then run:

```powershell
.\venv\Scripts\python.exe scripts\run_saved_model.py --input-file dataset\manual_test_input.csv
```

Or use this inline Python version:

```powershell
@'
from pathlib import Path
import json
import joblib
import pandas as pd

root = Path.cwd()
model = joblib.load(root / "models" / "best_price_model.joblib")
metrics = json.loads((root / "reports" / "model_training_metrics.json").read_text())
features = metrics["numeric_features"] + metrics["categorical_features"]

df = pd.read_csv(root / "dataset" / "feature_engineered_dataset.csv")
sample = df[features].head(3)
predictions = model.predict(sample)

print("Actual prices:", df["price"].head(3).round(2).tolist())
print("Predictions:", [round(float(x), 2) for x in predictions])
'@ | .\venv\Scripts\python.exe -
```

Expected behavior: the model loads successfully and returns price predictions.

## How To Recreate The Notebook Outputs

Use the training notebook directly:

```powershell
.\venv\Scripts\jupyter.exe notebook notebooks\03_model_training_results.ipynb
```

To test your own values in a notebook, open:

```powershell
.\venv\Scripts\jupyter.exe notebook notebooks\04_test_saved_model.ipynb
```

Or run the notebook in Jupyter and export the HTML again if needed.

## Final Report And Presentation

The final course files are saved outside the repo folder:

- `C:\Users\gosfe\OneDrive\University\Third year\Second Semester\Machine Learning\Project Documnts\ARTI 308 Final Project Report - Retail Price Optimizer.docx`
- `C:\Users\gosfe\OneDrive\University\Third year\Second Semester\Machine Learning\Project Documnts\Retail Price Optimizer Reveal Style Defense.pptx`
- `C:\Users\gosfe\OneDrive\University\Third year\Second Semester\Machine Learning\Project Documnts\Retail Price Optimizer - Professor Questions Guide.pdf`

## Team Notes

- Team leader: Abdulaziz Saud Aldossary
- Ahmed Alzayer is excluded from the final team list.
- Keep data-prep work as the dataset source of truth.
- Keep model artifacts and training outputs in this final `main` branch.
- Do not train using target-derived leakage features.
