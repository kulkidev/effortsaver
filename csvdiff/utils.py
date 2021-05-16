import csv
import logging
import pandas


def extract_reference_record_to_file(index_file, lookup_file, output_file):
    """
    This function extracts index field record from the lookup file
    :param index_file:
    :param lookup_file:
    :param outputfile:
    :return:
    """
    # load records from lookup file
    lookup_records = []
    field_names = ""
    with open(lookup_file, 'r') as lookup_file_ref:
        lookup_file_reader = csv.reader(lookup_file_ref,delimiter="|")
        field_names = lookup_file_reader.fieldnames
        logging.debug(f" lookup file fields are : {field_names}")
        for lookup_record in lookup_file_reader:
            lookup_records.append(lookup_record)

    output_records = []

    with open(index_file, 'r') as index_file_ref:
        index_file_ref_reader = csv.DictReader(index_file_ref)
        header_field = get_header_line(index_file_ref_reader.fieldnames)
        logging.debug(f" index file fields are : {header_field}")
        for row in index_file_ref_reader:
            for record in lookup_records:
                if row[header_field] == record[header_field]:
                    output_records.append(record)

    write_output_file(output_file=output_file,
                      field_names=field_names,
                      records=output_records)


def get_header_line(field_names):
    header_line = field_names[0]
    for index in range(1, len(field_names)):
        header_line = header_line + "|" + field_names[index]

    return header_line


def write_output_file(output_file, field_names, records):
    with open(output_file, "w", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=field_names, delimiter = "|")
        writer.writeheader()
        writer.writerows(records)


def read_csv_file_with_pandas(file_name):
    records = pd.read_csv(file_name, index_col=None, header=0, squeeze=True, delimiter="|",
                          nrows=10).to_dict(orient='records')
    for record in records:
        logging.info(f"record : {record}")


def compare_csv_file_using_index_field(file1, file2, index_field):
    output_lines = []
    field_names = ""
    src_records = []
    with open(file1, "r") as index_file:
        index_file_records = csv.DictReader(index_file, delimiter="|")
        for row in index_file_records:
            src_records.append(row)

    lookup_records = []
    with open(file2, "r") as lookup_file:
        lookup_file_records = csv.DictReader(lookup_file, delimiter="|")
        for row in lookup_file_records:
            lookup_records.append(row)

        for row in src_records:
            found = False
            for record in lookup_records:
                if record[index_field] == row[index_field]:
                    logging.info(f'for field : {row[index_field]} differences are : {dict_compare(row,record)}')
                    found = True
                    break
                if not found:
                    logging.info(f'The record for this field : {index_field} field : {row[index_field]} is not '
                                 f'present in {file2}')


def dict_compare(dictionary1, dictionary2):
    dictionary1_keys = set(dictionary1.keys())
    dictionary2_keys = set(dictionary2.keys())
    shared_keys = dictionary1_keys.intersection(dictionary2_keys)
    modified = {o: (dictionary1[o], dictionary2[o]) for o in shared_keys if dictionary1[o] != dictionary2[o]}

    return modified



