import yaml
import xml.etree.ElementTree as xml_tree

#Open and read the YAML file
with open('feed.yaml', 'r') as file:
 yaml_data = yaml.safe_load(file)

#Create the RSS element
rss_element = xml_tree.Element('rss', version='2.0', xmlns_itunes='http://www.itunes.com/dtds/podcast-1.0.dtd')

#Create the channel element
channel_element = xml_tree.SubElement(rss_element, 'channel')

#Add various elements to the channel
elements = {
'title': yaml_data['title'],
'link': yaml_data['link'],
'description': yaml_data['description'],
'language': yaml_data['language'],
'itunes:author': yaml_data['author'],
'itunes:image': yaml_data['image']
}

for tag, text in elements.items():
 element = xml_tree.SubElement(channel_element, tag)
 element.text = text

#Add items (episodes) to the channel
for item in yaml_data['item']:
 item_element = xml_tree.SubElement(channel_element, 'item')
 title_element = xml_tree.SubElement(item_element, 'title')
 title_element.text = item['title']
 author_element = xml_tree.SubElement(item_element, 'itunes:author')
 author_element.text = yaml_data['author']
 description_element = xml_tree.SubElement(item_element, 'description')
 description_element.text = item['description']
 duration_element = xml_tree.SubElement(item_element, 'itunes:duration')
 duration_element.text = item['duration']
 pub_date_element = xml_tree.SubElement(item_element, 'pubDate')
 pub_date_element.text = item['published']
 enclosure_element = xml_tree.SubElement(item_element, 'enclosure', url=yaml_data['link'] + item['file'], type='audio/mpeg', length=item['length'])

#Create the output tree and write to XML file
output_tree = xml_tree.ElementTree(rss_element)
output_tree.write('podcast.xml', encoding='UTF-8', xml_declaration=True)