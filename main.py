from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import create, read, custom_query, update, delete


def interactive_menu():

    while True:
        print("\n--- ETL-Query Interactive CLI ---")
        print("Please choose an action:")
        print("1. Extract data")
        print("2. Load transformed data")
        print("3. Query the database")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            print("Extracting data...")
            extract()
            print("Data extracted successfully.")

        elif choice == "2":
            print("Transforming and loading data...")
            load()
            print("Data loaded successfully.")

        elif choice == "3":
            query_menu()

        elif choice == "4":
            print("Exiting the CLI. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")


def query_menu():
    """
    Show query menu for CRUD operations on the database.
    """
    while True:
        print("\n--- Query Menu ---")
        print("Please choose a query action:")
        print("1. Create a new entry")
        print("2. Read data")
        print("3. Update an entry")
        print("4. Delete an entry")
        print("5. Execute custom query on table")
        print("6. Go back to main menu")

        query_choice = input("Enter your choice (1-5): ")

        if query_choice == "1":
            entry = input("Enter the 6 values for the entry (comma-separated): ").split(
                ","
            )
            if len(entry) == 6:
                entry = tuple(
                    map(str.strip, entry)
                )  # Strip whitespace and convert to tuple
                print(f"Inserting entry: {entry}")
                print(create(entry))
            else:
                print("Error: You must enter exactly 6 values.")

        elif query_choice == "2":
            print(read())

        elif query_choice == "3":
            column = input("Enter the column to update: ").strip()
            new_value = input(f"Enter the new value for {column}: ").strip()
            condition_column = input(
                "Enter the condition column for WHERE clause: "
            ).strip()
            condition_value = input(
                f"Enter the condition value for {condition_column}: "
            ).strip()
            print(
                f"Updating {column} to {new_value} where {condition_column} = {condition_value}"
            )
            print(update(column, new_value, condition_column, condition_value))

        elif query_choice == "4":
            condition_column = input(
                "Enter the condition column for WHERE clause: "
            ).strip()
            condition_value = input(
                f"Enter the condition value for {condition_column}: "
            ).strip()
            print(f"Deleting entry where {condition_column} = {condition_value}")
            print(delete(condition_column, condition_value))

        elif query_choice == "5":
            query = input(
                "Enter a custom SQL query or press Enter to run the default query: "
            ).strip()
            if query:
                print(f"Executing custom query: {query}")
                print(custom_query(query))
            else:
                print("Reading data using default query...")
                print(read())

        elif query_choice == "6":
            print("Going back to main menu...")
            break

        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    interactive_menu()
