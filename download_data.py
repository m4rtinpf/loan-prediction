import urllib.request
import shutil
import os
import tarfile

url = 'http://rapidsai-data.s3-website.us-east-2.amazonaws.com/notebook-mortgage-data/mortgage_2000-2015.tgz'
file_name = url.split('/')[-1]
# Check if the file exists
if not os.path.isfile(file_name):
    # Download the file from "url" and save it as "file_name"
    with urllib.request.urlopen(url) as response, open(file_name, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)
extract_path = 'data'
# Open the tar file
tar = tarfile.open(file_name, "r")
# Loop through each file and extract only the ones that are needed
for f in [
    'acq/Acquisition_2015Q1.txt',
    'acq/Acquisition_2014Q4.txt',
    'acq/Acquisition_2014Q3.txt',
    'acq/Acquisition_2014Q2.txt',
    'acq/Acquisition_2014Q1.txt',
    'acq/Acquisition_2013Q4.txt',
    'acq/Acquisition_2013Q3.txt',
    'acq/Acquisition_2013Q2.txt',
    'acq/Acquisition_2013Q1.txt',
    'acq/Acquisition_2012Q4.txt',
    'acq/Acquisition_2012Q3.txt',
    'acq/Acquisition_2012Q2.txt',
    'acq/Acquisition_2012Q1.txt',
    'perf/Performance_2015Q1.txt',
    'perf/Performance_2014Q4.txt',
    'perf/Performance_2014Q3.txt',
    'perf/Performance_2014Q2.txt',
    'perf/Performance_2014Q1.txt',
    'perf/Performance_2013Q4.txt',
    'perf/Performance_2013Q3.txt_1',
    'perf/Performance_2013Q3.txt_0',
    'perf/Performance_2013Q2.txt_1',
    'perf/Performance_2013Q2.txt_0',
    'perf/Performance_2013Q1.txt_1',
    'perf/Performance_2013Q1.txt_0',
    'perf/Performance_2012Q4.txt_1',
    'perf/Performance_2012Q4.txt_0',
    'perf/Performance_2012Q3.txt_1',
    'perf/Performance_2012Q3.txt_0',
    'perf/Performance_2012Q2.txt_1',
    'perf/Performance_2012Q2.txt_0',
    'perf/Performance_2012Q1.txt_1',
    'perf/Performance_2012Q1.txt_0',
]:
    tar.extract(f, path=extract_path)

# Remove tar file
os.remove(file_name)
# Move files from "acq" and "perf" directories to "data"
for directory in ['acq', 'perf']:
    for f in os.listdir('{0}/{1}'.format(extract_path, directory)):
        shutil.move('{0}/{1}/{2}'.format(extract_path, directory, f), extract_path)
    # Remove directory
    os.rmdir('{0}/{1}'.format(extract_path, directory))
