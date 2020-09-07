import sys, os, zipfile, tarfile
import urllib.request
import requests
from py7zr import SevenZipFile

#where_to_save = '../Data/'
where_to_save = 'Data/'

# create data directory
if not os.path.exists(where_to_save):
    os.makedirs(where_to_save)

# import Birthdays
url = 'https://raw.githubusercontent.com/guiwitz/Rdatasets/master/csv/mosaicData/Birthdays.csv'
urllib.request.urlretrieve(url, where_to_save+'Birthdays.csv')

# import BBBC006
if not os.path.isdir(where_to_save+'BBBC006_v1_images_z_16'):
    url = 'https://data.broadinstitute.org/bbbc/BBBC006/BBBC006_v1_images_z_16.zip'
    urllib.request.urlretrieve(url, where_to_save+'BBBC006_v1_images_z_16.zip')
    # unzip
    with zipfile.ZipFile(where_to_save+'BBBC006_v1_images_z_16.zip', 'r') as zip_ref:
        zip_ref.extractall(where_to_save)
    os.remove(where_to_save+'BBBC006_v1_images_z_16.zip')

# download NYC data
if not os.path.isdir(where_to_save+'NYC_Taxi'):
    os.makedirs(where_to_save+'NYC_Taxi')
    url = 'https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2020-01.csv'
    urllib.request.urlretrieve(url, where_to_save+ 'NYC_Taxi'+ '/' + 'yellow_tripdata_2020-01.csv')
    url = 'https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2020-02.csv'
    urllib.request.urlretrieve(url, where_to_save+ 'NYC_Taxi'+ '/' + 'yellow_tripdata_2020-02.csv')
    url = 'https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2020-03.csv'
    urllib.request.urlretrieve(url, where_to_save+ 'NYC_Taxi'+ '/' + 'yellow_tripdata_2020-03.csv')
    url = 'https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2020-04.csv'
    urllib.request.urlretrieve(url, where_to_save+ 'NYC_Taxi'+ '/' + 'yellow_tripdata_2020-04.csv')
    url = 'https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2020-05.csv'
    urllib.request.urlretrieve(url, where_to_save+ 'NYC_Taxi'+ '/' + 'yellow_tripdata_2020-05.csv')

    url = 'https://s3.amazonaws.com/nyc-tlc/misc/taxi+_zone_lookup.csv'
    urllib.request.urlretrieve(url, where_to_save+'NYC_Taxi'+ '/' + 'taxi+_zone_lookup.csv')

# download wikipedia data
if not os.path.isdir(where_to_save+'20161101-current_content-parts-1-50-pageids-12-117215'):
    url = 'https://zenodo.org/record/834557/files/20161101-current_content-parts-1-50-pageids-12-117215.7z?download=1'
    urllib.request.urlretrieve(url, where_to_save+'TokTrack.7z')
    archive = SevenZipFile(where_to_save+'TokTrack.7z', mode='r')
    archive.extractall(where_to_save)
    archive.close()

#url = 'https://zenodo.org/record/834557/files/20161101-current_content-parts-101-150-pageids-418317-1081580.7z?download=1'