outletSales = [[5, 6, 7, 7], [3 , 5, 6, 7], [12, 12, 11, 15]]
total = [0,0,0,0]
for quarter in range(0, 4):
    for outlet in range(0, 3): #Reduced to 3
        total[quarter] = total[quarter] + outletSales[outlet][quarter]
    #next outlet
    print(f"Total for quarter {quarter+1}, {total[quarter]}")
#next quarter
