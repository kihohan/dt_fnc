xlxs_dir = "fil_name.xlsx"
with pd.ExcelWriter(xlxs_dir) as writer:
    for brand in result['BRAND'].unique():
        result[result['BRAND'] == brand].to_excel(writer, sheet_name = brand, index = False)
