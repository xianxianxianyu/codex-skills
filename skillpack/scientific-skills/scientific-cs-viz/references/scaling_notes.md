# Scaling Notes (Polars/Dask)

## When to reach for Polars
- You need faster groupby/join on large CSV/Parquet.
- You want lazy execution and query optimization.

## When to reach for Dask
- Data doesn’t fit in memory, or you need parallel compute.
- You can tolerate a slightly more complex execution model.

## Artifact rule
Regardless of backend, always export:
- `tables/summary.csv` (or `.parquet`) for downstream use
- A concise `reports/eda.md` with command lines and file paths

