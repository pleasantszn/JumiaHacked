import requests

amount = 50

print("fetching data ...")
for i in range(amount):
    
    if i > 9 : 
        url = "https://ng.jumia.is/unsafe/fit-in/340x340/filters:fill(white)/product/" + str(i) + "/489686/1.jpg"
        response = requests.get(url)
	file = open("image"+str(i)+".png", "wb")
        file.write(response.content)
	file.close()
        print("image index " + str(i) )
print("done ")

