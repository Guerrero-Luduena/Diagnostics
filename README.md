# Diagnostics
#Hola, mundo! / Hello, world!

Repo is for the downloading of data files (csv,zip, xlsx.. etc) from urls.

2 scripts to use:
1) download_test_v1.ipynb
takes xlsx file list of 20160321_data_sets.xlsx, and downloads all files within it to folder structure outside of the Diagnostics repo.

NB. NOTE! CAREFUL with using xlsx files in git, if you want to make edits then please create a new .xlsx file each time a new request is run.

2) process_monthly_diag_wait_times_v1.ipynb
takes the monthly diagnostic wait times, unzips all and combines all csv's into one combined file with additional columns.

NB. The resulting csv is large. - 1.6GB
