def arm(n):
    sum = 0
    order=len(str(n))
    copy_n=n
    
    while (n>0):
      digit=n%10
      sum+=digit **order
      n = n // 10

    if (sum==copy_n):
      print(f"{copy_n} is an armstrong number")
      result ={
        "Number":copy_n,
        "Armstrong":True,
        "IP":"127.0.0.5"
      }
    else:
      print(f"{copy_n} is not an armstrong number")
      result ={
      "Number":copy_n,
      "Armstrong":False,
      "IP":"127.0.0.5"
      }

    return result