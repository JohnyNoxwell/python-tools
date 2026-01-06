import csv 


def load_sales(path):
    rows = []
    with open(path,  newline="") as f:
        reader = csv.DictReader(f)
        for row  in reader:
            rows.append({
                "product": row["product"],
                "price": int(row["price"]),
                "quantity": int(row["quantity"])
            })
    return rows


def compute_revenue(rows):
    revenue = {}
    for row in rows:
        product = row ["product"]
        total = row["price"] * row["quantity"]
        revenue[product] = revenue.get(product, 0) + total
    return revenue


def filter_revenue(revenue, product=None, min_revenue=None, contains=None):
    resuslt = dict(revenue)

    if product is not None:
        resuslt = {k: v for k, v in resuslt.items() if k.lower() == product.lower()}

    if min_revenue is not None:
        resuslt = {k: v for k, v in resuslt.items() if v >= min_revenue}

    if contains is not None:
        resuslt = {k: v for k, v in resuslt.items() if contains.lower() in k.lower()}
    
    return resuslt


def top_n(revenue, n):
    return sorted(revenue.items(), key=lambda x: x[1], reverse=True)[:n]