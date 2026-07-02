from support_item.others_items import name_for_comparison_df, name_for_lead_days_summary

def comparison_to_csv(df):
    if df.empty:
        print('DataFrame is empty,')

    if 'mean_abs_error' in df.columns:
        print('Table: Lead days summary.')
        filename = name_for_lead_days_summary(df)
    else:
        print('Table : Comparison data frame.')
        filename = name_for_comparison_df(df)

    filename.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(filename, index=False, encoding='utf-8')
