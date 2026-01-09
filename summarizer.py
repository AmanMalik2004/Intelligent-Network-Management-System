import pandas as pd

def summarize_logs(df):
    summary = {}

    summary['levels'] = df['level'].value_counts().to_dict()
    summary['messages'] = df['message'].value_counts().head(5).to_dict()
    summary['latest_critical_messages'] = df[df['message'].str.contains("down|loss|failure", case=False)].tail(3).to_dict('records') #case is just to ignore upper or lower case and tail 3 to select the bottom 3 recent one and record to make a dictionary for each row in dataframe(df)

    return summary