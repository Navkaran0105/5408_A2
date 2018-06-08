from elasticsearch_dsl import DocType, Float, Integer, Keyword, Text, connections
import csv
connections.create_connection(hosts=['ec2-18-220-95-159.us-east-2.compute.amazonaws.com:9200'])

def type_cast(sscore):
        try:
                new_ss = float(sscore)
                return new_ss
        except ValueError:
                return float(0)


class upload(DocType):
        tweet = Text()
        sentiment = Keyword()
        sentiment_score= Float()

        class Meta:
                index = 'sentiments'


upload.init(index='sentiments')

with open('analysis.csv','r') as result:
        f = csv.reader(result)
        count = 0
        for row in f:
                var =  upload(meta = {'id':count})
                var.tweet = row[0]
                var.sentiment = row[1]
                var.sentiment_score = type_cast( row[2])
                var.save()
                var = upload.get(id = count)
                count = count + 1
                print(row)

