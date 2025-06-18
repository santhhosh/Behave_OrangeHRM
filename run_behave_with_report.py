import os
import webbrowser
from behave.__main__ import main as behave_main

# Run Behave using behave.ini config
behave_main()

# Construct report path
report_path = os.path.abspath("reports/report.html")
report_url = f"file://{report_path}"

# Print HTML report link in terminal
print(f"\n✅ HTML Report generated at:\n{report_url}")

# Optionally, open it automatically in browser
webbrowser.open(report_url)