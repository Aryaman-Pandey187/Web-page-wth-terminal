import difflib

def normalize_schema(schema):
    """Normalize schema string for consistent comparison."""
    return "\n".join(
        line.strip() for line in schema.splitlines() if line.strip()
    )

def compare_schemas(schema1, schema2):
    """Compare two schema strings."""
    schema1_normalized = normalize_schema(schema1)
    schema2_normalized = normalize_schema(schema2)
    
    # Compare using difflib
    diff = difflib.unified_diff(
        schema1_normalized.splitlines(), 
        schema2_normalized.splitlines(), 
        lineterm="", 
        fromfile="Schema1", 
        tofile="Schema2"
    )
    return "\n".join(diff)

# Example schemas as strings
schema1 = """
CREATE TABLE table1 (
    id INT,
    name STRING,
    age INT
)
STORED AS PARQUET
"""

schema2 = """
CREATE TABLE table2 (
    id INT,
    name STRING,
    age INT
)
STORED AS PARQUET
"""

# Compare the schemas
differences = compare_schemas(schema1, schema2)
if differences:
    print("Schemas are different:\n")
    print(differences)
else:
    print("Schemas are identical. You can safely load data.")
