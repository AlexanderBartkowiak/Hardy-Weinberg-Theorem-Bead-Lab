import random

print("___________________Hardy-Weinberg Theorem Bead Lab___________________")
input0 = input("random or selected[r/s]: ")
if input0 == "r":
    type = True
if input0 == "s":
    type = False
input1 = input("Black Beads: ")
input2 = input("White Beads: ")
input3 = input("Generations: ")


if type == True:
    startblack = int(input1)
    startwhite = int(input2)
    generationnum = int(input3)
    gencounter = 0
    for gencounter in range (generationnum):

        #create black
        black = []
        for x in range (int(startblack)):
            black.append(1)

        #create white
        white = []
        for x in range (int(startwhite)):
            white.append(0)

        #mix them
        mixlist = white + black

        #create a random sample
        values = random.sample(mixlist,40)

        #create final genome values and count
        final = []
        blackfinal = 0
        whitefinal = 0
        mixedfinal = 0
        counter = 0
        for x in range(20):
            final.append(values[counter] + values[counter+1])
            if final[x] == 2:
                blackfinal += 1
            if final[x] == 1:
                mixedfinal += 1
            if final[x] == 0:
                whitefinal += 1
            counter = counter + 2

        #calculate the p and q value
        p = ((blackfinal + (.5 * mixedfinal)) / 20)
        q = 1 - p

        #reset start values
        startblack = p * 100
        startwhite = q * 100

        #print results
        print('Generation:' + str(gencounter+1) + ' black: ' + str(blackfinal) + ' mixed: ' + str(mixedfinal) + ' white: ' + str(whitefinal) + ' p: ' + str(p) + ' q: ' + str(q))

#___________________________________________________________________________________________________________________________________________________________________________________

else:
    startblack = int(input1)
    startwhite = int(input2)
    generationnum = int(input3)
    gencounter = 0

    for gencounter in range (generationnum):

        #create black
        black = []
        for x in range (int(startblack)):
            black.append(1)

        #create white
        white = []
        for x in range (int(startwhite)):
            white.append(0)

        #mix them
        mixlist = white + black

        #create a random sample
        values = random.sample(mixlist,40)

        #create final genome values and count
        final = []
        blackfinal = 0
        whitefinal = 0
        mixedfinal = 0
        counter = 0
        for x in range(20):
            final.append(values[counter] + values[counter+1])
            if final[x] == 2:
                blackfinal += 1
            if final[x] == 1:
                mixedfinal += 1
            if final[x] == 0:
                whitefinal += 1
            counter = counter + 2

        #calculate the p and q value
        p = ((blackfinal + (.5 * mixedfinal)) / (blackfinal + mixedfinal + whitefinal))
        q = ((whitefinal + (.5 * mixedfinal)) / (blackfinal + mixedfinal + whitefinal))
        pv = ((blackfinal + (.5 * mixedfinal)) / (blackfinal + mixedfinal))
        qv = (((.5 * mixedfinal)) / (blackfinal + mixedfinal))


        #reset start values
        startblack = pv * 100
        startwhite = qv * 100

        #print results
        print('Generation:' + str(gencounter+1) + ' black: ' + str(blackfinal) + ' mixed: ' + str(mixedfinal) + ' white: ' + str(whitefinal) + ' p: ' + str(p) + ' q: ' + str(q) + ' pv: ' + str(pv) + ' qv: ' + str(qv))
