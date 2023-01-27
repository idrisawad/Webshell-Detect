import os
import csv

webshell_extensions = ['.php', '.asp', '.jsp'] # add any other extensions commonly used for webshells
webshell_keywords = ['system', 'shell_exec', 'eval'] # add any other keywords commonly used in webshells

def detect_webshell(root_dir):
    with open('webshell_detection_results.csv', mode='w') as csv_file:
        fieldnames = ['File Path', 'Keywords Found']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for root, dirs, files in os.walk(root_dir):
            for file in files:
                file_path = os.path.join(root, file)
                file_extension = os.path.splitext(file_path)[1]
                if file_extension in webshell_extensions:
                    with open(file_path, 'r') as f:
                        file_contents = f.read()
                        keywords_found = []
                        for keyword in webshell_keywords:
                            if keyword in file_contents:
                                keywords_found.append(keyword)
                        if keywords_found:
                            writer.writerow({'File Path': file_path, 'Keywords Found': keywords_found})

detect_webshell('/var/www/html') # specify the root directory of the web server
