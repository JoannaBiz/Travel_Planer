Based on: https://www.udemy.com/course/python-windows-sql-server/ 

# Travel Planner  

**Travel Planner** is an application designed to help users plan their trips by managing information about destinations, schedules, and costs.  

## Table of Contents  

- [Features](#features)  
- [Technologies](#technologies)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Project Structure](#project-structure)  
- [Author](#author)  
- [License](#license)  

## Features  

- **Manage travel destinations**: Add, edit, and delete information about destinations.  
- **Schedule planning**: Set departure and return dates.  
- **Cost estimation**: Estimate travel expenses, including transport, accommodation, and attractions.  

## Technologies  

- **Backend**: Python  
- **Database**: T-SQL  

## Installation  

1. **Clone the repository**:  

   ```bash
   git clone https://github.com/JoannaBiz/Travel_Planer.git
   cd Travel_Planer
   ```

2. **Install required dependencies**:  

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up the database**:  

   - Create a database in a system that supports T-SQL.  
   - Import the scripts located in the `SQL` folder to create necessary tables and procedures.  

4. **Configure the database connection**:  

   - Edit the configuration file to include your database credentials.  

## Usage  

1. **Run the application**:  

   ```bash
   python main.py
   ```

2. **Use the application features**:  

   - Add new travel destinations.  
   - Plan travel schedules.  
   - Estimate travel expenses.  

## Project Structure  

- `00_CONNECT_SQL/`: Scripts for database connection.  
- `00_GUI/`: User interface files.  
- `00_PICTURES/`: Images used in the application.  
- `00_POWERSHELL/`: PowerShell scripts supporting the application.  
- `FUNCTION/`: Function definitions used in the app.  
- `IMPORT/`: Data import-related files.  
- `IMPORT_FILES/`: Example import files.  
- `PROCEDURES/`: Stored procedures for the database.  
- `SQL/`: SQL scripts for database creation and management.  
- `SQL_CRUD/`: SQL CRUD operations.  

## Author  

- **JoannaBiz** - [GitHub Profile](https://github.com/JoannaBiz)  

## License  

This project is licensed under the MIT License.  

---

This README provides an overview of the "Travel Planner" project by JoannaBiz. For further details, refer to the project’s documentation or contact the author.
