from collections import defaultdict

# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
conversion={'M':1000000,'B':1000000000}
def convert(damages):
    updated_damages=[]
    for damage in damages:
        unit = damage[-1]
        try:
            number = float(damage[:-1])
        except ValueError:
            updated_damages.append(damage)
        if unit in conversion:
            updated_damages.append(conversion[unit]*number)
        
        
        #if damage[-1] == "M":
        #    damage=float(damage[:-1]+"000000")
        #elif damage[-1] == "B":
        #    damage=float(damage[:-1]+'000000000')
        #updated_damages.append(damage)
            
    return updated_damages    
new_damages=convert(damages)




# write your construct hurricane dictionary function here:
hurricanes={}
for i in range(0,len(names)):
    #hurricanes[names[i]]=[months[i],years[i],max_sustained_winds[i],areas_affected[i],damages[i],deaths[i]]
    hurricanes[names[i]]={"Name":names[i],
                "Month":months[i],
                "Year":years[i],
                "Max Sustained Wind":max_sustained_winds[i],
                "Areas Affected":areas_affected[i],
                "Damage":new_damages[i],
                "Deaths":deaths[i]}





# write your construct hurricane by year dictionary function here:

def sort_by_year(hurricanes):
    hurricanes_by_year={}
    for i in hurricanes.values():
        current_year=i.get('Year')
        current_cane=i
        #print(current_year)
    
        if current_year in hurricanes_by_year:
            #print("in")
            #print(hurricanes_by_year)
            #print(current_cane)
            #print(hurricanes_by_year[current_year])
            #print("\n")
            hurricanes_by_year[current_year].append(current_cane.values())
            #hurricanes_by_year[current_year]=new_year_entr
    
        else:
            hurricanes_by_year[current_year]=[current_cane]
    #print(hurricanes_by_year[1932])
    return hurricanes_by_year





# write your count affected areas function here:

def count_by_areas(hurricanes):
    d= defaultdict(int)
    areas=[]
    for key in hurricanes:
        temp=hurricanes.get(key).get("Areas Affected")
        for each in temp:
            areas.append(each)
    #print(areas)
        
    for k in areas:
        d[k]+=1
    return d

affected_areas_count=count_by_areas(hurricanes)



# write your find most affected area function here:
def most_affected_area(dictionary):
    max_area = ''
    max_area_count = 0
    for each in dictionary:
        if dictionary.get(each)>max_area_count:
            max_area = each
            max_area_count = dictionary.get(each)
    return max_area






# write your greatest number of deaths function here:
def most_deaths(dictionary):
    cane = ''
    counter = 0
    for key in dictionary:
        deaths=dictionary.get(key).get("Deaths")
        if deaths>counter:
            counter = deaths
            cane = dictionary.get(key).get('Name')
    return cane, counter





# write your catgeorize by mortality function here:

mortality_scale = {0:0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}
def mortality_dict(dictionary):
    mortality_dict={0:[],1:[],2:[],3:[],4:[],5:[]}
    for key in dictionary:
        name = dictionary.get(key).get('Name')
        deaths = dictionary.get(key).get('Deaths')
        if deaths>mortality_scale[4]:
            mortality_dict[5].append(dictionary[key])
            continue
        
        elif deaths>mortality_scale[3]:
            mortality_dict[4].append(dictionary[key])
            continue
        elif deaths>mortality_scale[2]:
            mortality_dict[3].append(dictionary[key])
            continue
        elif deaths>mortality_scale[1]:
            mortality_dict[2].append(dictionary[key])
            continue
        elif deaths>mortality_scale[0]:
            mortality_dict[1].append(dictionary[key])
            continue
        else:
            mortality_dict[0].append(dictionary[key])
        
    return mortality_dict





# write your greatest damage function here:
def most_damage(dictionary):
    cane = ''
    counter = 0
    for key in dictionary:
        damage=dictionary.get(key).get("Damage")
        try:
            if damage>counter:
                counter = damage
                cane = dictionary.get(key).get('Name')
        except:
            continue
    return cane, counter






# write your catgeorize by damage function here:
damage_scale = {0:0,
               1: 100000000,
               2: 1000000000,
               3: 10000000000,
               4: 50000000000}
def damage_dict(dictionary):
    damage_dict={0:[],1:[],2:[],3:[],4:[],5:[]}
    for key in dictionary:
        name = dictionary.get(key).get('Name')
        damage = dictionary.get(key).get('Damage')
        try:
            if damage>damage_scale[4]:
                damage_dict[5].append(dictionary[key])
                continue
        
            elif damage>damage_scale[3]:
                damage_dict[4].append(dictionary[key])
                continue
            elif damage>damage_scale[2]:
                damage_dict[3].append(dictionary[key])
                continue
            elif damage>damage_scale[1]:
                damage_dict[2].append(dictionary[key])
                continue
            elif damage>damage_scale[0]:
                damage_dict[1].append(dictionary[key])
                continue
            else:
                damage_dict[0].append(dictionary[key])
        except:
            damage_dict[0].append(dictionary[key])
        
    return damage_dict