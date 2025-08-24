# Library Management System

This Project is made under Python course of TKA

## Overview
The Library Management System is a Python application that utilizes MySQL for managing books, members, and borrowed books in a library. This system allows users to perform various operations such as adding, removing, searching, and updating books and members, as well as borrowing and returning books.

## Features
- **Book Management**
  - Add new books to the library.
  - Remove books from the library.
  - Search for books by title.
  - List all books in the library.
  - Update book details.

- **Member Management**
  - Add new members to the library.
  - Remove members from the library.
  - Show a list of all members.

- **Borrowing and Returning Books**
  - Borrow books from the library.
  - Return borrowed books.
  - List all currently borrowed books.

## Requirements
- Python 3.x
- MySQL Server
- `mysql-connector-python` library

## Installation
1. **Clone the repository:**
   ```bash
    git clone https://github.com/mayurcodes01/Library_Management_System_With_MySQL.git

   ```

2. **Install the required library:**
   ```bash
   pip install mysql-connector-python
   ```

3. **Set up the MySQL database:**
   - Create a database named `tka`.
   - Create the necessary tables (`books`, `members`, `borrowed_books`) with appropriate fields.

## Database Schema
### Books Table
- `isbn`: VARCHAR (Primary Key)
- `title`: VARCHAR
- `author`: VARCHAR
- `quantity`: INT
- `year`: INT

### Members Table
- `member_id`: INT (Primary Key, Auto Increment)
- `name`: VARCHAR
- `email`: VARCHAR

### Borrowed Books Table
- `borrow_id`: INT (Primary Key, Auto Increment)
- `member_id`: INT (Foreign Key)
- `isbn`: VARCHAR (Foreign Key)
- `borrow_date`: DATE

## Usage
1. Run the application:
   ```bash
   python LibraryManagementSystem_MySQL.py
   ```

2. Follow the on-screen menu to perform various operations.

## Example Operations
- To add a book, select option 1 and provide the required details.
- To borrow a book, select option 10 and enter the member ID and ISBN of the book.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Thanks to the contributors and the open-source community for their support and resources.
