# Car-Recommend-System

A content-based car recommendation system that suggests similar cars based on their specifications — brand, fuel type, body type, transmission, seating capacity, price, and mileage/range.

## How It Works

The system uses **content-based filtering**:

1. Car specs are preprocessed using a `ColumnTransformer` pipeline:
   - Categorical features (brand, fuel type, body type, transmission, etc.) → `OneHotEncoder`
   - Numerical features (price, seating capacity, mileage, etc.) → `StandardScaler`
2. The transformed feature vectors are compared using **cosine similarity**.
3. Given a car name, the model returns the top-N most similar cars from the dataset.

## Data Preparation

Exploratory analysis and cleanup performed on `car_dataset.csv` include:

- Checking for nulls and inspecting distributions (brand, fuel type, body type, transmission, seating capacity)
- Dropping less relevant columns (`rto_tax_rs`, `insurance_rs`, `other_charges_rs`, `segment`)
- Bucketing `mileage_or_range` into readable ranges, with separate bins for electric vehicles (range in km) vs. fuel vehicles (mileage in km/l)

## Tech Stack

- Python
- pandas, NumPy
- scikit-learn (`OneHotEncoder`, `StandardScaler`, `ColumnTransformer`, `cosine_similarity`)
- seaborn, matplotlib (EDA/visualization)

## Project Structure

```
Car-Recommend-System/
├── model_training.ipynb   # Data exploration, preprocessing, and model logic
├── car_dataset.csv        # Car specifications dataset (not included in repo)
├── LICENSE
└── README.md
```

## Status

This project is a work in progress. The notebook currently covers data exploration, preprocessing, and the recommendation logic; a saved model artifact (`car_recommend_model.pkl`) and a standalone app for querying recommendations are planned next.

## Getting Started

1. Clone the repo:
   ```bash
   git clone https://github.com/vikaskatariya30/Car-Recommend-System.git
   cd Car-Recommend-System
   ```
2. Install dependencies:
   ```bash
   pip install pandas numpy scikit-learn seaborn matplotlib
   ```
3. Add `car_dataset.csv` to the project root and run `model_training.ipynb`.

## License

This project is licensed under the Apache License 2.0 — see the [LICENSE](LICENSE) file for details.

## Author

**Vikas Katariya**
GitHub: [@vikaskatariya30](https://github.com/vikaskatariya30)