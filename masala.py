 # 1-masala
# fruits = ['olma', 'banan', 'uzum']
# fruits.append('nok') 
# print(fruits)
# print(f"Ro'yxat uzunligi: {len(fruits)}") 

# if 'olma' in fruits:
#     print("Ha, ro'yxatda olma bor.")
# else:
#     print("Yo'q, ro'yxatda olma yo'q.")

# print(f"Bananning indeks raqami: {fruits.index('banan')}") 
# print(f"Mevalar ro'yxati: {fruits}")



# # 2-masala
# colors = ['qizil', 'yashil', 'ko\'k']

# colors.append('sariq')
# print(colors)

# colors.sort()
# print(f"Tartiblangan ro'yxat: {colors}") 
# print(f"Ro'yxat uzunligi: {len(colors)} ta elementdan iborat.")

# if 'yashil' in colors:
#     print("Ha, ro'yxatda yashil rang bor.")
# else:
#     print("Yo'q, ro'yxatda yashil rang yo'q.")
# print(f"Ranglar ro'yxati: {colors}")


# # 3-masala
# cities = ['Toshkent', 'Samarqand', 'Buxoro']

# cities.append('Xiva') 
# print(cities)

# print(f"Samarqand shahri indeks raqami: {cities.index('Samarqand')}") 

# print(f"Ro'yxat uzunligi: {len(cities)} ta shahar.") 

# cities.sort() 
# print(f"Tartiblangan ro'yxat: {cities}") 

# print(f"Tartiblangan ro'yxat: {sorted(cities)}")

# print(f"Asl ro'yxat: {cities}")

# # 4-masala:
# numbers = [5, 2, 8, 1]

# numbers.append(10)

# numbers.sort()

# length = len(numbers)

# has_eight = 8 in numbers

# print(f"Ro'yxat: {numbers}")
# print(f"Ro'yxat uzunligi: {length}")
# print(f"8 ro'yxatda mavjudmi? {'Ha' if has_eight else 'Yo\'q'}")

# # 5-masala
# animals = ['mushuk', 'it', 'qush']

# animals.append('baliq')

# animals.sort()

# print(animals)
# animals = ['mushuk', 'it', 'qush']
# animals.append('baliq')
# animals.sort()
# print(f"Hayvonlar ro'yxati: {animals}")
# print(f"Ro'yxat uzunligi: {len(animals)} ta hayvon.")
# if 'it' in animals:
#     print("Ha, ro'yxatda it bor.")
# else:
#     print("Yo'q, ro'yxatda it yo'q.")
# print(f"Itning indeks raqami: {animals.index('it')}")

# # 6-masala
# fruits = ['olma', 'banan', 'uzum', 'nok']
# fruits.append('apelsin')
# fruits.remove('banan')
# fruits.insert(3,'shaftoli')
# fruits.sort()
# print(fruits)
# print(f"Ro'yxat uzunligi: {len(fruits)} ta meva.")
# fruits.index('olma')
# if 'banan' in fruits:
#     print("Ha, ro'yxatda banan bor.")
# mavjud = 'shaftoli' in fruits
# if mavjud:
#     print("Ha, ro'yxatda shaftoli bor.")
# else:
#     print("Yo'q, ro'yxatda shaftoli yo'q.")
# print(f"Olmaning indeks raqami: {fruits.index('olma')}")

# # 7-masala
# menu = ['osh', 'lagmon', 'shashlik', 'somsa']
# menu.extend('manti',)
# menu.remove('lagmon')
# menu.sort()
# print(menu)
# print(f"Ro'yxat uzunligi: {len(menu)} ta taom.")
# menu.index('osh')
# if 'manti' in menu:
#     print("Ha, ro'yxatda manti bor.")
# mavjud = menu.index('shashlik')
# if 'shashlik' in menu:
#     print("Ha, ro'yxatda shashlik bor.")
# else:
#     print("Yo'q, ro'xatda osh yo'q.")

# # 8-masala
# cities = ['Toshkent', 'Samarqand', 'Buxoro', 'Xiva']
# cities.insert(0, 'Andijon')
# cities.remove('Xiva')
# cities.index('Samarqand')
# cities.sort()
# print(cities)
# print(f"Ro'yxat uzunligi: {len(cities)}")
# if 'Buxoro' in cities:
#     print('Buxoro')
# cities.pop()
# print(cities)

# # 9-masala
# students = ['Ali', 'Vali', 'Sardor', 'Aziz']
# students.append('Jamshid')
# students.remove('Sardor')
# students.insert(0, 'Jamshid')
# students.sort()
# students.index('Aziz')
# print(students)
# if 'Sardor' in students:
#     print('Sardor')
# students.pop()
# print(f"Ro'yxat uzunligi: {len(students)}")
# student_copy = students.copy()
# student_copy.append('Nodir ustoz')

# # 10-masala
# favorites = ['telefon', 'noutbuk', 'naushnik']
# favorites.append('planshet')
# favorites.append('soat')
# favorites.sort()
# print(f"Ro'yxat uzunligi: {len(favorites)}")
# favorites.index('noutbuk')
# if 'telefon' in favorites:
#      print(f"Ro'yxat uzunligi: {len(favorites)}")
#      favorites.remove('naushnik')
# favorites.pop()
# favorites_copy = favorites.copy()

# # 11-masala
# songs = ['Yomg\'ir', 'Sevgi', 'Hayot', 'Kuz']
# songs.insert(0, 'Yomg\'ir')
# songs.remove('Kuz')
# print(songs)
# songs.sort()
# print(songs)
# songs.index('Yomg\'ir')
# if 'hayot' in songs:
#     print('hayot')
# songs.pop()
# print(songs)
# print(f"Royxat uzunligi: {len(songs)}")
# songs.sort(reverse=True)
# songs.copy()
# print(songs)

# # 12-masala
# books = ['Alximik', 'Shaytanat', '1984']
# books.extend('Sariq devni minib')
# books.remove('Shaytanat')
# books.sort()
# print(books)
# books.index('1984')
# if 'Alximik' in books:
#     books.remove('Alximik')
# books.pop()
# print(books)
# print(f"Ro'yxat uzunligi: {len(books)}")
# books.sort(reverse=True)
# print(books)
# nusxa = books.copy()
# nusxa.append('Qirq yil')
# print(nusxa)

# # 13-masala
# movies = ['Inception', 'Matrix', 'Interstellar']
# movies.append('Parasite')
# movies.remove('Matrix')
# movies.sort()
# index = movies.index('Inception')
# print("Index",index)
# mavjud = 'Interstellar' in movies
# print("Ro'yhatda Interstellar bormi", mavjud)
# movies.pop()
# print("O'chirilgan filim",movies)
# uzunlik = len(movies)
# print("Ro'hat uzunligi",uzunlik)
# movies.sort(reverse=True)
# print(f"Teskari tartibda: {movies}")
# copy_movies = movies.copy()
# copy_movies.append('Joker')
# print("Asl ro'yxat:", movies)
# print("Nusxa:", copy_movies)

# # 14-masala
# emails = ['job_offer', 'spam', 'friend', 'news']
# emails.append('family')
# emails.remove('spam')
# emails.sort()
# index = emails.index('friend')
# print("Index",index)
# mavjud = 'job_offer' in emails
# print("Ro'yhatda job_offer bormi", mavjud)
# emails.pop()
# print("O'chirilgan emails",emails)
# uzunlik = len(emails)
# print("Ro'hat uzunligi",uzunlik)
# emails.sort(reverse=True)
# print(f"Teskari tartibda: {emails}")
# copy_emails = emails.copy()
# copy_emails.append('urgent')
# print("Asl ro'yxat:", emails)
# print("Nusxa:", copy_emails)

# # 15-masala:
# friends = ['Ali', 'Zara', 'Bobur', 'Nodir']
# friends.append('Jamol')
# friends.remove('Nodir')
# friends.sort()
# index = friends.index('Zara')
# print("Index",index)
# mavjud = 'Ali' in friends
# print("Ro'yhatda Ali bormi", mavjud)
# friends.pop()
# print("O'chirilgan emails",friends)
# uzunlik = len(friends)
# print("Ro'yhat uzunligi",uzunlik)
# friends.sort(reverse=True)
# print(f"Teskari tartibda: {friends}")
# copy_friends = friends.copy()
# copy_friends.append('Sardor')
# print("Asl ro'yxat:", friends)
# print("Nusxa:", copy_friends)

# # 16-masala
# animals = ['sher', 'yo\'lbars', 'ayiq', 'sher', 'quyon']
# animals.count('sher')
# animals.remove(animals[0])
# animals.append('kenguru')
# animals.sort()
# animals.index('yo\'lbars')
# if 'sher' in animals:
#     animals.remove('sher')
# animals.pop()
# print(animals)
# print(f"Ro'yxat uzunligi: {len(animals)}")
# nusxa = animals.copy()
# nusxa.append('sher')
# print(nusxa)

# # 17-masala
# champions = ['Khamzat Chimaev', 'Khabib Nurmagomedov', 'Conor McGregor', 'Mike Tyson', 'Wladimir Klichko', 'Eliud']
# champions.count('Mike Tyson')
# champions.pop()
# champions.extend('Bahodir Jalolov')
# champions.sort()
# print(champions.index('Mike Tyson'))
# print(champions)
# if 'Khabib Nurmagomedov' in champions:
#  champions.remove('Khabib Nurmagomedov')
# print(f"Royxat uzunligi: {len(champions)}")
# nusxa = champions.copy()
# nusxa.append('Khabib Nurmagomedov')
# print(nusxa)
# print(champions)

# # 18-masala
# cart = ['non', 'suyut', 'tuxum', "go'sht"]
# cart.index('tuxum')
# print(cart)
# cart.remove(cart[0])
# print(cart)
# cart.extend(cart)
# print(cart)
# cart.sort()
# print(cart)
# nusxa = cart.copy()
# print(nusxa)
# cart.clear()
# print(cart)
# if 'suyut' in cart:
#     cart.remove('suyut')
# print(cart)
# print(f"Royxat uzunligi: {len(cart)}")
# nusxa.pop()
# print(cart)

# # 19-masala
# courses = ['Python', 'Java', 'Data Science', 'Python']
# courses.count('Python')
# courses.remove('Java')
# print(courses)
# courses.extend('Web Development')
# print(courses)
# courses.sort()
# print(courses)
# courses.index('Data Science')
# print(courses)
# if 'Al' in courses:
#     courses.remove('Al')
# print(courses)
# courses.pop()
# print(courses)
# courses.remove('Python')
# print(courses)
# print(f"Ro'yhat uzunligi:{len(courses)}")
# nusxa = courses.copy()
# print(nusxa)

# # 20-masala
# cars = ['Chevrolet', 'Hyundai', 'Kia', 'Toyota']
# cars.insert(0, 'BMW')
# print(cars)
# cars.remove('Chevrolet')
# print(cars)
# nusxa = cars.copy()
# print(nusxa)
# cars.sort()
# print(cars)
# cars.index('Toyota')
# print(cars)
# if 'Chevrolet' in cars:
#     print(cars.index('Chevrolet'))
# cars.pop()
# print(cars)
# print(f"Ro'yxat uzunligi: {len(cars)}")
# cars.sort(reverse=True)
# print(cars)
# cars.clear()
# print(cars)
