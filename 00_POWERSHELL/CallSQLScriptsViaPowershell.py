# Import libraries
import subprocess
import os

# Set the SQL Instance to connect to via PowerShell and the initial database
SQLInstance = "HomePc\\SQL2K24"  # Użycie podwójnych ukośników w nazwie instancji
SQLDatabase = "master"

# Define method that calls PowerShell and passes the command as a parameter
def runPSCommand(cmd):
    result = subprocess.run(cmd, capture_output=True, text=True)  # capture_output=True przechwytuje stdout i stderr
    return result

# Retrieve all .sql files in given directory and execute them by calling runPSCommand
FolderToCheck = r"C:\Users\User\Desktop\Travel_Planer\00_POWERSHELL"  # Użycie surowego łańcucha
for file in os.listdir(FolderToCheck):
    if file.endswith(".sql"):
        print(f"Executing .sql file: {os.path.join(FolderToCheck, file)}")
        
        # Przygotowanie komendy bez Query, tylko InputFile
        SQLCommand = [
            "PowerShell",
            "-ExecutionPolicy", "Unrestricted",
            "-Command", f"Invoke-Sqlcmd -ServerInstance {SQLInstance} -InputFile \"{os.path.join(FolderToCheck, file)}\" -Database {SQLDatabase} -TrustServerCertificate True"
        ]
        
        result = runPSCommand(SQLCommand)

        # Sprawdzamy kod zakończenia i błędy, jeśli są
        if result.returncode != 0:
            print(f"Error occurred: {result.stderr}")
        else:
            print(f"Output: {result.stdout}")
