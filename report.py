import datetime
from jinja2 import Template

server_info = {
    "server_name": "Web server",
    "ip_address": "192.168.1.100",
    "os": "Ubuntu",
    "status": "Active"
}

timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
template_text = """
# Server Report

Timestamp: {{ timestamp }}
Server Name: {{ server_info.server_name }}
IP Address: {{ server_info.ip_address }}
Operating system: {{ server_info.os }}
Status: {{ server_info.status }}
"""

template = Template(template_text)
report = template.render(timestamp=timestamp, server_info=server_info)
report_file_path = "server_report.md"
with open(report_file_path, "w") as report_file:
    report_file.write(report)

print("Report created: ", report_file_path)