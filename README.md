# temp

A minimal "hello world" project demonstrating the core Python data stack: **numpy** for
number generation, **pandas** for structuring, and **matplotlib** for plotting.

The script synthesizes 120 days of daily weather data (temperature and humidity),
prints summary statistics, and renders both series as a line graph.

## Requirements

- Python >= 3.12 (pinned to 3.12 via `.python-version`)
- [uv](https://docs.astral.sh/uv/) for dependency management

## Setup and running

`uv` reads `pyproject.toml` and `uv.lock`, creating the virtual environment and
installing dependencies automatically on first run:

```bash
uv run main.py
```

This prints the dataset summary, saves the chart to `synthetic_data.png`, and opens
an interactive plot window.

To run without opening a window (e.g. on a headless machine or in CI), force the
non-interactive Agg backend:

```bash
MPLBACKEND=Agg uv run main.py
```

## How it works

`main.py` contains two functions:

### `make_dataset(days=120, seed=42)`

Returns a `pandas.DataFrame` indexed by a `DatetimeIndex` starting at `2026-01-01`,
with two columns:

| Column | Description |
| --- | --- |
| `temperature_c` | Seasonal sine wave over the day-of-year, centered at 15 °C with a 10 °C amplitude, plus Gaussian noise (σ = 1.5) |
| `humidity_pct` | Derived from temperature with a negative coefficient (−0.8), plus Gaussian noise (σ = 4) |

Humidity is deliberately *derived* from temperature rather than drawn independently,
so the two series are negatively correlated — the plot shows a real relationship
instead of two unrelated noise traces.

Randomness comes from `numpy.random.default_rng(seed)`, so output is reproducible:
repeated runs produce identical numbers and an identical chart.

### `main()`

Builds the dataset, prints `.head()` and `.describe()`, then plots both series on
shared axes with a legend and grid, saves the figure at 150 dpi, and calls
`plt.show()`.

## Customizing

Adjust the call in `main()` to change the output:

- `make_dataset(days=365)` — a full year, which shows the complete seasonal cycle
  (the default 120 days only covers the rising portion of the sine wave)
- `make_dataset(seed=7)` — a different random draw with the same underlying shape

## Project layout

```
.
├── main.py             # Dataset generation and plotting
├── pyproject.toml      # Project metadata and dependencies
├── uv.lock             # Pinned dependency versions
├── .python-version     # Python version pin (3.12)
└── synthetic_data.png  # Generated chart (rewritten on each run)
```

## Dependencies

Locked versions in `uv.lock`:

| Package | Version |
| --- | --- |
| numpy | 2.5.2 |
| pandas | 3.0.5 |
| matplotlib | 3.11.1 |
