import random
import math

words = [e.strip() for e in open("common_words")]

def correct_horse_battery_staple(word_size_bound,number_of_words):
    W = [e for e in words if len(e) < word_size_bound]
    P = ' '.join([random.choice(W) for i in range(number_of_words)])
    scr = math.log(len(W),2) * number_of_words
    return P,scr

def password_gen(size,alpha='1234567890!@#$%^&*()abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    P = ''.join([random.choice(alpha) for i in range(size)])
    scr = math.log(len(P),2) * size
    return P,scr

