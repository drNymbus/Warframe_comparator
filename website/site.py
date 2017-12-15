import get_data

warframe_db = get_data.connect_db("db/warframe.sqlite")

def my_table(table, keys):
    rows = get_data.select(table)

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


#create a div perfectly formed for the home_page (all 3)
def create_bandeau(types, subcategory):
    my_div = ""

    return my_div

def create_weapons(table, keys):
    my_div = ""

    return my_div

def create_user(table, keys):
    my_div = ""

    return my_div

def page(bandeau, weapons, user):
    page = "<html><body>"
    page += bandeau
    page += weapons
    page += user
    page += "</body></html>"
    return page

#open a new_session with an apppropriate sesion_id(number)
def launch_session(session_id):
    html = ""

    return html

#close the session
def close_session(session_id):
    html = ""

    return html