#!/usr/bin/python3

import sys


def cate_mapper():
    """ 
    The input file format is 
    video_id,trending_date,category_id,category,publish_time,views,likes,dislikes,comment_count,ratings_disabled,video_error_or_removed,country
    divided by ','
    """
    for line in sys.stdin:
        # Clean input and split it
        parts = line.strip().split(",")

        # Check that the line is of the correct format
        # If line is malformed, we ignore the line and continue to the next line
        if len(parts) != 12:
          continue
        #Get useful things out
        category = parts[3].strip()
        videoID= parts[0].strip().split()
        country = parts[11].strip().split()

       #Format the output
        print("{}\t{}\t{}".format(category, videoID,country))
#Define the cate_mapper can be called
if __name__ == "__main__":
    cate_mapper()
