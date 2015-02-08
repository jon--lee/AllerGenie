# @param    reviews        list of string reviews to process
# @param    keywords        list of keywords to search for in each review
# @return   processedList      list of processed strings that contain the keywords
def process(reviews, keywords):
    print "PROCESSING EVERYTHING"
    phrases = []
    for review in reviews:
        for keyword in keywords:
            endIndex = 0
            i = review.find(keyword, endIndex)
            while(i > -1):
                i = review.find(keyword, endIndex)
                if not i < 0:
                    #find end index
                    endIndex = review.find(".", i + len(keyword))
                    temp = review.find("!", i + len(keyword) + 1)
                    if(endIndex > temp and temp > -1):
                        endIndex = temp
                    temp = review.find("?", i + len(keyword) + 1)
                    if(endIndex > temp and temp > -1):
                        endIndex = temp
                    
                    if(endIndex < 0):
                        endIndex = len(review) - 1;
                
                
                
                
                    #find start index
                    j = i
                
                    while(j > -1) and not (review[j] == "." or review[j] == "!" or review[j] == "?"):
                        j = j - 1
                
                    if(j < 0):
                        j = 0
                    else:
                        j += 2
                    startIndex = j

                    if(i - startIndex > 120):
                        startIndex = i - 120
                    #print "start: " + str(startIndex)
                    if (endIndex - i > 120):
                        endIndex = i + 120
                    #print "end: " + str(endIndex);

                    phrases.append(("..." + review[startIndex:endIndex] + "...").decode('utf-8'))
    return phrases
