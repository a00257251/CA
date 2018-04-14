import tweepy
from db import Conn



ConsumerKey = "JuNMP4UrBrmcBo6grX4UY1zm1"
ConsumerSecret = "KJZWQiSJ2oWEzVT725f5Mpo8HeamxE36FOg92bbPFXmBSOhDsC"
AccessToken = "2946770101-qJUUWwWR4BkNtxwbUUfZfBUQXuyO0w1CutpbGCb"
AccessTokenSecret = "JNnzdWuFVRnB82CB9dGbleyxTDJcSbISN8qQWSXBJ3Pco"



auth = tweepy.OAuthHandler(ConsumerKey, ConsumerSecret)
auth.set_access_token(AccessToken, AccessTokenSecret)
#print tweet.entities.get('hashtags')
api = tweepy.API(auth)


def tweetSearch(Search):
    sea = api.search(q=Search ,language = "en" ,rpp=100)
    print sea
    for tweet in sea:
        print "Name:", tweet.author.name.encode('utf8')
        print "Screen-name:", tweet.author.screen_name.encode('utf8')
        print "Tweet created:", tweet.created_at
        print "Tweet:", tweet.text.encode('utf8')
        print "Retweeted:", tweet.retweeted
        print "Favourited:", tweet.favorited
        print "Location:", tweet.user.location.encode('utf8')
        print "Time-zone:", tweet.user.time_zone
        print "Geo:", tweet.geo
        print "hash:", tweet.entities.get('hashtages')
        print "//////////////////"

        language = tweet.lang
        if (language == 'en'):

            print  'tweet.text                             ' ,   tweet.text
            print  'tweet.created_at                       ' ,   tweet.created_at
            print  'tweet.geo                              ' ,   tweet.geo
            print  'language                               ' ,   language
            print  'tweet.place                            ' ,   tweet.place
            print  'tweet.coordinates                      ' ,   tweet.coordinates
            print  'tweet.user.favourites_count            ' ,   tweet.user.favourites_count
            print  'tweet.user.statuses_count              ' ,   tweet.user.statuses_count
            print  'tweet.user.description                 ' ,   tweet.user.description
            print  'tweet.user.location                    ' ,   tweet.user.location
            print  'tweet.user.id                          ' ,   tweet.user.id
            print  'tweet.user.created_at                  ' ,   tweet.user.created_at
            print  'tweet.user.verified                    ' ,   tweet.user.verified
            print  'tweet.user.following                   ' ,   tweet.user.following
            print  'tweet.user.url                         ' ,   tweet.user.url
            print  'tweet.user.listed_count                ' ,   tweet.user.listed_count
            print  'tweet.user.followers_count             ' ,   tweet.user.followers_count
            print  'tweet.user.default_profile_image       ' ,   tweet.user.default_profile_image
            print  'tweet.user.utc_offset                  ' ,   tweet.user.utc_offset
            print  'tweet.user.friends_count               ' ,   tweet.user.friends_count
            print  'tweet.user.default_profile             ' ,   tweet.user.default_profile
            print  'tweet.user.name                        ' ,   tweet.user.name
            print  'tweet.user.lang                        ' ,   tweet.user.lang
            print  'tweet.user.screen_name                 ' ,   tweet.user.screen_name
            print  'tweet.user.geo_enabled                 ' ,   tweet.user.geo_enabled
            print  'tweet.user.profile_background_color    ' ,   tweet.user.profile_background_color
            print  'tweet.user.profile_image_url           ' ,   tweet.user.profile_image_url
            print  'tweet.user.time_zone                   ' ,   tweet.user.time_zone
            print  'tweet.id                               ' ,   tweet.id
            print  'tweet.favorite_count                   ' ,   tweet.favorite_count
            print  'tweet.retweeted                        ' ,   tweet.retweeted
            print  'tweet.source                           ' ,   tweet.source
            print  'tweet.favorited                        ' ,   tweet.favorited
            print '//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'
            sql(tweet.user.name.encode('unicode-escape')  ,tweet.user.screen_name.encode('unicode-escape')  ,tweet.text.encode('unicode-escape'),tweet.user.profile_image_url,tweet.created_at,tweet.user.url,Search)








def sql(username,userScreenName,tweet,photo,TweetTime,url,topic):
    cursor, cnx =Conn()
    query = """INSERT INTO tweets (
         username   ,
         userScreenName   ,
         tweet   ,
         userPhoto  ,
         TweetTime  ,
         url  ,
         topicName
        )  
        VALUES(%s, %s, %s, %s, %s, %s,%s);"""
    data = (username   ,
            str(userScreenName)   ,
            tweet  ,
            photo  ,
            str(TweetTime)  ,      
            url  ,
            str(topic)
            )
    cursor.execute(query, data)
    cnx.commit()







def selectTweets(Search):
    cursor, cnx =Conn()
    print(str(Search))
    cursor.execute("select username,tweet,userPhoto,TweetTime,url  from tweets WHERE topicName='" + str(Search)+ "' ;")
   # cursor.callproc('Search', (Search))
    comments = cursor.fetchall()
    print(comments)
    comL = []
    for item in comments:
        i = {
            'username': item[0],
            'tweet': item[1],
            'userPhoto': item[2],
            'TweetTime': item[3],
            'url': item[4]
        }
        comL.append(i)
    print(comL)
    return comL



#i = 'Arsenal'
#tweetSearch(i)
#o = selectTweets(i)
#print(o)
































#print '------------------------------------------------------------------------------'
#
#
## print s.author.name.encode('utf8')
#    #print s.author.screen_name.encode('utf8')
#    #print s.textt.encode('utf8')
#    #print '---------------authet-------------'
#    #print s._json
#    #print s.author
#p = api.user_timeline('BBCSport')
#print(p)
#for t in p:
#    print(t.text)
#    print      t.text
#    print      t.created_at
#    print      t.geo
#   # print       language
#    print      t.place
#    print      t.coordinates
#    print      t.user.favourites_count
#    print      t.user.statuses_count
#    print      t.user.description
#    print      t.user.location
#    print      t.user.id
#    print      t.user.created_at
#    print      t.user.verified
#    print      t.user.following
#    print      t.user.url
#    print      t.user.listed_count
#    print      t.user.followers_count
#    print      t.user.default_profile_image
#    print      t.user.utc_offset
#    print      t.user.friends_count
#    print      t.user.default_profile
#    print      t.user.name
#    print      t.user.lang
#    print      t.user.screen_name
#    print      t.user.geo_enabled
#    print      t.user.profile_background_color
#    print      t.user.profile_image_url
#    print      t.user.time_zone
#    print      t.id
#    print      t.favorite_count
#    print      t.retweeted
#    print      t.source
#    print      t.favorited
#
#
#
#
#
#
#public_tweets = api.home_timeline()
#for tweet in public_tweets:
#    print tweet.text
#
#user = api.get_user('BBCSport')
#
#print user.screen_name
#print user.followers_count
#for friend in user.friends():
#   print friend.screen_name
#