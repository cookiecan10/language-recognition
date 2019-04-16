import language as l

# Specify all of the languages
languages = ("Duits", "Engels", "Frans", "Nederlands", "Pools", "Spaans", "Python")


if __name__ == "__main__":

    talen = []

    for lang in languages:
        talen.append(l.Language(lang))


    totalTotalTime = 0
    
    for taal in talen:
        
        taal.createDirs()

        taal.deleteUltimodels()
        
        if taal.hasUltimodels():
            taal.loadUltiModels()
        else:
            print("Calculating ({})".format(taal.language))
    
            totalTime = l.timer(taal.makeUltimodels)
    
            totalTotalTime += totalTime
            print("({}) Time: {}".format(taal.language, totalTime))
            print("")
            taal.saveUltiModels()

    while True:
        text = input("Geef input pls: ")

        lijstBi = []
        lijstTri = []
        
        for taal in talen:
            taal.loadUltiModels()

            text = taal.prepare(text)
            
            lijstBi.append([taal.language, taal.calcBiChance(text)])
            lijstTri.append([taal.language, taal.calcTriChance(text)])

        totalBi = 0
        totalTri = 0
        for item in lijstBi:
            totalBi += item[1]

        for item in lijstTri:
            totalTri += item[1]

        for item in lijstBi:
            item[1] = item[1]/totalBi*100

        for item in lijstTri:
            item[1] = item[1]/totalTri*100

        largestBi = lijstBi[0]
        print("Bi-grammen:")
        for ding in lijstBi:
            if ding[1] > largestBi[1]:
                largestBi = ding
            print("{:<10}  {:.2f}%".format(ding[0], ding[1]))

        print("The language is: {}".format(largestBi[0]))
        print("\nTri-grammen:")

        largestTri = lijstTri[0]
        for ding in lijstTri:
            if ding[1] > largestTri[1]:
                largestTri = ding
            print("{:<10}  {:.2f}%".format(ding[0], ding[1]))

        print("The language is: {}".format(largestTri[0]))

        
