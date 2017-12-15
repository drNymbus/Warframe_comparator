import get_data

warframe_db =get_data.connect_db("db/warframe.sqlite")

"""def my_table(dicts, keys):
    table = "<table><tr>"

    for i in range(len(keys)):
        table = table + "<th>" + keys[i] + "</th>"
    table = table + "</tr>"

    table += "<tr>"

    for i in range(len(dicts)):
        dict = dicts[i]
        checkbox_v = dict['Name']

        table += "<input type=\"checkbox\" value=\"" + checkbox_v + "\">"
        table += "<label for=\"" + checkbox_v + "\">"

        for j in range(len(keys)):
            v = dict[keys[j]]
            table += "<td>" + v + "</td>"

        table += "</label>"

    table += "</tr></table>"
    return table


def my_div(dicts, keys, my_class):
    table = my_table(dicts, keys)
    div = "<div class=\"" + my_class + "\">" + table
    div += "</div>"
    return div


def home_page(bandeau, weapons, user):
    page = "<html><body>"
    page += bandeau
    page += weapons
    page += user
    page += "</body></html>"
    return page

"""
def my_table(table, keys):
    rows = get_data.select(warframe_db,table)

    page = "<table><tr>"
    for key in keys:
        page += "<th>" + key + "</th>"
    page += "</tr>"

    for row in rows:
        page += "<tr>"
        page += "<input type=\"checkbox\" value=\"" + row[0] + "\">"
        page += "<label for=\"" + row[0] + "\">"
        for i in range(len(keys)):
            page += "<td>"+ row[i] +"</td>"
        page += "</tr></label>"

def my_div(table, keys, div_class):
    table = my_table(table, keys)
    div = "<div class=\"" + div_class + "\">" + table
    div += "</div>"
    return div

def home_page(bandeau, weapons, user):
    page = "<html><body>"
    page += bandeau
    page += weapons
    page += user
    page += "</body></html>"
    return page
