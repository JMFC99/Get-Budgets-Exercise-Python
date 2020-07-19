def getTotalBudget(people):
   Budget=0
   for person in people:
     Budget += person["budget"]
   return Budget
