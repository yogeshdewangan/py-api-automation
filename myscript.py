print("Hello")

output = ""


for i in range(10):
    output += str(i*2)


html = '<html><body><header>'+output+'</header></body></html>'

f = open("report1.html", "a")
f.write(html)
f.close()

