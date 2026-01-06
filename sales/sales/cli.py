import argparse
from sales.core import load_sales, compute_revenue, filter_revenue, top_n


def main():
    parser = argparse.ArgumentParser(description="Sales analytics")
    parser.add_argument("file", help="CSV file with sales data")
    parser.add_argument("--top", type=int, default=5, help="Number of top products")
    parser.add_argument("--product", help="Filter by exact product name")
    parser.add_argument("--min-revenue", type=float, help="Filter by minimum revenue")
    parser.add_argument("--contains", help="Filter by substring in product name")

    args = parser.parse_args()

    rows = load_sales(args.file)
    revenue = compute_revenue(rows)
    revenue = filter_revenue(
        revenue,
        product=args.product,
        min_revenue=args.min_revenue,
        contains=args.contains,
    )

    if not revenue:
        print("No items to display")
        return

    for product, total in top_n(revenue, args.top):
        print(f"{product}: {total}")


if __name__ == "__main__":
    main()
