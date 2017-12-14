def my_table(dicts, keys):
    table = "<table><tr>"
    for i in range(len(keys)):
        table = table + "<th>" +keys[i]+ "</th>"
    table = table  + "</tr>"
    table += "<tr>"
    for i in range(len(dicts)):
        for j in range(len(keys)):
            dict = dicts[i]
            v = dict[keys[j]]
            table += "<td>" + v + "</td>"

    table += "</tr>"
    table = table + "</table>"
    return table

def my_div(dicts,keys,my_class):
    table = my_table(dicts,keys)
    div = "<div class=\""+my_class+"\">" + table
    div += "</div>"
    return div

def home_page(bandeau,weapons,user):
    page = "<html><body>"
    page += bandeau
    page += weapons
    page += user
    page += "</body></html>"
    return page
