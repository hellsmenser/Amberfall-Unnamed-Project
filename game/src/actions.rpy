#Эффекты переходов
define fade = Fade(0.5, 0.5, 0.5)
define fx_shake = hpunch
define fade_to_black = Fade(0.3, 0.5, 0.0, color="#000")
define fade_from_black = Fade(0.0, 0.5, 0.3, color="#000")
define fade_to_white = Fade(0.1, 0.2, 0.4, color="#fff")
define dissolve_fast = Dissolve(0.25)
define dissolve_slow = Dissolve(1.0)

define pause_short = Pause(0.5)
define pause_medium = Pause(1.0)
define pause_long = Pause(2.0)

define slow_text = Text(speed=20)

# Появление
define appear_from_left = MoveTransition(xalign=0.0, duration=0.5)
define appear_from_right = MoveTransition(xalign=1.0, duration=0.5)
define exit_to_left = MoveTransition(xalign=-0.5, duration=0.5)
define exit_to_right = MoveTransition(xalign=1.5, duration=0.5)

# Эффекты персонажей
define sway = At([hpunch, 0.1])
define shake = At([vpunch, 0.1])

