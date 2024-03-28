#!/usr/bin/python3

"""
    Reads stdin line by line and computes metrics.
    Input format: <IP Address> - [<date>]
    "GET /projects/260 HTTP/1.1" <status code> <file size>
    After every 10 lines and/or a keyboard interruption (CTRL + C),
    prints statistics from the beginning:
        - Total file size: <total size>
        - Number of lines by status code:
            - possible status code: 200, 301, 400, 401, 403, 404, 405, and 500
            - if a status code doesn’t appear or is not an integer,
            don’t print anything for this status code
            - format: <status code>: <number>
        - status codes are printed in ascending order
    """

import sys

total_file_size = 0
status_code_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0,
                     404: 0, 405: 0, 500: 0}
line_count = 0

try:
    for line in sys.stdin:
        line = line.strip()
        parts = line.split()
        if len(parts) != 10:
            continue
        status_code = int(parts[8])
        file_size = int(parts[9])
        total_file_size += file_size
        status_code_count[status_code] += 1
        line_count += 1
        if line_count % 10 == 0:
            print("Total file size:", total_file_size)
            for code in sorted(status_code_count.keys()):
                if status_code_count[code] > 0:
                    print(f"{code}: {status_code_count[code]}")
            print()

except KeyboardInterrupt:
    print("\nKeyboard interruption detected. Printing final statistics...")
    print("Total file size:", total_file_size)
    for code in sorted(status_code_count.keys()):
        if status_code_count[code] > 0:
            print(f"{code}: {status_code_count[code]}")
