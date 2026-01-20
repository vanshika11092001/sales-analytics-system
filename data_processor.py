def clean_and_validate_records(records):
    valid = []
    invalid_count = 0

    for line in records:
        parts = line.split("|")

        if len(parts) != 8:
            invalid_count += 1
            continue

        txn_id, date, pid, pname, qty, price, cid, region = parts

        # TransactionID rule
        if not txn_id.startswith("T"):
            invalid_count += 1
            continue

        # Missing CustomerID or Region
        if cid.strip() == "" or region.strip() == "":
            invalid_count += 1
            continue

        # Quantity
        try:
            qty = int(qty)
            if qty <= 0:
                invalid_count += 1
                continue
        except:
            invalid_count += 1
            continue

        # Unit Price (remove commas)
        try:
            price = float(price.replace(",", ""))
            if price <= 0:
                invalid_count += 1
                continue
        except:
            invalid_count += 1
            continue

        # Product Name – remove commas
        pname = pname.replace(",", " ")

        valid.append({
            "TransactionID": txn_id,
            "Date": date,
            "ProductID": pid,
            "ProductName": pname,
            "Quantity": qty,
            "UnitPrice": price,
            "CustomerID": cid,
            "Region": region
        })

    print(f"Total records parsed: {len(records)}")
    print(f"Invalid records removed: {invalid_count}")
    print(f"Valid records after cleaning: {len(valid)}")

    return valid
