from itertools import combinations,  permutations
import pyautogui,time,sys

import botworkon

try:
    wait,vocab = float(sys.argv[1]),sys.argv[2]
except:
    wait,vocab = 0.15, "kelime-listesi.txt"


five = [(1592, 645), (1673, 703), (1642, 804), (1543, 802), (1509, 703)]
six = [(1597, 642), (1661, 688), (1665, 772), (1594, 817), (1518, 778), (1513, 689)]


kelimeler = []
with open(vocab) as file:
    for line in file:
        if " " in line:
            splited = line.split()
            for i in splited:
                kelimeler.append(i.replace("â","a").replace("-",""))
        else:
            kelimeler.append(line.strip("\n").strip().replace("â","a").replace("-",""))

def return_substrings(x):
    all_combnations = []
    all_perm = []

    for i in range(1,len(chars)+1):
        all_combnations += list(set(["".join(l) for l in combinations(chars,i)]))
    for i in all_combnations:
        c_char = [k for k in i]
        all_perm += list(set( ["".join(l) for l in permutations(c_char) ]))
    return sorted(list(set(all_perm)), key=len)

def move_for(valid_kelime,len):
    if len == 5:
        path = []
        for harf in valid_kelime:
            fivecop = five[:]
            charscop = chars[:]
            if fivecop[chars.index(harf)] in path:
                fivecop.pop(chars.index(harf))
                charscop.remove(harf)
            path += [fivecop[charscop.index(harf)]]
    elif len == 6:
        path = []
        for harf in valid_kelime:
            sixcop = six[:]
            charscop = chars[:]
            if sixcop[chars.index(harf)] in path:
                sixcop.pop(chars.index(harf))
                charscop.remove(harf)
            path += [sixcop[charscop.index(harf)]]


    pyautogui.moveTo(path[0])
    pyautogui.mouseDown()
    for i in path[1:]:
        time.sleep(wait)
        pyautogui.moveTo(i)
    time.sleep(wait)
    pyautogui.mouseUp()
    time.sleep(0.1)


while True:
    x=input("\nEnter characters:  ")
    chars = [i for i in x]
    level_len = len(chars)
    for random in return_substrings(x):
        if random in kelimeler and len(random) > 2:
            move_for(random,level_len)
            sys.stdout.flush()
            print(random)
