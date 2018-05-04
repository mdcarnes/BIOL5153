#! usr/bin/env python3

#This script will compile lifetime rattle profiles of long term snakes and spit out their ID and a list of segment values, newest to oldest

#load required modules
import sys
import os
import re
import argparse


def get_args():
    #create an ArgumentParser object ('parser')
    parser = argparse.ArgumentParser()

    #add required arguments
    parser.add_argunent("txt", help="name of the txt, tab delimited, data file")

    #parse the arguments
    return parser.parse_args()



def parse_file():
    #open the txt file
    complete = open(args.txt, 'r')

    print(complete)




def build_lists():





def main():
    parse_file(complete)

main()
