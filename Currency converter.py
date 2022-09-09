M=int(input("Value> "))
unit= input("For {R}upee For {D}ollar For {Y}en: ")
if unit =='R':
    Do=M/79.51
    Ye=M*1.75
    print("Dollar= ",Do)
    print("Yen= ",Ye)
          
if unit =='D':
    Ru=M*79.51
    Ye=M*138.64
    print("Rupees= ",Ru)
    print("Yen= ",Ye)

if unit =='Y':
    Ru=M/1.75
    Do=M/138.64
    print("Rupees= ",Ru)
    print("Dollar= ",Do)


