#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 19:00:26 2020

@author: jkenglish
"""



import random
import time


class CodeTracker:
    def __init__(self):
        self.nums = []

    def time_tracker(sort_func):
        """ Higher order function to track code execution times """
        """ used as a decorator """
        def exec_code(self, *args):
            """ function that excutes a function passed to the time_tracker """

            #capture the start and end times to get elapsed time
            start_time = time.time()
            sorted_list = sort_func(self, *args)            
            end_time = time.time()            
            elap_time = end_time - start_time
            return elap_time, sorted_list
        return exec_code


    @time_tracker
    def selSortNums(self, nums):
        """ Uses Selction Sort to sort the list """
        self.nums = nums
        for num_loc in range(len(self.nums)-1,0,-1):
            max_num_loc = 0
            # find max number location in remaining nums
            for next_num_loc in range(1,num_loc+1):
                if self.nums[next_num_loc] > self.nums[max_num_loc]:
                    max_num_loc = next_num_loc

            #Swap the number with the number at max_num_loc
            self.nums[num_loc], self.nums[max_num_loc] = self.nums[max_num_loc], self.nums[num_loc]

        return (self.nums)

    @time_tracker
    def bubSortNums(self, nums):
        """ Uses Bubble Sort to sort the list """
        # Start at the last number in the list
        for number in range(len(self.nums), 1, -1):
            for next_num in range(number-1):
                if self.nums[next_num] > self.nums[next_num+1]:
                    #Swap the number with the number at next_num
                    self.nums[next_num],self.num[next_num+1] = self.nums[next_num+1],self.nums[next_num]

        return (self.nums)


# Following methods are outside the CodeTracker Class

def genRandNums():
    """ Generate a list of Random Numbers """
    sort_size = int(input("Enter the size of the list to be sorted: "))

    # Create a list of random numbers for Selection sort use
    ssort_list = random.sample(range(sort_size), sort_size)

    # Create an identical copy of ssort_list to be used for Bubble Sort
    bsort_list = ssort_list[:]

    return ssort_list, bsort_list


def printResults(elap_time, sorted_list, sort_type):
    print(f"\n\nSorted {sort_type} List: \n\n {sorted_list}\n")
    print(f"{sort_type} Elapsed Time = {elap_time}\n")



def chkSortEff(ssort_elap_time, bsort_elap_time):
    """ Compare the elapsed times of the two Sort methods """
    if ssort_elap_time < bsort_elap_time:
        print(f"Selection Sort's Elapsed Time of {ssort_elap_time} < Bubble Sort's Elapsed time of {bsort_elap_time}")
        print("Selection Sort is more efficient than Bubble Sort")
    elif bsort_elap_time < ssort_elap_time:
        print(f"Bubble Sort's Elapsed Time of {bsort_elap_time} < Selection Sort's Elapsed time of {ssort_elap_time}")
        print("Bubble Sort is more efficient than Selection Sort")

    elif ssort_elap_time == bsort_elap_time:
        print("Selection Sort and Bubble sort have same Elapsed times.")


def main():

   print("\n\nWelcome to the Code Execution Tracker\n\n")
   ssort_list, bsort_list = genRandNums()

   my_tracker = CodeTracker()

   ssort_elap_time, sorted_ssort_list = my_tracker.selSortNums(ssort_list)

   printResults(ssort_elap_time, sorted_ssort_list, 'Selection Sort')

   bsort_elap_time, sorted_bsort_list = my_tracker.bubSortNums(bsort_list)

   printResults(bsort_elap_time, sorted_bsort_list, 'Bubble Sort')

   chkSortEff(ssort_elap_time, bsort_elap_time)


main()
