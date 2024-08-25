from bs4 import BeautifulSoup

SIMPLE_HTML = """
<!DOCTYPE html>
<html>
    <head>
            <title>Page Demo</title>
            <link rel="stylesheet" href="style.css" type="text/css">
    </head>
    <body>
        <h1>Heading level 2</h1>
        <p class="test1">
            Lorem ipsum, dolor sit amet consectetur adipisicing elit. Placeat iure qui alias minus libero tempora dolores sint vitae quo tempore, quam similique ducimus officiis nostrum labore rem architecto accusantium. Nobis!
            Facilis, odit suscipit? Neque est eligendi repellendus magni. Quo, at itaque perspiciatis dignissimos sequi quibusdam quasi aut, a magnam amet, ut sit distinctio omnis ab praesentium ea tempore aliquam perferendis?
        </p>
        <p>
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eveniet, consequuntur aliquam rerum quasi reprehenderit reiciendis expedita temporibus libero aperiam! Vero mollitia accusamus ad tempora, est quos. Possimus fuga ipsam adipisci!
            Fugit ex rerum, ratione quae cupiditate, repudiandae repellat odio, nulla tempora est modi. Explicabo alias quia aperiam optio, odit quasi sunt ex exercitationem facere possimus culpa accusantium minima hic reprehenderit?
        </p>
        <ul>
            <li>Orange</li>
            <li>Apple</li>
            <li>Mango</li>
            <li>Banana</li>
        </ul>
    </body>
</html>
"""

soup = BeautifulSoup(SIMPLE_HTML,"html.parser")
h1_tag = soup.find("h1")
print(h1_tag.string)

li_tag = soup.find_all("li")
for li in li_tag:
    print(li.string)

p_tag = soup.find("p",attrs= {"class":"test1"} )
print(type(p_tag))
print(p_tag.string)

p_tag2 = soup.select_one("p.test1")
print(p_tag2.string)