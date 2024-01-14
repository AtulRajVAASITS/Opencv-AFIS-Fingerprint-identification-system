# Opencv-AFIS-Fingerprint-identification-system
This is a python opencv program to find same fingerprint based on the opencv shift model from a database. This is a research based model not yet for consumer grade but will be made into consumer grade in a few years and it does not use minutiae features for fingerprint detection.
The requierments are python 3, compatible opencv version to python 3. Also this is tested in debain environment with python version 3 and opencv version 4.5.1 .
Usage:
python3 fp.py
When running the file keep the fingerprint you want to be detected from the database named as s.png and change the database location in the fp.py file in two place where the location is displayed, by default it is "/home/jake/Downloads/d1"). Change it to your database location
This program works only with scanned prints not latent prints.
