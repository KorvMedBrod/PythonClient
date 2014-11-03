from riak import RiakClient

client = RiakClient(protocol='pbc', host='127.0.0.1', http_port=8098)
xml_file = open('tweetsSchema.xml', 'r')
schema_data = xml_file.read()
print(schema_data)
client.create_search_schema('tweetsSchema', schema_data)
xml_file.close()
client.create_search_index("default", "tweetsSchema")
print(client.list_search_indexes())
