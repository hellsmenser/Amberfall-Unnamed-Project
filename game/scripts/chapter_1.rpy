label ch1_beginning:
    jump ch1_wake_up

label ch1_wake_up:
    jump ch1_decoration_start

label ch1_decoration_start:
    menu:
        "Повесить плакат":
            jump ch1_decorate_poster
        "Повесить флажки":
            jump ch1_decorate_flags
        "Повесить шарики":
            jump ch1_decorate_balloons
    jump ch1_bday_congrats

label ch1_decorate_poster:
    jump ch1_decoration_start

label ch1_decorate_flags:
    jump ch1_decoration_start

label ch1_decorate_balloons:
    jump ch1_decoration_start

label ch1_bday_congrats:
    jump ch1_visit_reed        

label ch1_visit_reed:
    jump ch1_store_errand

label ch1_store_errand:
    menu:
        "Швырнуть банку со всей силы":
            pass
        "Прицелиться и кинуть её как баскетболист":
            pass
        "Не выёбываться и спокойно подойти к мусорке":
            pass    
    jump ch1_came_home

label ch1_came_home:
    menu:
        "Xrox":
            jump ch1_xrox
        "Журналы":
            jump ch_1_journals
        "Телик":
            jump ch_1_tv
    jump ch1_garage

label ch1_xrox:
    jump ch1_came_home

label ch1_journals:
    jump ch1_came_home 

label ch1_tv:
    jump ch1_came_home

label ch1_garage:
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