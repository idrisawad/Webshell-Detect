# Webshell-Detect

This script will search for files with certain extensions and keywords that are commonly found in webshells. This script will only detect webshells that are written in a certain way and may not detect all webshells and export them in a CSV file.

The script uses the `csv` module to write the results to a file called "webshell_detection_results.csv". It writes the "File Path" and "Keywords Found" in the csv file. The `DictWriter` class is used to write the results as a dictionary, with the keys of the dictionary matching the fieldnames defined at the beginning of the script.

It's important to note that this script is for demonstration purposes only and the results should be carefully checked and validated before taking any action. Additionally, it's important to understand that using this script without permission on a web server you don't own could be considered illegal and/or unethical.

It's important to also note that, in order to use this script in a real scenario, you'll need to run this script with appropriate permissions (i.e. a user that has access to the files on the web server) and it's recommended to use this script alongside other security measures like a web application firewall and intrusion detection/prevention system.

Again, please be aware that using this script without permission on a web server you don't own could be considered illegal and/or unethical.

Legal Disclaimer:
This script is intended for authorized use only. By using this script, you agree to use it in compliance with all applicable laws and regulations. The author of this script is not responsible for any actions taken or damages caused by the use of this script.

The user of this script is solely responsible for obtaining any necessary permissions or licenses required for its use. The author of this script makes no representations or warranties of any kind, express or implied, about the completeness, accuracy, reliability, suitability or availability with respect to the script or the information, products, services, or related graphics contained in the script for any purpose. Any reliance you place on such information is therefore strictly at your own risk.

In no event will the author of this script be liable for any loss or damage including without limitation, indirect or consequential loss or damage, or any loss or damage whatsoever arising from loss of data or profits arising out of, or in connection with, the use of this script.

By using this script, you understand and agree that the author of this script shall have no liability for any damages whatsoever, including but not limited to any direct, indirect, special, incidental, or consequential damages, and including, without limitation, lost revenues, lost profits, or loss of prospective economic advantage, resulting from the use or misuse of the information contained in this script.

The user of this script must not use this script for any illegal or unauthorized purpose. The user is solely responsible for any actions taken through the use of this script, and the author of this script will not be held liable for any damages or losses resulting from such actions.

By using this script, you confirm that you have read and understood this disclaimer and agree to be bound by its terms. If you do not agree with the terms of this disclaimer, you must not use this script.
