import pandas as pd
import numpy as np

categories = [
    "Accessories", "Backpacks", "Backpacks and Duffel bags", "Bags", "beachwear", 
    "Beauty", "Beauty & Lifestyle > Beauty > Beauty Accessories", 
    "Beauty & Lifestyle > Beauty > Body", "Beauty & Lifestyle > Beauty > Face", 
    "Beauty & Lifestyle > Beauty > Face > Body", "Beauty & Lifestyle > Beauty > Hair", 
    "Beauty & Lifestyle > Beauty > Make up", "Beauty & Lifestyle > Beauty > Perfume", 
    "Beauty & Lifestyle > Lifestyle > Books", "Beauty & Lifestyle > Lifestyle > Fragrances & Candles", 
    "Beauty & Lifestyle > Lifestyle > Home & Living", 
    "Beauty & Lifestyle > Lifestyle > Home & Living > Tableware", 
    "Beauty & Lifestyle > Lifestyle > Pets", "Beauty & Lifestyle > Lifestyle > Tableware", 
    "Beauty & Lifestyle > Lifestyle > Textiles", "Beauty & Lifestyle > Lifestyle > Umbrella", 
    "Beauty accessories", "Beauty and Lifestyle", 
    "Beauty and Lifestyle > Beauty > Beauty accessories", 
    "Beauty and Lifestyle > Beauty > Body", "Beauty and Lifestyle > Beauty > Face", 
    "Beauty and Lifestyle > Beauty > Fragrances", "Beauty and Lifestyle > Beauty > Hair", 
    "Beauty and Lifestyle > Beauty > Make up", "Beauty and Lifestyle > Lifestyle > Books", 
    "Beauty and Lifestyle > Lifestyle > Candles and Home fragrances", 
    "Beauty and Lifestyle > Lifestyle > Hi-Tech", 
    "Beauty and Lifestyle > Lifestyle > Home&Living", 
    "Beauty and Lifestyle > Lifestyle > Pets", "Beauty and Lifestyle > Lifestyle > Tablewear", 
    "Beauty and Lifestyle > Lifestyle > Textiles", 
    "Beauty and Lifestyle > Lifestyle > Travels", 
    "Beauty and Lifestyle > Lifestyle > Umbrellas", "beauty-lifestyle", 
    "Belt bags", "Beltbags", "belts", "Body", "Books", 
    "Candles and Home fragrances", "cappelli e guanti", "Card holders", "Cardholders", 
    "Clothing", "Clutch bags", "Clutches", "Cross Body & Shoulder Bags", 
    "Crossbody and Shoulder bags", "Crossbody bags", "custom-price", "Face", 
    "Fragrances", "Glasses", "Gloves", "Hair", "Handbags", "Hats", 
    "hats and gloves > Gloves", "hats and gloves", "hats and gloves > Hats", 
    "hats and gloves > Scarves", "Hi-Tech", "Home&Living", "Lifestyle", "Make up", 
    "Man", "Man > Accessories > Belts", "Man > Accessories > Glasses", 
    "Man > Accessories > Jewellery", "Man > Accessories > Jewellery > Bracelets", 
    "Man > Accessories > Jewellery > Cufflinks", "Man > Accessories > Jewellery > Necklaces", 
    "Man > Accessories > Jewellery > Rings", "Man > Accessories > Scarves", 
    "Man > Accessories > Wallets and small leather goods", 
    "Man > Accessories > Wallets and small leather goods > Cardholders", 
    "Man > Accessories > Wallets and small leather goods > Small Leather Goods", 
    "Man > Accessories > Wallets and small leather goods > Wallets", 
    "Man > Bags > Backpacks and Duffel bags", "Man > Bags > Belt bags", 
    "Man > Bags > Crossbody bags", "Man > Bags > Pouch and Business bags", 
    "Man > Bags > Tote bags", "Man > Clothing > Jackets and Blazers", 
    "Man > Clothing > Jackets and Blazers > Blazers and Vests", 
    "Man > Clothing > Jackets and Blazers > Bomber jackets", 
    "Man > Clothing > Jackets and Blazers > Casual jackets", 
    "Man > Clothing > Jackets and Blazers > Denim jackets", 
    "Man > Clothing > Jackets and Blazers > Leather jackets", 
    "Man > Clothing > Jackets and Blazers > Lightweight and Windbreakers", 
    "Man > Clothing > Jeans > Denim shorts", "Man > Clothing > Jeans > Jeans", 
    "Man > Clothing > Jumpsuits", "Man > Clothing > Knitwear > Cardigans", 
    "Man > Clothing > Knitwear > Pullovers", "Man > Clothing > Outerwear > Coats", 
    "Man > Clothing > Outerwear > Heavy jackets", "Man > Clothing > Outerwear > Leather coats", 
    "Man > Clothing > Outerwear > Parkas", "Man > Clothing > Outerwear > Puffer jackets", 
    "Man > Clothing > Outerwear > Trench coats and Rain coats", 
    "Man > Clothing > Outerwear > Vests", "Man > Clothing > Shirts", "Man > Clothing > Suits", 
    "Man > Clothing > T-Shirts and Sweatshirts > Polo shirts", 
    "Man > Clothing > T-Shirts and Sweatshirts > Sweatshirts", 
    "Man > Clothing > T-Shirts and Sweatshirts > T-shirts", 
    "Man > Clothing > Trousers > Bermudas and Shorts", "Man > Clothing > Trousers > Joggers", 
    "Man > Clothing > Trousers > Trousers", "Man > Clothing > Underwear and Beachwear > Beachwear", 
    "Man > Clothing > Underwear and Beachwear > Socks", 
    "Man > Clothing > Underwear and Beachwear > Underwear", "Man > Shoes > Boots", 
    "Man > Shoes > Espadrilles", "Man > Shoes > Lace-ups", "Man > Shoes > Loafers", 
    "Man > Shoes > Sandals and slippers", "Man > Shoes > Sneakers", "Men", "Mini bags", 
    "Pouch and Business bags", "Scarves", "Scarves and gloves", "shoes", "Small Leather Goods", 
    "Tablewear", "Tote bags", "Travels", "Umbrellas", "unisex", 
    "Unisex > Abbigliamento unisex > Outwears > Trench coats and rain coats", 
    "Unisex > Calzature unisex > Flat scarpe basse", "Unisex > Calzature unisex > Mocassini", 
    "Unisex > Calzature unisex > Mules", "Unisex > Calzature unisex > Sneakers", 
    "Unisex > Calzature unisex > Sandali", "Unisex > Calzature unisex > Stivali e stivaletti", 
    "Unisex > Calzature unisex > Stringate", "Unisex > Shoes > Flat scarpe basse", 
    "Unisex > Shoes > Mocassini", "Unisex > Shoes > Mules", "Unisex > Shoes > Sandali", 
    "Unisex > Shoes > Sneakers", "Unisex > Shoes > Stivali e stivaletti", 
    "Unisex > Shoes > Stringate", "Unisex > Unisex accessories > Bijoux", 
    "Unisex > Unisex accessories > Minuteria/slg", "Unisex > Unisex accessories > Portafogli", 
    "Unisex > Unisex accessories > Sciarpe", "Wallets", "Wallets and small leather goods", 
    "Woman", "Woman > Accessories > Belts", "Woman > Accessories > Glasses", 
    "Woman > Accessories > Hats and hair accessories > Hair accessories", 
    "Woman > Accessories > Jewellery", "Woman > Accessories > Hats and hair accessories > Hats", 
    "Woman > Accessories > Jewellery > Bracelets", "Woman > Accessories > Jewellery > Earrings", 
    "Woman > Accessories > Jewellery > Rings", "Woman > Accessories > Jewellery > Necklaces", 
    "Woman > Accessories > Scarves and gloves > Gloves", 
    "Woman > Accessories > Scarves and gloves > Scarves", 
    "Woman > Accessories > Wallets and Small Leather Goods", 
    "Woman > Accessories > Wallets and Small Leather Goods > Small leather goods", 
    "Woman > Accessories > Wallets and Small Leather Goods > Wallets", 
    "Woman > Bags > Backpacks and Duffel bags", "Woman > Bags > Beltbags", 
    "Woman > Bags > Clutch bags", "Woman > Bags > Crossbody and Shoulder bags", 
    "Woman > Bags > Handbags", "Woman > Bags > Mini bags", "Woman > Bags > Tote bags", 
    "Woman > Clothing > Beachwear > Bikinis", "Woman > Clothing > Beachwear > Cover-ups", 
    "Woman > Clothing > Beachwear > One pieces", "Woman > Clothing > Dresses > Maxi", 
    "Woman > Clothing > Dresses > Midi", "Woman > Clothing > Jackets and Blazers > Blazers and gilets", 
    "Woman > Clothing > Jackets and Blazers > Bomber jackets", 
    "Woman > Clothing > Jackets and Blazers > Casual jackets", 
    "Woman > Clothing > Jackets and Blazers > Denim jackets", 
    "Woman > Clothing > Jackets and Blazers > Leather jackets", 
    "Woman > Clothing > Jackets and Blazers > Windbreakers", 
    "Woman > Clothing > Jeans > Jeans", "Woman > Clothing > Jeans > Shorts", 
    "Woman > Clothing > Jumpsuits", "Woman > Clothing > Knitwear > Cardigans", 
    "Woman > Clothing > Knitwear > Sweaters", "Woman > Clothing > Lingerie and nightwear > Bras", 
    "Woman > Clothing > Lingerie and nightwear > Nightwear", 
    "Woman > Clothing > Lingerie and nightwear > Slips", 
    "Woman > Clothing > Lingerie and nightwear > Socks and Collants", 
    "Woman > Clothing > Outerwear > Capes", "Woman > Clothing > Outerwear > Coats", 
    "Woman > Clothing > Outerwear > Leather coats", "Woman > Clothing > Outerwear > Parkas", 
    "Woman > Clothing > Outerwear > Pea coats", "Woman > Clothing > Outerwear > Puffer jackets", 
    "Woman > Clothing > Outerwear > Trench coats and Rain coats", 
    "Woman > Clothing > Outerwear > Vests", "Woman > Clothing > Shirts and Blouses > Blouses", 
    "Woman > Clothing > Shirts and Blouses > Shirts", "Woman > Clothing > Skirts > Maxi", 
    "Woman > Clothing > Skirts > Midi", "Woman > Clothing > Skirts > Mini", 
    "Woman > Clothing > Tops and Sweatshirts > Sweatshirts", 
    "Woman > Clothing > Tops and Sweatshirts > T-shirts and Polo shirts", 
    "Woman > Clothing > Tops and Sweatshirts > Tops", "Woman > Clothing > Trousers > Joggers", 
    "Woman > Clothing > Trousers > Leggings", "Woman > Clothing > Trousers > Shorts and Bermuda shorts", 
    "Woman > Clothing > Trousers > Trousers", "Woman > Shoes > Boots and booties", 
    "Woman > Shoes > Boots and booties > Ankle boots", 
    "Woman > Shoes > Boots and booties > Boots", "Woman > Shoes > Boots and booties > Chelsea boots", 
    "Woman > Shoes > Boots and booties > Combat boots", 
    "Woman > Shoes > Boots and booties > Winter boots", 
    "Woman > Shoes > Flats > Ballet flats", "Woman > Shoes > Flats > Espadrilles", 
    "Woman > Shoes > Flats > Flats", "Woman > Shoes > Lace-ups", "Woman > Shoes > Loafers", 
    "Woman > Shoes > Mules", "Woman > Shoes > Pumps", "Woman > Shoes > Sandals", 
    "Woman > Shoes > Sneakers", "cosmetic_case_ikonic", "ikonic"
]

vendors_ignore = ['jellycat', 'Tory burch', 'norma kamali', '3juin', 'autry', 'khrisjoy',
                  'dans les rues', '1913 dresscode', 'RUI', 'saf safu', 'MVP Wardrobe', 'si rossi']
vendors_ignore = [x.title() for x in vendors_ignore]


def round_to_5_or_0(x):
    return np.round(x / 5) * 5

def round_to_nearest_10(x):
    return np.ceil(x / 10) * 10 if (x % 10) >= 5 else np.floor(x / 10) * 10

def fix_vendors(x):
    x = x.lower()
    
    if 'moncler basic' in x:
        x = 'moncler'
    
    if 'self portrait' in x:
        x = 'Self-Portrait'
    
    if 'mm6' in x:
        return 'MM6'

    if 't shirt' in x:
        return 'T-Shirt'
    
    if 'comme de garcons' in x:
        return 'Comme Des Garçons'
    
    if 'Carhartt Wip' in x:
        return 'Carhartt WIP'
    
    if x == '"' or x == "''":
        return ''
    
    return x.title()

def fix_country(x):
    if x in ['France', 'Francia']:
        return 'France'
    if x in ['Italy', 'Italia']:
        return 'Italy'
    if x in ['China', 'Cina']:
        return 'China'
    if x in ['Germany', 'Germania']:
        return 'Germany'
    if x in ['Denmark', 'Danimarca']:
        return 'Denmark'
    if x in ['United States', 'Stati Uniti d']:
        return 'United States'
    if x in ['United Kingdom', 'Gran Bretagna']:
        return 'United Kingdom'
    if x in ['Portugal', 'Portogallo']:
        return 'Portugal'
    if x in ['Japan', 'Giappone']:
        return 'Japan'
    if x in ['Poland', 'Polonia']:
        return 'Poland'
    if x in ['Slovenia']:
        return 'Slovenia'
    if x in ['Spain', 'Spagna']:
        return 'Spain'
    if x in ['Australia']:
        return 'Australia'
    if x in ['Hungary', 'Ungheria']:
        return 'Hungary'
    if x in ['Thailand', 'Tailandia']:
        return 'Thailand'
    if x in ['Vietnam']:
        return 'Vietnam'
    if x in ['Romania']:
        return 'Romania'
    if x in ['Bosnia and Herzegovina', 'Bosnia ed Erzegovina']:
        return 'Bosnia and Herzegovina'
    if x in ['Bulgaria']:
        return 'Bulgaria'
    if x in ['Turkey', 'Turchia']:
        return 'Turkey'
    if x in ['Moldova Republic of', 'Moldova', 'Moldavia', 'Moldova@ Republic of']:
        return 'Moldova'
    if x in ['Sweden', 'Svezia']:
        return 'Sweden'
    if x in ['Macedonia']:
        return 'Macedonia'
    if x in ['Philippines', 'Filippine']:
        return 'Philippines'
    if x in ['Tunisia']:
        return 'Tunisia'
    if x in ['Korea, Republic of', 'Corea', 'Korea@ Republic of']:
        return 'South Korea'
    if x in ['Cambodia', 'Cambogia']:
        return 'Cambodia'
    if x in ['Pakistan']:
        return 'Pakistan'
    if x in ['Austria']:
        return 'Austria'
    if x in ['India']:
        return 'India'
    if x in ['Brazil', 'Brasile']:
        return 'Brazil'
    if x in ['Morocco', 'Marocco']:
        return 'Morocco'
    if x in ['Serbia']:
        return 'Serbia'
    if x in ['Ireland', 'Irlanda']:
        return 'Ireland'
    if x in ['Lithuania', 'Lituania']:
        return 'Lithuania'
    if x in ['Indonesia']:
        return 'Indonesia'
    if x in ['Madagascar']:
        return 'Madagascar'
    if x in ['Bangladesh']:
        return 'Bangladesh'
    if x in ['El Salvador']:
        return 'El Salvador'
    if x in ['Albania']:
        return 'Albania'
    if x in ['Jordan', 'Giordania']:
        return 'Jordan'
    if x in ['Mauritius']:
        return 'Mauritius'
    if x in ['Slovakia', 'Slovacchia']:
        return 'Slovakia'
    if x in ["Lao People's Democratic Republic", 'Laos']:
        return 'Laos'
    if x in ['Taiwan']:
        return 'Taiwan'
    if x in ['Myanmar']:
        return 'Myanmar'
    if x in ['Armenia']:
        return 'Armenia'
    if x in ['Hong Kong']:
        return 'Hong Kong'
    if x in ['Sri Lanka']:
        return 'Sri Lanka'
    if x in ['Guatemala']:
        return 'Guatemala'
    if x in ['Peru', 'Perù']:
        return 'Peru'
    if x in ['Kenya', 'Kenia']:
        return 'Kenya'
    if x in ['Belgium', 'Belgio']:
        return 'Belgium'
    if x in ['Switzerland', 'Svizzera']:
        return 'Switzerland'
    if x in ['Mongolia']:
        return 'Mongolia'
    if x in [0, '0']:
        return ''
    return x

def fix_heel_dim(x):
    convert_to_inches = lambda x: round(x / 25.4, 1)
    
    if isinstance(x, str) and ' / ' in x:
        x = float(x.strip(' ')[0].replace(',', '.').replace("'", '').strip())
        return f'{x} mm / {convert_to_inches(x)}"'
    
    if isinstance(x, str) and 'mm' in x:
        x = float(x.replace('mm', '').replace(',', '.').replace("'", '').strip())
        return f'{x} mm / {convert_to_inches(x)}"'
    
    if isinstance(x, str) and 'cm' in x:
        x = float(x.replace('cm', '').replace(',', '.').replace("'", '').strip())
        x *= 10
        return f'{x} mm / {convert_to_inches(x)}"'
    
    return 0


def fix_bag_dim(length, height, depth):
    if length == 0 or height == 0 or length == '0' or height == '0' or isinstance(length, int):
        return ''
    
    try:
        remove = lambda z: float(str(z).lower().replace('c', '').replace('m', '').replace(',', '.').replace('!', '').strip())
    
        length, height, depth = remove(length), remove(height), remove(depth)
    except ValueError:
        return ''
    
    cm = f'H {height} cm x L {length} x D {depth} cm'
    
    cm_to_inch = lambda z: round(z / 2.54, 1)

    length, height, depth = cm_to_inch(length), cm_to_inch(height), cm_to_inch(depth)
    
    inches = f'H {height}" x L {length}" x D {depth}"'
    
    return f'{cm} / {inches}'


def fix_bags(data):
    bags = data[data['Tags'].str.lower().str.contains('bag')][['Bag length', 'Bag height']]
    empty_bags = bags[(bags['Bag length'] == '0') & (bags['Bag height'] == '0')]
    data.loc[empty_bags.index, ['Bag length', 'Bag height']] = ''
    data['Dimensions'] = data.apply(lambda row: fix_bag_dim(row['Bag length'], row['Bag height'], row['Bag width']), axis=1)
    return data
    
def fix_file(filename):
    # read the file
    data = pd.read_csv(filename, sep=';')
    
    # rename columns
    data.rename(columns={
        'Sku Supplier': 'SKU',
        'Name': "Product's Title",
        'EAN': 'Barcode',
        'Brand': 'Vendor',
        'Categories': 'Tags',
        'Bag weight': 'Bag width',
    }, inplace=True)
    
    data.fillna(value={'Bag length': 0, 'Bag width': 0, 'Bag height': 0}, inplace=True)
    
    # fix season representation
    data['Season'] = data['Season'].apply(lambda x: x.title())
    
    # fix prices
    data['Retail Price'] = data['Retail Price'].apply(lambda x: float(str(x).replace('Eur', '').replace(',', ''.strip())))
    data['Retail Price'] *= 1.08        # convert to USD
    data['Compare to Price'] = data['Retail Price'].apply(lambda x: round_to_nearest_10(x))
    data['Retail Price'] = data['Retail Price'] * 1.25
    data['Retail Price'] = data['Retail Price'].apply(lambda x: round_to_5_or_0(x))
    
    # fix sizes
    size = data[data['Size Info'].str.lower().isin(['standard'])]
    data.loc[size.index, 'Size Info'] = '-'
    
    # remove other years
    data = data[~data['Year'].isin(['2021', '2022', '2023'])]
    
    # select correct categories
    data = data[data['Tags'].isin(categories)]
    
    # fix vendors
    data["Product's Title"] = data["Product's Title"].str.title()
    data['Vendor'] = data['Vendor'].apply(lambda x: fix_vendors(x).upper())
    data = data[~data['Vendor'].isin(vendors_ignore)]
    
    # fix countries
    data['Made in'] = data['Made in'].apply(lambda x: fix_country(x))
    
    data = fix_bags(data)
    
    # fix heels
    data['Heel height'].fillna(0, inplace=True)
    data['Heel height'] = data['Heel height'].apply(lambda x: fix_heel_dim(x))
    
    data.drop(columns=['Nome ITA', 'Descrizione ITA', 'Star', 'Insole length', 'Color Styleisnow ITA', 'FTA'], inplace=True)
    
    data.to_csv('all_products.csv')
    return data
    
    # bags = data[data["Product's Title"].str.contains('Bag')]
    # bags.drop(columns=['Accessory length', 'Accessory height', 'Accessory weight', 'Heel height', 'Plateau height',], inplace=True)
    # bags['SKU FULL'] = bags['Sku Styleisnow'] + '-' + 'os'
    
    # bags.to_csv('bags.csv', index=False)
    
    # others = data[~data["Product's Title"].str.contains('Bag')]
    # others.drop(columns=['Bag length', 'Bag height', 'Bag width', 'Dimensions'], inplace=True)
    
    # others.to_csv('other_products.csv', index=False)
    # return bags, others