import sys, os, zipfile, tarfile
import urllib.request
import requests

#where_to_save = '../Data/'
where_to_save = 'Data/'

#create data directory
if not os.path.exists(where_to_save):
    os.makedirs(where_to_save)
    
#import Birthdays
url = 'https://raw.githubusercontent.com/guiwitz/Rdatasets/master/csv/mosaicData/Birthdays.csv'  
urllib.request.urlretrieve(url, where_to_save+'Birthdays.csv')

'''#import BBBC032
if not os.path.isdir(where_to_save+'BBBC032_v1_dataset'):
    os.makedirs(where_to_save+'BBBC032_v1_dataset')
    url = 'https://data.broadinstitute.org/bbbc/BBBC032/BBBC032_v1_dataset.zip'
    urllib.request.urlretrieve(url, where_to_save+'BBBC032_v1_dataset.zip')
    #unzip
    with zipfile.ZipFile(where_to_save+'BBBC032_v1_dataset.zip', 'r') as zip_ref:
        zip_ref.extractall(where_to_save+'BBBC032_v1_dataset')
    os.remove(where_to_save+'BBBC032_v1_dataset.zip')
    
#download wikipedia data
if not os.path.isdir(where_to_save+'TokTrack'):
    os.makedirs(where_to_save+'TokTrack')
    url = 'https://zenodo.org/record/834557/files/20161101-current_content-parts-1-50-pageids-12-117215.7z?download=1'
    urllib.request.urlretrieve(url, where_to_save+'TokTrack.zip')
    archive = SevenZipFile('TokTrack.7z')
    archive.extractall()
'''
