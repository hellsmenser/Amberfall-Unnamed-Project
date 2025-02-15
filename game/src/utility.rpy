label initstats(anon=0, lucy=0, amber=0, story1=False, story2=false):
    
   $ anon_score = anon
   $ lucy_score = lucy
   $ amber_score = amber
   $ story_1 = story1
   $ story_2 = story2
   return

label get_ending:
   if anon_score >= 4 and lucy_score >= 4 and amber_score >= 4 and story_1 and story_2:
      return(4) # 4 эндинг
   elif anon_score >= 3 and lucu_score <=2 and amber_score >=4 and story_2: 
      return(3) # 3 эндинг
   elif anon_score <= 2 and lucy_score >=2 and amber_score >=3:
      return(2) # 2 эндинг
   else:
      return(1) # 1 эндинг