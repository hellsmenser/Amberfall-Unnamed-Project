#Эффекты переходов
define fade = Fade(0.5, 0.5, 0.5)
define fx_shake = hpunch
define fade_to_black = Fade(0.3, 0.5, 0.0, color="#000")
define fade_from_black = Fade(0.0, 0.5, 0.3, color="#000")
define fade_to_white = Fade(0.1, 0.1, 0.5, color="#fff")
define dissolve_fast = Dissolve(0.25)
define dissolve_slow = Dissolve(1.0)

define pause_short = Pause(0.5)
define pause_medium = Pause(1.0)
define pause_long = Pause(2.0)

# Появление
transform appear_from_left(dist):
    xalign -0.5
    linear 0.5 dist

transform appear_from_right(dist):
    xalign 1.0
    linear 0.5 dist

transform exit_to_left:
    linear 1.0 xalign -0.5

transform exit_to_right:
    linear 0.5 xalign 1.5 