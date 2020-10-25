def plus_long(mots):
    output = mots[0]
    for mot in mots:
        if len(mot) > len(output):
            output = mot
    return output

assert plus_long(["Paris", "Strasbourg", "Lyon"]) \
       == "Strasbourg"

##############################################

def plus_grand(liste):
    m = liste[0]
    for e in liste:
        if m < e:
            m = e
    return m

assert plus_grand([4,8,3,9,10,3,4]) == 10

##################################

def somme(liste):
    return liste[0] + somme(liste[1:]) \
           if liste else 0

assert somme([5,6,2,3]) == 16

####################################

def get_pairs(liste):
    return [e for e in liste if e%2 == 0]

assert get_pairs([5,7,13]) == []
assert get_pairs([3,6,10,1]) == [6,10]

################################

def trier(liste):
    listeinit = liste.copy()
    
    while listeinit != []:
        max = plus_grand(listeinit)
        listeinit.remove(max)
        yield max


assert list(trier([8, 14, 5, 0, -2, 5])) \
       == [14, 8, 5, 5, 0, -2]

########################################

def get_filename(path):
    filename_with_ext = path.split("/")[-1]
    return filename_with_ext.split(".")[0]

assert get_filename("/usr/bin/toto.py") == "toto"
    
##################################

print([[i*j for i in range(0,5)] for j in range(1,5)])

###################################

def compter_char(texte):
    occurences = {}
    for c in texte:
        
        if c in occurences:
            occurences[c] += 1
        else:
            occurences[c] = 1

    return occurences

lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
compte = compter_char(lorem)
for char, count in compte.items():
    print("%s -> %s" % (char, count))
    
##############################################
    
example_dict = [{'name': 'Sebastian', 'email': 'Donec.felis.orci@consectetueripsumnunc.edu', 'country': '1979'}, {'name': 'Barclay', 'email': 'aliquet.metus.urna@neceleifend.co.uk', 'country': '2000'}, {'name': 'Vivien', 'email': 'pharetra@a.com', 'country': '1955'}, {'name': 'Britanney', 'email': 'eu.tellus.Phasellus@arcuvelquam.ca', 'country': '1961'}, {'name': 'Reese', 'email': 'tortor.dictum.eu@egestasSed.ca', 'country': '1951'}, {'name': 'Keegan', 'email': 'libero.nec@cursuset.co.uk', 'country': '1998'}, {'name': 'Ezekiel', 'email': 'tempus.mauris.erat@aclibero.org', 'country': '1951'}, {'name': 'Odessa', 'email': 'massa.Quisque.porttitor@felis.net', 'country': '1925'}, {'name': 'Elijah', 'email': 'luctus.vulputate.nisi@nunc.com', 'country': '1963'}, {'name': 'Hilel', 'email': 'lectus.pede.et@aliquetsem.ca', 'country': '1982'}, {'name': 'Callie', 'email': 'et.euismod.et@aliquetmagnaa.net', 'country': '1984'}, {'name': 'India', 'email': 'Duis.sit.amet@Phaselluslibero.com', 'country': '1938'}, {'name': 'Lane', 'email': 'amet@turpis.ca', 'country': '1922'}, {'name': 'Alexis', 'email': 'sagittis.placerat@nibhdolor.net', 'country': '1927'}, {'name': 'Micah', 'email': 'lorem.eget.mollis@SeddictumProin.com', 'country': '1914'}, {'name': 'Rigel', 'email': 'sollicitudin@eratinconsectetuer.org', 'country': '1941'}, {'name': 'Avram', 'email': 'tincidunt.vehicula@vulputate.org', 'country': '1919'}, {'name': 'Dieter', 'email': 'ornare.lectus.justo@Integeridmagna.org', 'country': '1937'}, {'name': 'Sarah', 'email': 'cubilia.Curae.Phasellus@non.net', 'country': '1946'}, {'name': 'Graham', 'email': 'elit.Curabitur.sed@maurisIntegersem.edu', 'country': '1931'}, {'name': 'Daquan', 'email': 'fermentum.convallis.ligula@porttitorinterdum.co.uk', 'country': '1934'}, {'name': 'Nell', 'email': 'purus@lectusconvallisest.org', 'country': '1997'}, {'name': 'Ocean', 'email': 'ut@Nuncquisarcu.net', 'country': '2006'}, {'name': 'Cruz', 'email': 'Aenean.euismod.mauris@idmollisnec.edu', 'country': '1950'}, {'name': 'Hyacinth', 'email': 'amet@Nunc.edu', 'country': '1929'}]

people_with_edu = [people["name"]
                   for people in example_dict
                   if people["email"].endswith(".edu")]
                   
###################################
    
def carre():
    i = 1
    while True:
        yield i**2
        i += 1

for c in carre():
    if c > 200:
        break
    print(c)

###########################################
    
def fibo():
    a, b = 0, 1
    yield a
    yield b
    
    while True:
        a, b = (b, a+b)
        yield b

for n in fibo():
    if n > 500:
        break
    print(n)