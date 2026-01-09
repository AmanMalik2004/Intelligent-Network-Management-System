from alert_classifier import classify_alert
from summarizer import summarize_logs

def chat(df, query):
    query = query.lower()

    if "summary" in query:
        return summarize_logs(df)
    elif "recent alert" in query or "critical" in query:
        criticals = df[df['level'] == 'ERROR'].tail(5).to_dict('records')
        return criticals
    elif "classify" in query:
        sample = df['message'].iloc[-1] #iloc is an integer-based index locator in pandas, -1 selects the last row from the message colum, -1 means last row
        return f"Latest message: '{sample}' is classified as {classify_alert(sample)}"
    else:
        return "Available commands:\n - 'summary'\n - 'recent alerts'\n - 'classify latest'\n"