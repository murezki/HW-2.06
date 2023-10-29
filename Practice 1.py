# def biggest_dict(**kwargs):
#     yomayo = {'first_one': 'we can do it'}
#     yomayo.update(kwargs)
#     return yomayo
# output = biggest_dict(k1=22, k2=31, k3=11, k4=91, name='Елена', age=31, weight=61, eyes_color='grey')
# print(output)




#------



# newDict = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5}
# perestanovka = list(newDict.keys())
# newDict[perestanovka[-1]], newDict[perestanovka[0]] = newDict[perestanovka[0]], newDict[perestanovka[-1]]
# del newDict[perestanovka[1]]
# newDict['new_key'] = 'new_value'
# print(newDict)


#------

countries = {
    'Kazakhstan': 'Astana',
    'USA': 'Washington DC',
    'Yabadaba': 'Doo'
}

def add(country, capital, country_dict):
    country_dict[country] = capital

def remove(country, country_dict):
    if country in country_dict:
        del country_dict[country]
    else:
        print("ERROR")


def edit(country, new_capital, country_dict):
    if country in country_dict:
        country_dict[country] = new_capital
    else:
        print("ERROR")

add('Leeeee', 'Chotam', countries)
print(countries)

remove('Yabadaba', countries)
print(countries)

edit('USA', 'asfasc', countries)
print(countries)