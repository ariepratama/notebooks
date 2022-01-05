import pandas as pd


def load_as_dataframe(data_loc: str, category_sheet: str = "KODE POLA") -> pd.DataFrame:
    category_data = pd.read_excel(data_loc, sheet_name=category_sheet, header=1)
    itoc = {str(row[category_sheet.lower()]): row[2] for _, row in category_data.iterrows()}

    data_sheets = [
        "{}-{}".format(start, start + 499)
        for start in range(1, 10001, 500)
    ]

    data: List[pd.DataFrame] = [
        pd.read_excel(data_loc, sheet_name=data_sheet)
        for data_sheet in data_sheets
    ]

    all_data = pd.concat(data)

    columns = all_data.columns
    all_data = all_data.rename(columns={
        col: itoc[str(col)]
        for col in columns
        if str(col) in itoc
    })
    return all_data
