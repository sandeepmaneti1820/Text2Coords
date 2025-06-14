import xml.etree.ElementTree as ET

def read_node_data(search_text, xml_file="window_dump.xml"):
    try:
        # Parse the XML file
        tree = ET.parse(xml_file)
        root = tree.getroot()

        # List to collect matching node data
        matching_nodes = []

        # Iterate through all <node> elements and check for matching 'text'
        for node in root.iter('node'):
            if node.get('text') == search_text:
                bounds = node.get('bounds')
                if bounds:
                    # Extract top-left x, y coordinates from bounds string "[x1,y1][x2,y2]"
                    coords = bounds.strip("[]").split("][")[0].split(",")
                    x, y = int(coords[0]), int(coords[1])

                    matching_nodes.append({
                        'index': node.get('index'),
                        'text': search_text,
                        'bounds': bounds,
                        'x': x,
                        'y': y
                    })

        if matching_nodes:
            result = matching_nodes[0]
            print(f"x: {result['x']}, y: {result['y']} (type: {type(result['x'])})")
            return result['x'], result['y']
        else:
            print(f"No node found with text: '{search_text}'")
            return None, None

    except ET.ParseError as e:
        print(f"Error parsing XML: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Example usage
read_node_data("Search links")
