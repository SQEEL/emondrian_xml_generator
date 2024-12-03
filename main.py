import xml.etree.ElementTree as ET
import xml.dom.minidom
import clickhouse_connect


class ClickHouseClient:
    """
    A wrapper for ClickHouse client interactions.
    """

    def __init__(self, host, port, database, username, password):
        self.client = clickhouse_connect.get_client(
            host=host, port=port, username=username, password=password, database=database
        )

    def execute_query(self, query):
        """
        Executes a query and returns the result rows.
        """
        try:
            result = self.client.query(query)
            return result.result_rows
        except Exception as e:
            print(f"Error executing query: {e}")
            return []


def get_tables(client, database, source_table):
    """
    Retrieves a list of table names matching the source table.
    """
    query = f"""
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = '{database}'
          AND table_name = '{source_table}'
    """
    return [row[0] for row in client.execute_query(query)]


def get_columns(client, database, table):
    """
    Retrieves a list of column names for a given table.
    """
    query = f"""
        SELECT name
        FROM system.columns
        WHERE database = '{database}' AND table = '{table}'
    """
    return [row[0] for row in client.execute_query(query)]


def generate_schema(host, port, database, username, password, schema_name, source_table):
    """
    Generates an XML schema based on ClickHouse table structure.
    """
    client = ClickHouseClient(host, port, database, username, password)
    schema_element = ET.Element("Schema", name=schema_name)

    # Retrieve source tables
    source_tables = get_tables(client, database, source_table)
    if not source_tables:
        print(f"No tables found for {source_table}.")
        return

    for table in source_tables:
        # Add Cube and Table elements
        cube = ET.SubElement(schema_element, "Cube", name=table)
        ET.SubElement(cube, "Table", name=table)

        # Retrieve columns for the current table
        columns = get_columns(client, database, table)
        if not columns:
            print(f"No columns found for table {table}. Skipping.")
            continue

        # Add Dimensions and Measures
        for col in columns:
            if col.startswith("n_"):
                ET.SubElement(
                    cube,
                    "Measure",
                    name=col.capitalize(),
                    column=col,
                    aggregator="sum",
                    formatString="#,###.00",
                )
            else:
                dimension_name = col.capitalize()
                dimension = ET.SubElement(cube, "Dimension", name=dimension_name)
                hierarchy = ET.SubElement(
                    dimension,
                    "Hierarchy",
                    hasAll="true",
                    allMemberName=f"All {dimension_name}",
                )
                ET.SubElement(
                    hierarchy,
                    "Level",
                    name=dimension_name,
                    column=col,
                    uniqueMembers="true",
                )

    # Beautify and save XML
    save_schema_to_file(schema_element, f"{source_table}.xml")


def save_schema_to_file(schema_element, filename):
    """
    Converts XML to a pretty string and writes it to a file.
    """
    xml_str = ET.tostring(schema_element, encoding="unicode", method="xml")
    pretty_xml_str = xml.dom.minidom.parseString(xml_str).toprettyxml(indent="    ")

    try:
        with open(filename, "w") as file:
            file.write(pretty_xml_str)
        print(f"XML schema has been written to {filename}")
    except Exception as e:
        print(f"Failed to write XML to file: {e}")


if __name__ == "__main__":
    # Connection details
    host = 'your_host'
    port = 8123
    database = 'your_database'
    username = 'your_username'
    password = 'your_password'

    # Schema and table details
    schema_name = 'your_schema'
    source_table = 'your_table'

    generate_schema(
        host=host,
        port=port,
        database=database,
        username=username,
        password=password,
        schema_name=schema_name,
        source_table=source_table,
    )
