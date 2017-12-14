import sqlite3
import crawler

tables = ['Primary', 'Secondary', 'Melee', 'AWP', 'AWM']

def clean_dict(dict, keys):
    for weapon in dict:
        for key in keys:
            value = weapon[key]

            value = value.replace(' ','')
            value = value.replace('%','')
            value = value.replace(' ','')
            value = value.replace('x','')
            value = value.replace('s','')

            try:
                value = value.encode("utf-8")
            except Exception as e:
                print("Can't encode(\"utf-8\"): " + str(e))
            try:
                float(value)
                weapon[key] = value
            except Exception as e:
                print(str(e))
                try:
                    int(value)
                    weapon[key] = value
                except Exception as e:
                    print("Can't do shit :"  + str(e))
            weapon[key] = value
    return dict

def create_tuple(weapon, keys):
    tuple = ()
    for key in keys:
        if key != 'Disposition':
            tuple = tuple + (weapon[key], )
    return tuple

########################################################################################################################

warframe_db = sqlite3.connect('db/warframe.sqlite')

i_table=0
for type in crawler.category:
    guns, keys = crawler.get_data(crawler.url_data, type)
    clean_dict(guns,keys)
    for weapon in guns:
        tuple = create_tuple(weapon, keys)
        try:
            warframe_db.execute('INSERT INTO '+tables[i_table]+'_weapon VALUES '+str(tuple))
            warframe_db.commit()
        except Exception as e:
            print("Cannot insert tuple: " + str(e))

warframe_db.close()
