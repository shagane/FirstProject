arm_let = 'ԱԲԳԴԵԶԷԹԺԻԼԽԾԿՀՂՃՄՅՆՇՈՉՊՌՍՎՏՐՑՓՔՕՖաբգդեզէթժիլխծկհղճմյնշոչպռսվտրցփքօֆ'
rus_let = 'АБГДЭЗЭТЖИЛХЦКհХЧМЙНШоЧПРСВТРЦПКОФабгдэзэтжилхцкհхчмйншочпрсвтрцпкоф'
arm_dict = { a: b for (a, b) in zip(arm_let, rus_let)}
arm_dict1 = {'Ձ':'ДЗ', 'ձ':'дз', 'Ջ':'ДЖ', 'ջ':'дж', 'և':'ев', ':':'.', 'ը': '', 'Ը':''}
arm_dict2 = {'Եւ':'ЕВ', 'ԵՒ':'ЕВ', 'եւ':'ев', 
            'ՈՒ':'У', 'ու':'у', 'իւ':'ю', 'աւ':'ай', 
            'եա':'й' , 'ԵԱ':'Й', ' Ո':' В', ' ո':' в', '\nՈ' : '\nВ', '\nո': '\nв'}
arm_dict3 = {' Ե':' Й', ' ե':' й', '\nԵ' : '\nЙ'}

arm_dict.update(**arm_dict1)

with open(r'd:\Shagane\arm-text.txt', encoding='utf-8') as arm:
    lines = arm.read()
rus = open(r'd:\Shagane\rus-text.txt', 'w', encoding='utf-8')
counter = 0

for i in lines:
    if counter < len(lines)-1 : 
        counter = counter + 1
        s = i + lines[counter]
        if s in arm_dict2:
            rus.write(arm_dict2[s])
        elif s in arm_dict3 and lines[counter+2]+lines[counter+3] in arm_dict2:
            pass
        elif s in arm_dict3 and lines[counter+2]+lines[counter+3] in arm_dict2:
            rus.write(arm_dict3[s])
        elif i in ['ւ', 'Ւ']:
            pass
        elif i in arm_dict:
            rus.write(arm_dict[i])
        else:
            rus.write(i)
    
rus.close()

   