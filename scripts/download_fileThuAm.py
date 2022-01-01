# -*- coding: utf-8 -*-
#!/usr/bin/env python3

# Import module
import gdown

# Parameters
url = 'https://drive.google.com/uc?id=1X2O3-WINfAf0AbcdAjViUt3Z8yihotD1'
output = 'fileThuAm.zip'

# Download
gdown.download(url, output, quiet=False)
