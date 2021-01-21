if year%4 == 0 :
  # 4로 나누어떨어지며 100으로는 나누어떨어지지 않는 경우
  if year%100 != 0 :
    print("Leap Year")
  # 4로 나누어떨어지며 100으로도 나누어떨어지는 경우
  else :
    if year%400 == 0 :
      print("Leap Year")
    else :
      print("Not Leap Year")
else :
  print("Not Leap Year")
