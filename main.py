import language as l

# Specify all of the languages
languages = ("Duits", "Engels", "Frans", "Nederlands", "Pools", "Spaans")


if __name__ == "__main__":

    talen = []

    for taal in languages:
        talen.append( l.Language(taal) )

    totalTotalTime = 0.0

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

        # TODO Make printing look nice
        
        print(lijstBi)
        print(lijstTri)
