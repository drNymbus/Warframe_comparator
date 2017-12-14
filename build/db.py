import sqlite3
warframe_db = sqlite3.connect("db/warframe.sqlite")

try:
    warframe_db.execute('''
    CREATE TABLE Primary_weapon (
        name text PRIMARY KEY,
        trigger text,
        damage double float,
        crit_c float,
        crit_d float,
        status float,
        projectile text,
        fire_rate float,
        mag_size int,
        reload float,
        mastery int
    )''')
    warframe_db.commit()
except Exception as e:
    print("Primary_weapon :"+str(e))

try:
    warframe_db.execute('''
    CREATE TABLE Secondary_weapon (
        name text PRIMARY KEY,
        trigger text,
        damage double float,
        crit_c float,
        crit_d float,
        status float,
        projectile text,
        fire_rate float,
        mag_size int,
        reload float,
        mastery int
    )''')
    warframe_db.commit()
except Exception as e:
    print("Secondary_weapon :"+str(e))

try:
    warframe_db.execute('''
    CREATE TABLE Melee_weapon (
        name text PRIMARY KEY,
        type text,
        damage double float,
        slide int,
        att_speed float,
        crit_c float,
        crit_d float,
        status_chance int,
        mastery int
    )''')
    warframe_db.commit()
except Exception as e:
    print("Melee_weapon :"+str(e))

try:
    warframe_db.execute('''
    CREATE TABLE AWP_weapon (
        name text PRIMARY KEY,
        type text,
        damage double float,
        crit_c float,
        crit_d float,
        status int,
        projectile text,
        fire_rate float,
        mag_size int,
        reload_t int,
        mastery int
    )''')
    warframe_db.commit()
except Exception as e:
    print("AWP_weapon :"+str(e))

try:
    warframe_db.execute('''
    CREATE TABLE AWM_weapon (
        name text PRIMARY KEY,
        damage double float,
        slide int,
        att_speed float,
        crit_c float,
        crit_d float,
        status_chance int,
        mastery int
    )''')
    warframe_db.commit()
except Exception as e:
    print("AWM_weapon :"+str(e))

warframe_db.close()