

<img width="317" alt="Screen Shot 2023-12-08 at 11 29 19 AM" src="https://github.com/ariolus/DRAST/assets/85976942/34e6f026-ec53-4ae9-95dc-93fe8d0a47ab">

___

DRAST is a versatile Python program designed to analyze and collect DNS record data for domains stored in a DNS server. It supports a variety of record types, including A, AAAA, MX, NS, SOA, TXT, CNAME, PTR, SRV and CAA. The collected data can be saved to a file or an SQLite3 database.
____

## Features

- Collect A, AAAA, MX, NS, SOA, TXT, CNAME, PTR, SRV, CAA records.
- Collect data into a text file.
- Add custom DNS IP address.
- Location information for type A record.
- Add collected data to an SQLite3 database.
- Suspended mode for continuous data collection and program operation, allowing users to modify `dns_domains.txt` while the program runs.
- Interactive and command-line modes for flexibility in usage.

## Installation

### Requirements

- Python 3

### Instructions

1. Clone the repository:

    ```sh
    git clone https://github.com/ariolus/DRAST
    ```

2. Install dependencies:

    ```sh
    cd DRUST
    pip3 install -r requirements.txt
    ```

## Usage

1. To add and edit a bulk list with domains, go to the `Domain_list` directory and edit the `dns_domains.txt` file:

    ```sh
    cd Domain_list
    vim dns_domains.txt
    ```

    Add the domains each from a new line to the file in the following formats:

    ```
    example.com
    www.example.com
    ```

    Alternatively, you can use the `-i` flag to specify a file containing a list of domains for bulk processing:

    ```sh
    python3 main.py -b -i /path/to/file.txt
    ```

    The file should contain one domain per line.

2. Once you have edited the file, you can run the program in one of two modes:

   - **Interactive Mode:**

     Use the following command for interactive mode:

     ```sh
     python3 main.py -I
     ```

     Interactive mode allows real-time interaction with the program.

   - **Normal Mode:**

     For more options and information, you can check the help menu:
     
     ```sh
     python3 main.py -h
     ```

     Example: Resolve a single domain in JSON format:
     
     ```sh
     python3 main.py -s example.com -j
     ```

     Example: Bulk resolve domains from a file in dictionary format:
     
     ```sh
     python3 main.py -b -i /path/to/file.txt -d
     ```

     Example: Use SQL mode with a custom DNS IP address and suspended mode:
    
     ```sh
     python3 main.py --sql --dns 8.8.8.8 -S
     ```

3. During operation, the program will create a directory called `Output` in which the data files will be saved. File names are represented as date and time. Also, if there is a need to use another output directory, the flag '-o PATH' can be used.

4. The program creates a `resolver.db` file in the root directory of the program and saves all the received data in it. When the program is in suspended mode, users can modify the `dns_domains.txt` file without disrupting the data collection process. To enter suspended mode, press `CTRL + Z` in the terminal. To resume the program, use the `fg` command.

## Note
This program has only been tested on macOS and Linux operating systems.

