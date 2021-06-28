import xml.etree.ElementTree as ET
import os
import glob
from typing import List
from ebay_item import EbayItem
from tqdm import tqdm
from plot_images import plot_images
from pprint import pprint

def get_description_for_path(path:str) -> str:
    result = ""
    with open(path,mode='r',encoding='UTF-8') as f:
        result = '\n'.join(f.readlines())
    return result



DATASET_FOLDER = [os.path.join('eBay-Daten','Ebay_2019_09_03_bis_2019_11_30'),
                  os.path.join('eBay-Daten','Ebay_2019_12_01_bis_2020_02_14')]
ITEM_DESCRIPTION_FOLDER = [os.path.join(x,'ItemDescriptions') for x in DATASET_FOLDER]
ITEM_IMAGES_FOLDER = [os.path.join(x,'ItemPictures') for x in DATASET_FOLDER]

ebay_items = []

namespace={'xmlns': 'http://www.ebay.com/marketplace/search/v1/services'}
for i,folder in tqdm(enumerate(DATASET_FOLDER),position=2):
    for xml_file in tqdm(glob.glob(os.path.join(folder,'*.xml')),position=1):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        items = root.find('xmlns:searchResult',namespaces=namespace)
        for item in tqdm(items,position=0):
            item_id = item.find('xmlns:itemId',namespaces=namespace).text
            title = item.find('xmlns:title',namespaces=namespace).text

            primary_category = item.find('xmlns:primaryCategory',namespaces=namespace)
            category_id = primary_category.find('xmlns:categoryId',namespaces=namespace).text
            category_name = primary_category.find('xmlns:categoryName',namespaces=namespace).text

            seller = item.find('xmlns:sellerInfo',namespaces=namespace)
            seller_feedback_score = seller.find('xmlns:feedbackScore',namespaces=namespace).text
            seller_positive_feedback_percent = seller.find('xmlns:positiveFeedbackPercent',namespaces=namespace).text


            selling_status = item.find('xmlns:sellingStatus',namespaces=namespace)
            selling_price = selling_status.find('xmlns:currentPrice',namespaces=namespace).text
            bid_count = selling_status.find('xmlns:bidCount',namespaces=namespace).text if selling_status.find('xmlns:bidCount',namespaces=namespace) is not None else 0
            selling_state = selling_status.find('xmlns:sellingState',namespaces=namespace).text

            item_details = {}
            item_specifics = item.find('xmlns:ItemSpecifics',namespaces=namespace)
            for item_specific in item_specifics.findall('xmlns:NameValueList',namespaces=namespace):
                name = item_specific.find('xmlns:Name',namespaces=namespace).text
                value = item_specific.find('xmlns:Value',namespaces=namespace).text
                item_details[name] = value
            
            item_description_path = os.path.join(ITEM_DESCRIPTION_FOLDER[i],f'{item_id}.txt')
            item_description = get_description_for_path(path = item_description_path)

            item_images_paths = glob.glob(os.path.join(ITEM_IMAGES_FOLDER[i],f'{item_id}*.jpg'))
            item_images_paths.extend(glob.glob(os.path.join(ITEM_IMAGES_FOLDER[i],f'{item_id}*.png')))
            

            ebay_items.append(EbayItem(item_id,title,category_id,category_name,
                                       selling_price,bid_count,item_details,item_description,
                                       item_images_paths,seller_feedback_score,
                                       seller_positive_feedback_percent))
            
print()

