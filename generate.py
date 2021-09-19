import json

# Open template
with open("template.txt") as f:
    template = f.read()

# Process content
with open("content.json") as f:
    content = json.load(f)

categories = set()

items_html = ""

for item in content:
    categories = categories.union(set([c.lower() for c in item["categories"]]))
    
    items_html += '<div class="item ' + ' '.join(item["categories"]) + '">\n' + \
                  '    <b>' + item["title"] + '</b>\n' + \
                  '    <p>' + item["desc"] + '</p>\n' + \
                  ('    <a href="' + item["link"] + '">Read more</a>\n' if "link" in item else "") + \
                  '</div>\n'

category_html = "\n".join([
    f'<div class="item">' + \
    f'    <input type="checkbox" name="{c.lower()}" id="{c.lower()}" onchange="update()" checked="true">' + \
    f'    <label for="{c.lower()}">{c}</label>' + \
    f'</div>'
    for c in categories
])

# Output
with open("index.html", "w") as f:
    f.write(template.replace(r"%%%CHECKBOXES%%%", category_html).replace(r"%%%ITEMS%%%", items_html))
