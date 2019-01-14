from morpheus import morph
import time
from statistics import mean

#data = []
#for i in range(100):
    #start = time.time()
path = "D:/gitapps/portfolio/texts.xlsx"

morph.import_text(path)
morph.new_parse()
#morph.print_main()
    #data.append(time.time() - start)
morph.print_test()

#print("average:", mean(data))