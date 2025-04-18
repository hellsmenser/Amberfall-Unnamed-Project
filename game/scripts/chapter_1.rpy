label ch_1_beginning:
    
    jump ch1_wake_up

label ch1_wake_up:
    
    jump ch1_decoration_start

label ch1_decoration_start:
    
    menu:
        "Повесить плакат":
            jump ch1_poster_scene  

label ch1_poster_scene:
    menu:
        "Повесить флажки":
            jump ch1_flags_scene

label ch1_flags_scene:
    
    menu:
        "Повесить шарики":
            jump ch_1_ballons_scene

label ch1_ballons_scene:
    
    jump ch1_bday_congrats1

label ch1_bday_congrats1:

    jump ch1_visit_reed        

label ch1_visit_reed:
    
    jump ch1_store_errand

label ch1_store_errand:

    menu:
        "Швырнуть банку со всей силы":
            jump ch1_trash_throw
        "Прицелиться и кинуть её как баскетболист":
            jump ch1_trash_nba
        "Не выёбываться и спокойно подойти к мусорке":
            jump ch_1_trash_normis    

label ch1_trash_throw:

    jump ch1_came_home

label ch1_trash_nba:

    jump ch1_came_home

label ch1_trash_normis:

    jump ch1_came_home        

label ch_1_came_home:

    menu:
        "Xrox":
            jump ch1_xrox
        "Журналы":
            jump ch_1_journals
        "Телик":
            jump ch_1_tv

label ch_1_xrox:

    jump ch_1_garage_incident

label ch_1_journals:

    jump ch_1_garage_incident 

label ch_1_tv:

    jump ch_1_garage_incident

label ch1_garage_incident:

    jump ch1_dinner_prep

label ch1_dinner_prep:

    jump ch1_guests_arrival

label ch1_guests_arrival:

    jump ch1_gifts_and_cake

label ch1_gifts_and_cake:

    jump ch1_night_out_decision

label ch1_night_out_decision:
    
    menu:
        "Разрешить уйти":
            $ ember_affection += 1
            jump ch1_night_out_allowed
        "Запретить":
            $ anon_strict += 1
            jump ch1_night_out_denied

label ch1_night_out_allowed:
    
    jump ch1_end
    
label ch1_night_out_denied:
    
    jump ch1_end    

label ch1_end:

    return