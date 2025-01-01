To compare two Hive tables to check if they have the same DML (Data Manipulation Language) structure using Python, you can use the `pyhive` library to connect to Hive and query the table schemas. Here’s a step-by-step approach:

### Steps:
1. **Connect to Hive**: Use the `pyhive` library to establish a connection with the Hive server.
2. **Retrieve Table Schema**: Query the `DESCRIBE FORMATTED` or `SHOW CREATE TABLE` output for each table to get the schema.
3. **Compare Schemas**: Parse the results and compare the columns, data types, and other attributes to ensure compatibility.

### Code Example:
```python
from pyhive import hive
import difflib

# def get_table_schema(connection, database, table):
#     """Fetch the table schema using SHOW CREATE TABLE."""
#     query = f"SHOW CREATE TABLE {database}.{table}"
#     cursor = connection.cursor()
#     cursor.execute(query)
#     schema = "\n".join(row[0] for row in cursor.fetchall())
#     return schema

# def compare_table_schemas(schema1, schema2):
#     """Compare two schemas and return differences."""
#     diff = difflib.unified_diff(
#         schema1.splitlines(), schema2.splitlines(), lineterm="", 
#         fromfile="Table1 Schema", tofile="Table2 Schema"
#     )
#     return "\n".join(diff)

# # Hive connection details
# hive_host = "your_hive_host"
# hive_port = 10000
# hive_username = "your_username"
# hive_database = "your_database"

# Tables to compare
table1 = "table_name_1"
table2 = "table_name_2"

try:
    # Connect to Hive
    conn = hive.Connection(host=hive_host, port=hive_port, username=hive_username, database=hive_database)
    
    # Fetch schemas
    schema1 = get_table_schema(conn, hive_database, table1)
    schema2 = get_table_schema(conn, hive_database, table2)
    
    # Compare schemas
    differences = compare_table_schemas(schema1, schema2)
    if differences:
        print("Schemas are different:\n")
        print(differences)
    else:
        print("Schemas are identical. You can safely load data.")
except Exception as e:
    print(f"Error: {e}")
```

### Key Notes:
1. **Install Dependencies**:
   - Install `pyhive` using pip: `pip install pyhive`.
2. **Schema Comparison**:
   - Use `SHOW CREATE TABLE` as it provides the complete DML structure of the table.
   - Alternatively, use `DESCRIBE FORMATTED` if you need more details.
3. **Error Handling**:
   - Handle cases where tables do not exist or connection fails.
4. **Cluster Access**:
   - Ensure the Python script has access to the Hive cluster, including appropriate permissions.

This script will help you compare the schemas and decide if the tables are compatible for data loading.