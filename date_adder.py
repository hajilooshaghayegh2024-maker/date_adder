import argparse
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

def add_to_date(start_date, days=0, weeks=0, months=0, years=0):
    date_obj = datetime.strptime(start_date, "%Y-%m-%d")
    result = date_obj + relativedelta(days=days, weeks=weeks, months=months, years=years)
    return result.strftime("%Y-%m-%d")

def main():
    parser = argparse.ArgumentParser(description="Add time to a date.")
    parser.add_argument("--date", type=str, help="Start date in YYYY-MM-DD format (default: today)", default=datetime.now().strftime("%Y-%m-%d"))
    parser.add_argument("--days", type=int, default=0, help="Number of days to add")
    parser.add_argument("--weeks", type=int, default=0, help="Number of weeks to add")
    parser.add_argument("--months", type=int, default=0, help="Number of months to add")
    parser.add_argument("--years", type=int, default=0, help="Number of years to add")

    args = parser.parse_args()

    try:
        new_date = add_to_date(args.date, args.days, args.weeks, args.months, args.years)
        print(f"Resulting date: {new_date}")
    except ValueError as e:
        print(f"Error: {e}. Please use YYYY-MM-DD format.")

if __name__ == "__main__":
    main()
