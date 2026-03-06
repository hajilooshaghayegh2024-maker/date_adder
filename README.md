# Date Adder CLI

## Purpose
The **Date Adder** is a lightweight Python command-line utility designed to help users quickly calculate future or past dates. It simplifies date arithmetic by allowing you to add or subtract days, weeks, months, and years from any given date (defaulting to today) without needing to manually account for leap years or varying month lengths.

This tool is ideal for developers, project managers, or anyone needing to calculate deadlines, milestones, or recurring dates directly from the terminal.

## Key Features
- **Flexible Arithmetic**: Add or subtract days, weeks, months, and years.
- **Smart Calculations**: Automatically handles leap years and different month durations using `python-dateutil`.
- **ISO Standard**: Uses the universal `YYYY-MM-DD` date format.
- **Dynamic Defaults**: If no date is provided, it defaults to the current system date.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/hajilooshaghayegh2024-maker/date_adder.git
   cd date_adder
   ```

2. **Install dependencies**:
   This tool requires the `python-dateutil` library.
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script from your terminal using the following arguments:

| Argument | Description | Default |
| :--- | :--- | :--- |
| `--date` | The start date in `YYYY-MM-DD` format | Today |
| `--days` | Number of days to add (use negative for subtraction) | 0 |
| `--weeks` | Number of weeks to add | 0 |
| `--months`| Number of months to add | 0 |
| `--years` | Number of years to add | 0 |

### Examples

**1. Add 30 days to today:**
```bash
python date_adder.py --days 30
```

**2. Add 2 months and 1 week to a specific date:**
```bash
python date_adder.py --date 2024-01-01 --months 2 --weeks 1
```

**3. Subtract 1 year from a date:**
```bash
python date_adder.py --date 2025-12-25 --years -1
```

## License
MIT License
