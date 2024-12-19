import os

from weather_sdk import get_new_event, SMSServer

token = os.getenv('FORECAST_TOKEN')
town_title = 'Курск'

token = os.getenv('SMS_TOKEN')
server = SMSServer(token)


new_event = get_new_event(token, town_title)
event_date = new_event.get_date()
event_time = new_event.get_time()
event_area = new_event.get_area()
phenomenon_description = new_event.get_phenomenon()


sms_template = '''{town_title}: {event_time} {event_date} {event_area} ожидается {phenomenon_description}. Будьте внимательны и осторожны.'''


# .format (town_title = "Курск" , event_time = new_event.get_time()  , event_date = new_event.get_date() , event_area = new_event.get_area()  , phenomenon_description = new_event.get_phenomenon() .'''



# print('sms_template',sms_template)
# print('sms_message')


# print(event_time)
# print(event_date)
# print(event_area)
# print(phenomenon_description)


# print('token', token)              
# print('new_event', new_event )     


# print('sms_template', sms_template)
# print('phenomenon_description', phenomenon_description )
# print('event_time', event_time)
# print('event_date', event_date)
# print('event_area', event_area)


sms_message = sms_template.format(
    phenomenon_description = new_event.get_phenomenon(),
    town_title = "Курск" ,
    event_time = new_event.get_time(),
    event_date = new_event.get_date(),
    event_area = new_event.get_area(),
)

server.send(sms_message)


# Гипотеза 1: В переменной нет прогноза погоды для Курска
# Способ проверки: Выведу переменную new_event
# Код для проверки: print(new_event)
# Установленный факт: Переменная new event хранит 'Регион:' и 'Погода:' 
# Вывод: В переменной нет прогноза погоды для Курска, гипотеза подтвердилась 


# Гипотеза 2.1: town_title на самом деле пуста
# Способ проверки: Выведу переменную town_title
# Код для проверки: print(town_title)
# Установленный факт: Переменная town_title хранит 'Курск' 
# Вывод: Гипотеза опроверглась, переменная town_titl хранит 'Курск'


# Гипотеза 2.2: В town_title не название города
# Способ проверки: Выведу переменную town_title
# Код для проверки: print(town_title) 
# Установленный факт: Переменная town_titl хранит 'Курск' 
# Вывод: Гипотеза опроверглась.


# Гипотеза 3: Переменная token на самом деле пуста
# Способ проверки: Выведу переменную token
# Код для проверки: print(token)
# Установленный факт:Переменная token хранит 'None' 
# Вывод: Гипотеза подтвердилась


# Гипотеза 4.1: Может, `token` всё ещё пуст?
# Способ проверки: Выведу переменную token
# Код для проверки: print(token) 
# Установленный факт: Переменная token хранит 85b98d96709fd49a69ba8165676e4592
# Вывод:Гипотеза опроверглась


# Гипотеза 4.2: Может, в токене не то значение, не 85b98d96709fd49a69ba8165676e4592
# Способ проверки: Поменяю значение переменной token
# Код для проверки: с помощью секретного редактора заменю значения переменной
# Установленный факт: после замены значения переменной ничего не изменилось, кроме самого значения переменной
# Вывод: Гипотеза опроверглась


# Гипотеза 4.3: Может, значение `85b98d96709fd49a69ba8165676e4592` успевает измениться до строчки `new_event = ...`?
# Способ проверки: вывести переменную token до строчки `new_event
# Код для проверки: print(token)
# Установленный факт:значение переменной token не изменилось 
# Вывод: Гипотеза опроверглась


# Гипотеза 5.1: Переменная `event_time` пуста/в ней не время
# Способ проверки: Выведу переменную event_time
# Код для проверки: print(event_time)
# Установленный факт: Переменная event_time пуста
# Вывод: Гипотеза подтвердилась


# Гипотеза 5.2: Переменная `event_date` пуста/в ней не дата
# Способ проверки: Выведу переменную event_date
# Код для проверки: print(event_date)
# Установленный факт: Переменная `event_date` содержит дату
# Вывод: Гипотеза опроверглась


# Гипотеза 5.3: Переменная `event_area` пуста/в ней не место
# Способ проверки: Выведу переменную event_area 
# Код для проверки: print(event_area)
# Установленный факт: Переменная `event_area` содержит место
# Вывод: Гипотеза опроверглась


# Гипотеза 5.4: Переменная `phenomenon_description` пуста/в ней не описание погодного явления
# Способ проверки: Выведу переменную phenomenon_description
# Код для проверки: print(phenomenon_description)
# Установленный факт: Переменная `phenomenon_description` содержит описание погодного явления
# Вывод: Гипотеза опроверглась


# Гипотеза 6: В шаблоне используются какие-то переменные, которые не передаются в .format()
# Способ проверки: Выделю поочерёдно все переменные, которые использую в шаблоне
# Код для проверки: Выделяю переменные поочерёдно  
# Установленный факт: Переменые передаются в format() 
# Вывод:Гипотеза опровергнута


# Гипотеза 7: Название переменных можно передавать в фигурные скобки 
# Способ проверки:Выведу переменную sms_template
# Код для проверки: print(sms_template)
# Установленный факт: названия переменных передаются в фигурные скобки
# Вывод: Гипотеза подтвердилась

# Гипотеза 8: Шаблон может быть передан в функцию send() 
# Способ проверки: Выведу переменную sms_message
# Код для проверки: print(sms_message)
# Установленный факт: переменная sms_message передается в функцию send()
# Вывод: Гипотеза подтвердилась


# Гипотеза 9: Если добавить к переменным ключевые аргументы в format() код заработает
# Способ проверки: добавить ключевые аргументы
# Код для проверки: .format (town_title = "Курск" , event_time = new_event.get_time()  , event_date = new_event.get_date() , event_area = new_event.get_area()  , phenomenon_description = new_event.get_phenomenon() .'''
# Установленный факт: Код не работает, так как были переданы строки а не переменные
# Вывод: Гипотеза опроверглась

# Гипотеза 10: Если передать переменные , а не строки, код заработает?
# Способ проверки: Передать переменные, а не строки
# Код для проверки: 
 # phenomenon_description = new_event.get_phenomenon(),
 #    town_title = "Курск" ,
 #    event_time = new_event.get_time(),
 #    event_date = new_event.get_date(),
 #    event_area = new_event.get_area(),
# )
# Установленный факт: Код работает, так как были переданы именно переменные
# Вывод: Гипотеза подтвердилась