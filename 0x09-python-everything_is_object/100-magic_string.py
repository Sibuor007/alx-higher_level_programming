#!/usr/bin/python3
def magic_string(freq_=[0]):
    freq_[0] = freq_[0] + 1
    return "BestSchool" + (", BestSchool" * (freq_[0] - 1))
