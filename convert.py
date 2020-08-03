#IN ORDER TO RUN YOU MUST DOWNLOAD CHROMEDRIVER.EXE WHICH CAN BE FOUND HERE:
#https://chromedriver.chromium.org/
#THIS MUST THEN BE PLACED IN THE SAME FOLDER AS THIS PYTHON FILE
from selenium import webdriver
driver = webdriver.Chrome()

#ENTER THE PATH TO THE TXT FILE CONTAINING THE TIKTOK DESKTOP URLS HERE
#MAKE SURE TO USE DOUBLE SLASHES IF ON WINDOWS
#THE FILE SHOULD BE FORMATTED SO IT HAS ONE LINK PER LINE, NO BLANK LINES AND NOTHING ELSE

file = open("C:\\Users\\jack-\\Documents\\tiktokConvertorTestFile.txt", 'r')
urls = []
i = 1

for line in file:
    print("Processing line: " + str(i))
    url = str(line).rstrip().lstrip()
    driver.get(url)
    urls.append(str(driver.current_url))
    i += 1

#THIS WILL BE SAVED IN THE SAME FOLDER AS THIS PYTHON FILE
#PLEASE ENSURE THAT THERE IS NO OTHER FILE NAMED THE SAME
with open('Tiktok_Desktop_Links.txt', mode='w') as links_file:
    for link in urls:
        links_file.write(link + "\n")





