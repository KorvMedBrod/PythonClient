from riak import RiakClient, RiakNode

client = RiakClient(protocol='pbc', host='127.0.0.1', http_port=8098)
print(client.ping())
tweetBucket = client.bucket("tweets")
print(tweetBucket.get_properties())
print(client.get_buckets())
print(client.bucket_type("tweets"))
allKeysInTweets = client.get_keys(tweetBucket)
print("Number of keys... ",len(allKeysInTweets))


stream = client.stream_keys("tweets")
for key_list in stream:
     print("key_list;" , key_list)
stream.close()
