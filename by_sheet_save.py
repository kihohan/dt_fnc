def save_sheet_excel(df, excel_name, sheet_column):
    xlxs_dir = excel_name + ".xlsx"
    with pd.ExcelWriter(xlxs_dir) as writer:
        for unique in sorted(df[sheet_column].unique())
            df[df[sheet_column] == unique].drop(sheet_column,1).to_excel(writer, sheet_name = unique, index = False)
