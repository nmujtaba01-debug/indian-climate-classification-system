regions =[{'name': 'Western Ghats', 'rainfall':152},
          {'name':'Rajasthan','rainfall':60},
          {'name':'Kolkata','rainfall':100},
          {'name':'Meghalaya', 'rainfall': 250},
          {'name':'Amazon Basin','rainfall': 500}]

regions.append({'name':'Bangaluru','rainfall':360})


print('Indian Climate Classification System')
print('----------------------------')



for region in regions:
  if region['rainfall'] < 100:
    print(region['name'],'is an Arid region')

  elif region['rainfall'] >= 100 and region['rainfall'] < 300:
    print(region['name'],'is a moderate region')

  else:
    print(region['name'],'is a high rainfall region')
