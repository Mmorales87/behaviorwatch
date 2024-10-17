import json
import os
from interfaces.ireport_generator import IReportGenerator

class ReportGenerator(IReportGenerator):
    def __init__(self, config_file):
        self.config_file = config_file
        self.reports_dir = "reports"
        os.makedirs(self.reports_dir, exist_ok=True)

    def generate_report(self, insult, user, media_file):
        report_data = {
            "insult": insult,
            "user": user,
            "media_file": media_file
        }
        report_filename = os.path.join(self.reports_dir, f"report_{user}.json")
        
        with open(report_filename, 'w') as report_file:
            json.dump(report_data, report_file, indent=4)
        
        print(f"Reporte generado: {report_filename}")

