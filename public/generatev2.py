import random

def generateHTMLpage(pageNum, linkName):
    if linkName == 0:
        f = open("dummy/%s.html" % pageNum, 'w')
        f.write("<html> \n <body> \n <h1>HEY MY page num is %s </h1> \n </body> \n </html>" % pageNum)
        f.close
    else:
        f = open("dummy/%s.html" % pageNum, 'w')
        f.write('<html> \n <body> \n <h1>HEY MY page num is %s </h1> \n <br> \n <a href="%s"> link to %s! </a> <br> \n </body> \n </html>' % (pageNum, linkName, linkName))
        f.close

#    pageName = pageNum + ".html"
#    return pageName

def generateBadXML(pageNum):
    lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam vitae tortor tincidunt, pulvinar urna sit amet, mollis libero. Phasellus a laoreet purus. Suspendisse sagittis sollicitudin metus, nec venenatis ligula porttitor eget. Duis sed ipsum nisl. Curabitur dignissim vehicula augue, sed congue dui condimentum eget. Nam ante eros, egestas vel tristique a, viverra in leo. Cras commodo ornare dolor a vestibulum. Morbi id lorem fermentum, elementum lacus sed, fermentum nunc. Maecenas vel elit magna. Integer malesuada, metus quis mattis auctor, odio ante placerat justo, eget consectetur magna enim a neque. Etiam sit amet felis vitae urna adipiscing fermentum. Proin eu dolor bibendum, pellentesque ante nec, semper lectus. Proin at quam non massa porttitor luctus id vitae lectus. Praesent mollis non dui non gravida. Etiam ultricies augue accumsan, consequat metus eget, fermentum mi."
    f  = open("dummy/%s.xml" % pageNum, 'w')
    f.write('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>' + '\n'
            + '<data>' + '\n' + lorem + '\n' + '</data>')
    f.close

#    pageName = pageNum + ".xml"
#    return pageName

def generateGoodXML(pageNum):
    lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam vitae tortor tincidunt, pulvinar urna sit amet, mollis libero. Phasellus a laoreet purus. Suspendisse sagittis sollicitudin metus, nec venenatis ligula porttitor eget. Duis sed ipsum nisl. Curabitur dignissim vehicula augue, sed congue dui condimentum eget. Nam ante eros, egestas vel tristique a, viverra in leo. Cras commodo ornare dolor a vestibulum. Morbi id lorem fermentum, elementum lacus sed, fermentum nunc. Maecenas vel elit magna. Integer malesuada, metus quis mattis auctor, odio ante placerat justo, eget consectetur magna enim a neque. Etiam sit amet felis vitae urna adipiscing fermentum. Proin eu dolor bibendum, pellentesque ante nec, semper lectus. Proin at quam non massa porttitor luctus id vitae lectus. Praesent mollis non dui non gravida. Etiam ultricies augue accumsan, consequat metus eget, fermentum mi."
    keywords = ["nsidc", "penguins", "oai", "nutch", "polar", "center"]
    f = open("dummy/%s.xml" % pageNum, 'w')
    f.write('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>' + '\n'
            + '<data>' + '\n' + lorem + '\n' + keywords[random.randint(0, 5)] + '</data>')

#    return pageName

def goodorbadXML(percentofgood):
    num = 100 * percentofgood
    if num > random.randint(0, 100):
        return False
    else:
        return True




def generateSite(numHTML, numXML, maxDepth, percentofgood):

    i = 0
    q = 0

    f = open("index.html", 'w')
    htmlbegin = "<html> \n <body> \n <h4> Site exists for testing nutch and nutch plugins, there will be a variety of files on this site, this siter is generated with the pythonfile named generate.py, ask Erik Mingo if you cannot find </h4>"
    htmlend = "</body> \n </html>"
    f.write(htmlbegin)
    while i < numHTML:
        depth = random.randint(0, maxDepth)
        if q > numXML:
            if depth == 0:
                generateHTMLpage(i, 0)
                f.write('<a href="dummy/%s.html"> Link to %s </a> \n <br> \n' %(i, i))
                i = i + 1
            else:
                z = 0
                while z <= depth:
                    currentpage = "depthno%s_%s" % (i, z)
                    lastpagecounter = z - 1
                    lastpage = "depthno%s_%s" %  (i, lastpagecounter)
                    if z == 0:
                        generateHTMLpage(i, currentpage + ".html")
                        f.write('<a href="dummy/%s.html"> Link to %s </a> \n <br> \n' %(i, i))
                        i = i + 1
                    elif z == depth:
                        generateHTMLpage(lastpage, 0)
                    else:
                        generateHTMLpage(lastpage, currentpage + ".html")
                    z = z + 1

        else:
                xmlname = str(q) + ".xml"
                if depth == 0:
                    if goodorbadXML(percentofgood):
                        generateGoodXML(str(q))
                        generateHTMLpage(i, xmlname)
                        f.write('<a href="dummy/%s.html"> Link to %s </a> \n <br> \n' %(i, i))
                        i = i + 1
                        q = q + 1
                    else:
                        generateBadXML(str(q))
                        generateHTMLpage(i, xmlname)
                        f.write('<a href="dummy/%s.html"> Link to %s </a> \n <br> \n' %(i, i))
                        i = i + 1
                        q = q + 1
                else:
                    z = 0
                    while z <= depth:
                        currentpage = "depth%s_%s" % (i, z)
                        lastpagecounter = z - 1
                        lastpage = "depth%s_%s" % (i, lastpagecounter)
                        if z == 0:
                            generateHTMLpage(i, currentpage + ".html")
                            f.write('<a href="dummy/%s.html"> Link to %s </a> \n <br> \n' %(i, i))
                            i = i + 1
                        elif z == depth:
                            if goodorbadXML(percentofgood) == True:
                                generateHTMLpage(lastpage, xmlname)
                                generateGoodXML(str(q))
                                q = q + 1
                            else:
                                generateHTMLpage(lastpage, xmlname)
                                generateBadXML(str(q))
                                q = q + 1
                        else:
                            generateHTMLpage(lastpage, currentpage + ".html")
                        z  = z + 1



generateSite(1000, 50, 5, .25)
