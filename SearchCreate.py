from riak import RiakClient


client = RiakClient(protocol='pbc', host='127.0.0.1', http_port=8098)
client.create_search_index("tweets")
