#!/usr/bin/python3
import sys
def read_map_output(file):
    for line in file:
        yield line.strip().split("\t")
def cate_reducer():
    current_category = ""
    category_list = []  # this is a list
    #for category, video_id, country in read_map_output(sys.stdin):
    for category, videoID, countryID in read_map_output(sys.stdin):

        if videoID == "video_id": # ignore the first sheet head
            continue
        #if current category is not the previews one, means the last category have finished outputting
        #we could deal with the preview category records with writtened categ
        if category != current_category:
            if current_category != "":  #check if the category is blank
                category_list = list(set([tuple(t) for t in category_list]))
                category_list = [list(v) for v in category_list]    #put all tuple records in category_list into a  set to filte the duplicated ones
                numCountry = len(category_list) #that we get the number of countrys
                list1 =[]
                for item in category_list:  #get the country record into another list
                    video =item[0]
                    list1.append(video)
                list2 = []
                for id in list1:    #filte the the duplicated ones
                    if id not in list2:
                        list2.append(id)
                numVideo = len(list2)   #that we get the number of countrys
                average =str(("%.2f" %(numCountry/numVideo)))   #count the average country number of this category
                print("{}\t{}".format(current_category, average).strip())   #format the output
            category_list = []  #clear the category list for next category
            current_category =category  #clear the category name for next category
        category_list.append([videoID,countryID])   #append  new category records into the category list
    lastprint(current_category,category_list)   #above lines can only handle all the categorys except the last category because no category is following the last one
#we should printout the last category besides the for loop
def lastprint(current_category,category_list):  #do all the same things as  above
    current_category = current_category
    category_list = category_list
    if current_category != "":
                category_list = list(set([tuple(t) for t in category_list]))
                category_list = [list(v) for v in category_list]
                numCountry = len(category_list)
                list1 =[]
                for item in category_list:
                    video =item[0]
                    list1.append(video)
                list2 = []
                for id in list1:
                    if id not in list2:
                        list2.append(id)
                numVideo = len(list2)
                average =str(("%.2f" %(numCountry/numVideo)))
                print("{}\t{}".format(current_category, average).strip())

if __name__ == "__main__":  #cate_reducer can be called 
    cate_reducer()

