
def jpg_generator(line):
    mid = line.split('\t')[0]
    num = line.split('\t')[1]
    faceid = line.split('\t')[4]
    return "{}/{}-{}.jpg".format(mid, num, faceid)

for n in range(11):
    d = {}

    with open("WC-MS-Celeb.tsv","r") as wikidata_pairs:
        if n != 10:
            for i in wikidata_pairs.readlines()[n*500000:(n+1)*500000]:
                d[i.split('\t')[1].rstrip()] = None
        else:
            for i in wikidata_pairs.readlines()[n*500000:]:
                d[i.split('\t')[1].rstrip()] = None

    a = 0
    with open("path/to/FaceImageCroppedWithOutAlignment.tsv", "r") as dataset:
        y = dataset.readline()
        while y:
            x = jpg_generator(y)
            if x in d:
                d[x] = y.split('\t')[-1]
            y = dataset.readline()
        
            if a%10000 == 0:
                print(n, a)
            a += 1

    final_dataset = open("data/Cropped-WC-MS-Celeb.tsv","a")
    wikidata_pairs = open("WC-MS-Celeb.tsv", "r")

    if n != 10:
        for i in wikidata_pairs.readlines()[n*500000:(n+1)*500000]:
            final_dataset.write(i.rstrip() + '\t' + d[i.split('\t')[1].rstrip()])
    else:
        for i in wikidata_pairs.readlines()[n*500000:]:
            final_dataset.write(i.rstrip() + '\t' + d[i.split('\t')[1].rstrip()])

    wikidata_pairs.close()
    final_dataset.close()

