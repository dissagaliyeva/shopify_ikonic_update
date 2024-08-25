import pandas as pd
import requests
from lxml import etree
from fetch_all_products import *

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
    
def get_products_to_add(new_bags, new_others):
    old_bags = pd.read_csv('bags.csv')
    old_others = pd.read_csv('other_products.csv')
    
    bags = new_bags[~new_bags['Sku Styleisnow'].isin(old_bags['Sku Styleisnow'].values.tolist())]
    others = new_others[~new_others['Sku Styleisnow'].isin(old_others['Sku Styleisnow'].values.tolist())]
    
    bags.to_csv('bags_to_add.csv', index=False)
    others.to_csv('others_to_add.csv', index=False)
    
    # TODO: update the old bags!!!!!!!!!!!
    # bags.to_csv('bags.csv', index=False)
    # others.to_csv('all_others.csv', index=False)


def update_products():
    import requests
    url = "http://pim.coltorti.it:8080/csvExport/export/00000000000000000363/allProducts.csv"
    username = "int"
    password = "zUVv9cXR"
    
    response = requests.get(url, auth=(username, password))
    
    if response.status_code == 200:
        with open('all_products.csv', 'wb') as file:
            file.write(response.content)
        print('File added successfully')
        new_bags, new_others = fix_file('all_products.csv')
        get_products_to_add(new_bags, new_others)
    else:
        print(f"Failed to download the file. Status code: {response.status_code}")


if __name__ == '__main__':
    df = get_data()
    
    if df is not None:
        df = df[['id', 'size', 'id_manufacturer', 'variant', 'qty']]
        df.rename(columns={'id': 'SKU FULL'}, inplace=True)

        bags = pd.read_csv('bags.csv')
        bags_merged = bags[bags['SKU FULL'].isin(df['SKU FULL'])]
        bags_merged['Qty'] = df[df['SKU FULL'].isin(bags_merged['SKU FULL'])]['qty'].values
        bags_merged[['Sku Styleisnow', 'Qty']].to_csv('updated_bags.csv', index=False)
        
        other = pd.read_csv('other_products.csv')
        other_merged = other[other['SKU FULL'].isin(df['SKU FULL'])]
        other_merged['Qty'] = df[df['SKU FULL'].isin(other_merged['SKU FULL'])]['qty'].values
        other_merged.to_csv('updated_other.csv', index=False)
        
        update_products()
        
        del bags, df, other, bags_merged, other_merged
        