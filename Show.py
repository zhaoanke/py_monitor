from bs4 import BeautifulSoup
with open("data_center.html", "r+", encoding='utf-8') as html:
    html_1 = BeautifulSoup(html, 'lxml')
    divs = html_1.select('.chart-container')
    divs[0]["style"] = "width:10%;height:10%;position:absolute;top:0;left:2%;"
    divs[1]["style"] = "width:40%;height:40%;position:absolute;top:12%;left:2%;"
    divs[2]["style"] = "width:35%;height:10%;position:absolute;top:1%;left:30%;"
    divs[3]["style"] = "width:40%;height:40%;position:absolute;top:10%;left:25%;"
    divs[4]["style"] = "width:40%;height:35%;position:absolute;top:12%;left:55%;"
    divs[5]["style"] = "width:30%;height:35%;position:absolute;top:60%;left:5%;"
    divs[6]["style"] = "width:60%;height:50%;position:absolute;top:50%;left:35%;"

    body = html_1.find("body")
    body["style"] = """background-image:url("./img/za.jpg")"""  # 背景图片

    html_new = str(html_1)
    html.seek(0, 0)
    html.truncate()
    html.write(html_new)
    html.close()
