import csv

filename_data = ['FILENAME',]
avx256_data = ['NUM_OF_AVX256_INST',]
avx512_data = ['NUM_OF_AVX512_INST',]
total_data = ['TOTAL_AVX_INST',]

"""This will generate CSV file for avx insturction"""
def write_csv( csvfilename ):

    with open(csvfilename, "w") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=filename_data)
        writer.writeheader()
        writer = csv.DictWriter(csvfile, fieldnames=avx256_data)
        writer.writeheader()
        writer = csv.DictWriter(csvfile, fieldnames=avx512_data)
        writer.writeheader()
        writer = csv.DictWriter(csvfile, fieldnames=total_data)
        writer.writeheader()
    
    return;
