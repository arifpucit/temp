import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def make_dataset(days=120, seed=42):
    """Build a synthetic time series of daily temperature and humidity."""
    rng = np.random.default_rng(seed)
    dates = pd.date_range("2026-01-01", periods=days, freq="D")

    t = np.arange(days)
    temperature = 15 + 10 * np.sin(2 * np.pi * t / 365) + rng.normal(0, 1.5, days)
    humidity = 60 - 0.8 * (temperature - 15) + rng.normal(0, 4, days)

    return pd.DataFrame(
        {"temperature_c": temperature, "humidity_pct": humidity}, index=dates
    )


def main():
    print("Hello from temp!")

    df = make_dataset()
    print(df.head())
    print(df.describe())

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df.index, df["temperature_c"], label="Temperature (°C)")
    ax.plot(df.index, df["humidity_pct"], label="Humidity (%)")
    ax.set_title("Hello Pull Request")
    ax.set_xlabel("Date")
    ax.set_ylabel("Value")
    ax.legend()
    ax.grid(alpha=0.3)
    fig.autofmt_xdate()
    fig.tight_layout()

    fig.savefig("synthetic_data.png", dpi=150)
    print("Saved plot to synthetic_data.png")
    plt.show()


if __name__ == "__main__":
    main()
