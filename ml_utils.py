import csv

"""
This module includes a few functions used in computing top10 dislike growing 
"""


def filteringnDate(record):  #filting the useful things out
    try:
        columns = record.split(",")
        videoID = columns[0].strip()
        trendDate = columns[1].strip()
        category = columns[3].strip()
        like = columns[6].strip()
        dislike = columns[7].strip()
        country = columns[11].strip()

        return (trendDate,[videoID,category,like,dislike,country])
    except:
        return ('',[''])

def countnDeleteDate(a):
        lists=list(a)
        try:
                gap = int(lists[1][3]) - int(lists[1][2])
                key = str(lists[1][0]+','+lists[1][4])
                value = [lists[1],gap]
                return(key,value)
        except:
                return ('',[''])

def countTwo(a):    # count the grade of first two days, that is the outcome
    if len(a[1])>=2:
        video_ID_country=a[0]
        category=a[1][0][0]
        grade=int(a[1][1][1])-int(a[1][0][1])
        return(video_ID_country, [category,grade])


def changeKey(a):   #gey the grade to the  first place for sorting 
    videoID=a[0]
    category=a[1][0]
    grade=a[1][1]

    key = grade
    value = [category,videoID]
    return (key, value)

def formatTrans(a): #change the format into what we what we want
    a = list(a)
    a[1][0],a[1][1]= a[1][1],a[1][0]
    a[0],a[1]=a[1],a[0]
    id_country=a[0][0]
    cate = a[0][1].strip('u')
    grade = a[1]
    return (id_country,cate,grade)