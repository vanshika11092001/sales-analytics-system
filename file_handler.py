def read_sales_file(file_path):
    records = []
    with open(file_path, 'r', encoding='latin-1') as file:
        lines = file.readlines()

    header = lines[0].strip().split("|")

    for line in lines[1:]:
        if not line.strip():
            continue
        records.append(line.strip())

    return header, records
