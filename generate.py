import json


def get_content(item):
    categories = ' '.join(item["categories"])
    title = item["title"]
    date = item.get("date")
    desc = item["desc"]
    link = item.get("link")

    return '\n'.join([
        f'<div class="item {categories}">',
         '    <p class="categories">' + ', '.join(item["categories"]) + '</p>',
        f'    <b>{title}</b>\n',
        f'    <i>{date}</i>\n' if date else "",
        f'    <p>{desc}</p>\n',
        f'    <a href="{link}">Read more</a>\n' if link else "",
        f'</div>\n'
    ])


# Open template
with open("template.txt") as f:
    template = f.read()

# Process content
with open("content.json") as f:
    content = json.load(f)

# Name
template = template.replace(r"%%%NAME%%%", content["name"])
template = template.replace(r"%%%TITLE%%%", content["title"])

# Social media
template = template.replace(r"%%%LINKEDIN%%%", content["socialmedia"]["linkedin"])
template = template.replace(r"%%%TWITTER%%%", content["socialmedia"]["twitter"])

# Content
categories = set()

items_html = ""

for item in content["content"]:
    categories = categories.union(set([c.lower() for c in item["categories"]]))
    items_html += get_content(item)

category_html = '<div class="item"><input type="checkbox" name="all" id="all" onchange="allx()" checked="true">' + \
                '<label for="all">Select all/none</label></div>'
category_html += "\n".join([
    f'<div class="item">' + \
    f'    <input type="checkbox" name="{c.lower()}" id="{c.lower()}" onchange="update()" checked="true">' + \
    f'    <label for="{c.lower()}">{c}</label>' + \
    f'</div>'
    for c in categories
])

# Output
with open("index.html", "w") as f:
    f.write(template.replace(r"%%%CHECKBOXES%%%", category_html).replace(r"%%%ITEMS%%%", items_html))
