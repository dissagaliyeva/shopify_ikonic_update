import pandas as pd
import requests
from lxml import etree

# URL of the XML file
url = "https://www.styleisnow.com/feeds/stock_xml_incremental.xml"


def get_data():

    # Send a GET request to fetch the XML content
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the XML content
        root = etree.fromstring(response.content)
        
        # Find all <item> elements
        items = root.findall('.//item')
        
        # Convert the <item> elements to a list of dictionaries
        data = []
        for item in items:
            item_data = {}
            for child in item:
                # Remove the namespace from the tag
                tag_name = str(child.tag).split('}')[-1]  # Splits the tag at '}' and takes the part after it
                item_data[tag_name] = child.text  # Store the tag's text content
            data.append(item_data)
        
        # Convert the list of dictionaries to a DataFrame
        return pd.DataFrame(data)
    else:
        print("Failed to retrieve the XML content")
        return None
    


if __name__ == '__main__':
    df = get_data()
    
    if df is not None:
        df = df[['id', 'size', 'id_manufacturer', 'variant', 'qty']]
        df.rename(columns={'id': 'SKU FULL'}, inplace=True)

        bags = pd.read_csv('bags.csv')
        bags_merged = bags[bags['SKU FULL'].isin(df['SKU FULL'])]
        bags_merged['Qty'] = df[df['SKU FULL'].isin(bags_merged['SKU FULL'])]['qty'].values
        bags_merged[['Sku Styleisnow', 'Qty']].to_csv('updated_bags.csv', index=False)
        # bags_merged.to_csv('updated_bags.csv', index=False)
        
        other = pd.read_csv('other_products.csv')
        other_merged = other[other['SKU FULL'].isin(df['SKU FULL'])]
        other_merged['Qty'] = df[df['SKU FULL'].isin(other_merged['SKU FULL'])]['qty'].values
        
        other_single = other_merged[other_merged['Barcode'].str.len() == 1].to_csv('updated_single_others.csv')
        other_multiple = other_merged[other_merged['Barcode'].str.len() != 1].to_csv('updated_multiple_others.csv')
        
        del bags, df, other, bags_merged, other_merged
        