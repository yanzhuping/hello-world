# def funA(desA):
#     print("It's funA")
#
#
# def funB(desB):
#     print("It's funB")
#
#
# @funA
# def funC():
#     print("It's funC")
#
# def funA(desA):
#     print("It's funA")
#
#
# def funB(desB):
#     print("It's funB")
#
#
# # @funB
# # @funA
# def funC():
#     print("It's funC")
#


# def funA(desA):
#     print("It's funA")
#
#     print('---')
#     print(desA)
#     desA()
#     print('---')
#
#
# def funB(desB):
#     print("It's funB")
#
#
# @funB
# @funA
# def funC():
#     print("It's funC")

# def funA(desA):
#     print("It's funA")
#
#
# def funB(desB):
#     print("It's funB")
#     print('---')
#     print(desB)
#
#
# @funB
# @funA
# def funC():
#     print("It's funC")

# a={'a':111,"b":2222}
# print(type(a.keys()))
# print(a.keys())
#
# print (','.join(sorted(map(str,a.keys()))))

a={"a":{"name":"yanzp","age":"27"},"b":2,"c":3,"d":4}
a={"a":{"name":"yanzp","age":"27"},"b":2,"c":3,"d":4}
# print(a)
# print(a.items())
# print(a.values())
# print(list(a.items()))  #以列表形式显示字典所有的键
# print(list(a.values()))   #以列表形式显示字典所有的值
keyAndValues=list(a.items())
for keyAndValue in keyAndValues:
    if isinstance(keyAndValue[1],dict):
        news=list(keyAndValue[1].items())
        print(news)
        for new in news:
            print(new[0])
            print(new[1])
    else:
        print(keyAndValue[0],type(keyAndValue[0]))
        print(keyAndValue[1],type(keyAndValue[1]))


#这是master分支

