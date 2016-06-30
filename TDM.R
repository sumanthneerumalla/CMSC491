library("twitteR")
library("tm")
library("wordcloud")
library("plyr")

api_key <- "LipYGLsynELHg8kGXJw9M68h9"
api_secret <- "dM0NW7VAj2t4EHGpOzTKfkpcFSDMaC42IVdZGIT47eLFyMctjs"
token <- "945794155-6VFpCWRBZPUFh4IyjGIlejiNiDN4YVmscbLcWE9m"
tokenSecret <- "qbtGWl0rKMs76tRr6iZb53uQQOuVSKDDHvxDM95QH76WV"

setup_twitter_oauth(api_key,api_secret,token,tokenSecret)

Colatweets <- searchTwitter("Coca Cola",n=25,lang='en)
Pepsitweets <- searchTwitter("Pepsi Cola",n=25, lang='en')

tweets_txt <- ldply(Colatweets,statusText)
tweets_vect = tweets_txt$V1

tweets_corpus <- Corpus(VectorSource(tweets_vect))
tweets_corpus <- tm_map(tweets_corpus,tolower)
tweets_corpus <- tm_map(tweets_corpus,removePunctuation)
tweets_corpus <- tm_map(tweets_corpus, function(x,removeWords(x,stopwords()))

tweets_corpus <- tm_map(tweets_corpus,PlainTextDocument)

par(ask=TRUE)

wordcloud(tweets_corpus)

tweets_tdm <- TermDocumentMatrix(tweets_corpus,control = list(removePunctuation = TRUE, stopwords = TRUE))

findFreqTerms(tweets_tdm,lowfreq=10)

findAssoc(tweets_tdm,'cloud',.49)

tweets2_tdm <- removeSparseTerms(tweets_tdm,sparse=0.90)
tweets2_tdm <-as.matrix(tweets2_tdm)
tweets2_dist <-dist(tweets2_tdm,method="euclidean")
