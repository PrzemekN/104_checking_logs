# Przemek Nawrocki 08.2017 ver 2.1
"""
|_Folder
    |_subFolder
        |_*.log

os.listdir
import os
dirname = "c:\\testy"
print(os.listdir(dirname))
print(glob.glob('c:\\testy\\*.txt'))
print([f for f in os.listdir(dirname)
     if os.path.isfile(os.path.join(dirname, f))])
"""
import glob
import sys
import time
# import mmap
# checking how many params were passed out, if less than 2 then stop
# first arg should be: string we are looking for, for example: ERROR
# second arg should be: path for folder in which there are subfolders for example: c:\testy
# whole call should looks like this, for example: python c:\<folder>\python_script.py error c:\testy
quantity_of_argv = len(sys.argv)
# argumenty liczymy od zera gdzie zero to nazwa skryptu
if quantity_of_argv < 3:
    print("missing arguments, we need 2 arguments")
    print("for example: skrypt.py <arg1> <arg2>")
    sys.exit(0)
# pobieranie czasu startu skryptu   
startlocaltime = time.asctime(time.localtime(time.time()))
#---------------
for i in range(1,len(sys.argv)):
    print ("tArgument",i, ":",sys.argv[i])
#---------------  
#storing list of folders 
folders_list = glob.glob(sys.argv[2] + '\\*\\')
# TODO posortowac listę: folders_list
print("lista podfolderow ",folders_list)
print('\n')
# for testing only
folders_list.sort()
#print("lista podfolderow ",folders_list)


quantity_of_folders = len(folders_list)
# TODO jako 1 parametr podawac gdzie ma tworzyc plik log, jesli wpisze puste to domyslnie tam skad uruchomiono skrypt czyli parametr 0
# otwieramy plik log tekstowy do wpisywania rezultatow
# niech tworzony plik log bedzie unikalny poprzez dolozenie do nazwy daty,godzina,sekundy
startlocaltimeformatted=startlocaltime.replace(':','')
startlocaltimeformatted=startlocaltimeformatted.replace(' ','')
nazwaPliku='c:\\testy\\summary'+startlocaltimeformatted+'.log'
podsumowanie=open(nazwaPliku, 'w')
podsumowanie.write(sys.argv[0]+'\n')
podsumowanie.write(sys.argv[1]+'\n')

#przejscie po podkatalogach w katalogu okreslonym jako wywolanie arg[2]
for k in range(0,quantity_of_folders):
    #print("PODFOLDER: ",folders_list[k])
    files_list = glob.glob(folders_list[k] + '\\*.log')
    # TODO posortowac listę: folders_list
    quantity_of_files = len(files_list)
    #print ("ilosc plików log  w podfolderze: ",quantity_of_files)
    for j in range(0,quantity_of_files):
       #print(files_list[j])
       with open(files_list[j]) as file:
           for line in file:
               #if 'ERROR' in line:
               if sys.argv[1] in line:
                   line= line.replace("  ", "")                   
                   podsumowanie.write(line)   
                   print(line)
                   print(j)
       print('\n')
#----------
stoplocaltime = time.asctime( time.localtime(time.time()) )
podsumowanie.write("START: ")
podsumowanie.write(startlocaltime)
podsumowanie.write("\n")
podsumowanie.write(" STOP: ")
podsumowanie.write(stoplocaltime)
podsumowanie.close()
print("KONIEC / STOP")	
