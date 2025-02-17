import sqlite3
import csv
import os

def create_books_database(cleaned_books_data.csv):
    #verify if file exists
    if not os.path.exists(cleaned_books_data.csv):
        print(f"\nError: File '{cleaned_books_data.csv}' not found in the current directory.")
        print(f"Current directory: {os.getcwd()}")
        print("\nFiles in current directory:")
        for file in os.listdir():
            print(f"- {file}")
        return False
    
    try:
        #connect to SQLite database
        conn = sqlite3.connect('books.db')
        cursor = conn.cursor()
        
        #create table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                price REAL NOT NULL,
                availability INTEGER NOT NULL,
                rating INTEGER NOT NULL
            )
        ''')
        
        #clear existing data
        cursor.execute('DELETE FROM books')
        
        #read CSV file and insert data
        with open(cleaned_books_data.csv, 'r', encoding='utf-8') as file:
            #print first few lines of CSV for debugging
            print("\nFirst few lines of CSV file:")
            print(file.readline())  # Header line
            print(file.readline())  # First data line
            file.seek(0)  # Reset file pointer to beginning
            
            csv_reader = csv.DictReader(file)
            records_inserted = 0
            
            for row in csv_reader:
                try:
                    cursor.execute('''
                        INSERT INTO books (title, price, availability, rating)
                        VALUES (?, ?, ?, ?)
                    ''', (
                        row['title'],
                        float(row['price']),
                        int(row['availability']),
                        int(row['rating'])
                    ))
                    records_inserted += 1
                except KeyError as e:
                    print(f"\nError: Missing column in CSV file: {e}")
                    print("Expected columns: title, price, availability, rating")
                    print("Found columns:", list(row.keys()))
                    return False
                
        # commit changes
        conn.commit()
        print(f"\nsuccessfully inserted {records_inserted} books into the database.")
        return True
        
    except sqlite3.Error as e:
        print(f"\ndatabase error: {e}")
        return False
    except Exception as e:
        print(f"\nunexpected error: {e}")
        return False
    finally:
        if 'conn' in locals():
            conn.close()

def query_database():
    try:
        conn = sqlite3.connect('books.db')
        cursor = conn.cursor()
        
        print("\nDatabase Analysis:")
        
        # Check if we have any data
        cursor.execute('SELECT COUNT(*) FROM books')
        count = cursor.fetchone()[0]
        
        if count == 0:
            print("No data found in the database.")
            return
            
        # Average price by rating
        print("\n1. Average price by rating:")
        cursor.execute('''
            SELECT rating, COUNT(*) as count, ROUND(AVG(price), 2) as avg_price
            FROM books
            GROUP BY rating
            ORDER BY rating
        ''')
        for row in cursor.fetchall():
            print(f"Rating {row[0]}: {row[1]} books, Average price: ${row[2]}")
        
        # Price statistics
        print("\n2. Price statistics:")
        cursor.execute('''
            SELECT 
                MIN(price) as min_price,
                MAX(price) as max_price,
                ROUND(AVG(price), 2) as avg_price
            FROM books
        ''')
        stats = cursor.fetchone()
        print(f"Min price: ${stats[0]}")
        print(f"Max price: ${stats[1]}")
        print(f"Average price: ${stats[2]}")
        
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
    print("Current directory:", os.getcwd())
    csv_file = input("cleaned_books_data.csv: ")
    
    if create_books_database(cleaned_books_data.csv):
        query_database()