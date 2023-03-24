
<img width="513" src="https://user-images.githubusercontent.com/85976942/191089269-0918c8c1-db83-4f67-bfcb-7218697960d6.png">

___

DNS Resolver is a Python program that collects DNS record data for domains stored in a DNS server. It currently supports A, AAAA, MX, NS, SOA, TXT, and CNAME record types, and can save the collected data to a file or SQLite3 database. The program is under active development and will have more features in the future.

____

## Features

- Collect A, AAAA, MX, NS, SOA, TXT, CNAME records.
- Collect data into a text file.
- Add custom DNS IP address.
- Location information for type A record.
- Add resolved data to a SQLite3 database.

## Installation

### Requirements

- Python 3

### Instructions

1. Clone the repository:

    ```sh
    git clone https://github.com/ADK200/DNS_resolver.git
    ```

2. Install dependencies:

    ```sh
    cd DNS_resolver
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

2. Once you have edited the file, go back to the root directory of the program and run it:

    ```sh
    cd ..
    python3 main.py
    ```

3. During operation, the program will create a directory called `Output` in which the data files will be saved. File names are represented as date and time.

4. The program creates a resolver.db file in the root directory of the program and saves all the received data in it.

# Note
This program has only been tested on macOS and Linux operating systems. Use on other operating systems is not guaranteed to work.
