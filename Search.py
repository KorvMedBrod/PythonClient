from riak import RiakClient
import riak


client = RiakClient(protocol='pbc', host='127.0.0.1', http_port=8098)
tweetsBucket = client.bucket('tweets')
tweetsBucket.get("*")

#results = client.fulltext_search("tweets", "525322516722892802:*")
#print("Output; ",results)
