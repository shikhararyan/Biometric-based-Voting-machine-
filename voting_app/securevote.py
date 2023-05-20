# from secugen import getFP
from matcher import matchFP

flag = True
countA = 0
countB = 0
while flag:
    aadhar = input()
    print('get the fingerprint')
    # getFP(aadhar,'secure_vote')
    score = matchFP(aadhar,'secure_vote')
    if score > 6:
        print('select the party for you want to vote\n')
        print('1-partyA\n')
        print('2-partyB\n')
        c = int(input("select the party: "))
        if c == 1:
            countA += 1
        else:
            countB += 1
    c = input("Do you want to continue y/n:")
    if c == 'n':
        flag = False

if countA > countB:
    print('partyA won.')
else:
    print('PartyB won.')
    


    