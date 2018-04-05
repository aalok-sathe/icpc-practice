# Aalok Sathe
#! /bin/env/ python3

import sys

def read_from(stream, current_index_list)
    current_index_list.insert(0,current_index_list[0]+1)
    return stream[current_index_list[1]]

lines = sys.stdin.readlines()

for line_index in range(len(lines)):
    lines[line_index] = lines[line_index][:-1]
    
current_index_list = [0,]
for test_case in list(range(int(lines[current_index_list[0]]))):
    
    current_index_list[0] += 1
    
    G = int(read_from(lines, current_index_list))
    
    good_words = set()
    for i in range(G):
        good_words.add(str(read_from(lines, current_index_list)))

    B = int(read_from(lines, current_index_list))
        
    bad_words = set()
    for i in range(B):
        bad_words.add(str(read_from(lines, current_index_list)))
    
    cipher_text = str(read_from(lines, current_index_list))
    
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = "abcdefghijklmnopqrstuvwxyz"
        
    for shift in range(25):
        deciphered = ""
        for char in cipher_text:
            deciphered += cipher_text[(cipher_text.index(char)+shift) % len(cipher_text)]
        match = 0
        threat = 0
        nonmatch = 0
        for word in deciphered.split():
            if (word in good_words) or (word in bad_words):
                if 
                match += 1
            else
                nonmatch += 1
            
            
            
