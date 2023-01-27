# Webshell-Detect

This script will search for files with certain extensions and keywords that are commonly found in webshells. This script will only detect webshells that are written in a certain way and may not detect all webshells and export them in a CSV file.

The script uses the `csv` module to write the results to a file called "webshell_detection_results.csv". It writes the "File Path" and "Keywords Found" in the csv file. The `DictWriter` class is used to write the results as a dictionary, with the keys of the dictionary matching the fieldnames defined at the beginning of the script.

* It's important to note that this script is for demonstration purposes only and the results should be carefully checked and validated before taking any action. Additionally, it's important to understand that using this script without permission on a web server you don't own could be considered illegal and/or unethical. *

* It's important to also note that, in order to use this script in a real scenario, you'll need to run this script with appropriate permissions (i.e. a user that has access to the files on the web server) and it's recommended to use this script alongside other security measures like a web application firewall and intrusion detection/prevention system. *

#### Requirements #### 

 - Python 3.x
 - os module
 - csv module

#### Usage ####

 1. Clone or download the script from the repository.
 2. Open a terminal and navigate to the directory where the script is located.
 3. Run the script by typing `python webshell_detect.py` in the terminal and press enter.
 4. The script will start to scan the web server directory and write the results to a file called `webshell_detection_results.csv`.
 5. The script will create a CSV file in the same directory where the script is located.
 6. Open the csv file to see the results.

#### Configuration ####
The script can be configured by modifying the following variables:

 - `webshell_extensions`: A list of file extensions that the script will search for. By default, the script will search for PHP, ASP, and JSP files. Additional extensions can be added as needed.
 - `webshell_keywords`: A list of keywords that the script will search for. By default, the script will search for the keywords "system", "shell_exec", and "eval". Additional keywords can be added as needed.
 - `root_dir` : The script will scan the directory that is passed as the argument to the function `detect_webshell()` by default it is set to `/var/www/html`.

#### Limitations ####

 - This script is not a guaranteed method of detecting all webshells and may need to be adapted to the specific environment and use case.
 - The script is only able to detect the webshells that are written in a certain way and may not detect all webshells.
 - The script will only detect webshells that are located in the specified directory and its subdirectories.
 - It's important to run this script with appropriate permissions (i.e. a user that has access to the files on the web server)
 - It's recommended to use this script alongside other security measures like a web application firewall and intrusion detection/prevention system.
 - This script is for demonstration purposes only and the results should be carefully checked and validated before taking any action.

#### Legal and Ethical Use ####

It's important to understand that using this script without permission on a web server you don't own could be considered illegal and/or unethical. Always make sure you have the necessary permissions before running this script.

#### Conclusion ####
The webshell detection script can be a useful tool for detecting webshells on a web server. However, it's important to understand that it's not a guaranteed method of detection and that the script may need to be adapted to the specific environment and use case. Additionally, it's important to use this script legally and ethically and it's recommended to use this script alongside other security measures.


* Again, please be aware that using this script without permission on a web server you don't own could be considered illegal and/or unethical. *

#### Legal Disclaimer: ####

This script is intended for authorized use only. By using this script, you agree to use it in compliance with all applicable laws and regulations. The author of this script is not responsible for any actions taken or damages caused by the use of this script.

The user of this script is solely responsible for obtaining any necessary permissions or licenses required for its use. The author of this script makes no representations or warranties of any kind, express or implied, about the completeness, accuracy, reliability, suitability or availability with respect to the script or the information, products, services, or related graphics contained in the script for any purpose. Any reliance you place on such information is therefore strictly at your own risk.

In no event will the author of this script be liable for any loss or damage including without limitation, indirect or consequential loss or damage, or any loss or damage whatsoever arising from loss of data or profits arising out of, or in connection with, the use of this script.

By using this script, you understand and agree that the author of this script shall have no liability for any damages whatsoever, including but not limited to any direct, indirect, special, incidental, or consequential damages, and including, without limitation, lost revenues, lost profits, or loss of prospective economic advantage, resulting from the use or misuse of the information contained in this script.

The user of this script must not use this script for any illegal or unauthorized purpose. The user is solely responsible for any actions taken through the use of this script, and the author of this script will not be held liable for any damages or losses resulting from such actions.

By using this script, you confirm that you have read and understood this disclaimer and agree to be bound by its terms. If you do not agree with the terms of this disclaimer, you must not use this script.
