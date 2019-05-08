from pyspark import SparkContext
from ml_utils import *
import argparse
#test
#test1

if __name__ == "__main__":
    sc = SparkContext(appName="Top10Disklike")  #define the app name 
    parser = argparse.ArgumentParser()  #define the things in command lines
    parser.add_argument("--input", help="the input path")
    parser.add_argument("--output", help="the output path")
    args = parser.parse_args()
    input_path = args.input
    output_path = args.output

    Original = sc.textFile("AllVideos_short.csv")   #define the input file 
    filtedInfo = Original.map(filteringnDate).sortByKey()     #filter the useful things out 
    integrated = filtedInfo.map(countnDeleteDate)   #do some count insides the record
    records = integrated.groupByKey().map(lambda x : (x[0], list(x[1])))    #get the Keys togethere
    result = records.map(countTwo).filter(lambda x : isinstance(x, tuple))  #get first two days out and do some counting
    result= result.map(changeKey).sortByKey(0).top(10)  #sort the records by the value of dislike growth
    sc.parallelize(result).map(formatTrans).saveAsTextFile(output_path) #trans the format into required format
    
