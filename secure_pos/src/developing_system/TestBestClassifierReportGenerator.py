import json
import jsons
import os
import utility

REPORT_BEST_CLASSIFIER_PATH = 'development_system/reports/best_classifier/report_best_classifier.json'

class TestBestCLassifierReportGenerator:

    def generate_report(self, test_best_classifier, training_error_best_classifier):

        report = {
            'report_title:': 'Report of the Test of the best classifier',
            'id_best_classifier' : test_best_classifier.id_best_classifier,
            'test_tolerance': test_best_classifier.test_tolerance,
            'test_error': test_best_classifier.test_error,
            'training_error': training_error_best_classifier
        }

        with open(os.path.join(utility.data_folder, REPORT_BEST_CLASSIFIER_PATH), 'w') as report_file:
            report_file.write(json.dumps(report, indent=2))