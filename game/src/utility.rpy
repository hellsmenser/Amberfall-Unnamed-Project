label initstats:
   default anon_score = 0
   default talk_time = 0
   default amber_score = 0
   default story_1 = False
   default story_2 = False
   
   default poster_added = False
   default flags_added = False
   default balloons_added = False
   return

label get_ending:
   if anon_score >= 4 and amber_score >= 5 and talk_time >= 5 and story_1 and story_2:
      return(4) # 4 эндинг
   elif anon_score >= 3 and amber_score >= 3 and talk_time >= 3  and story_2: 
      return(3) # 3 эндинг
   elif anon_score < 2 and amber_score < 3 and talk_time < 3:
      return(2) # 2 эндинг
   else:
      return(1) # 1 эндинг