from riak import RiakClient
import riak


client = RiakClient(protocol='pbc', host='127.0.0.1', http_port=8098)
tweetsBucket = client.bucket('tweets')
print(client.fulltext_search(tweetsBucket,"*:*"))
#print(tweetsBucket.get("525322516722892802").encoded_data)
