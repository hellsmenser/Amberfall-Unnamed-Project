################################################################################
## Стили
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5

style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")

style bar:
    ysize gui.bar_size
    left_bar Frame("gui/window_icon.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/window_icon.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/window_icon.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/window_icon.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/window_icon.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/window_icon.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/window_icon.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/window_icon.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/window_icon.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/window_icon.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/window_icon.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/window_icon.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/window_icon.png", gui.frame_borders, tile=gui.frame_tile)

style window is default
style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/window_icon.png", xalign=0.5, yalign=1.0)

style namebox is default
style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/window_icon.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label is default
style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue is default
style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False

style input_prompt is default
style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width

style choice_vbox is vbox
style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is button
style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is button_text
style choice_button_text is default:
    properties gui.text_properties("choice_button")

style quick_button is default
style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text is button_text
style quick_button_text:
    properties gui.text_properties("quick_button")

style navigation_button is gui_button
style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text is gui_button_text
style navigation_button_text:
    properties gui.text_properties("navigation_button")

style main_menu_frame is empty
style main_menu_frame:
    xsize 420
    yfill True

    background "gui/window_icon.png"

style main_menu_vbox is vbox
style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text is gui_text
style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title is main_menu_text
style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version is main_menu_text
style main_menu_version:
    properties gui.text_properties("version")

style game_menu_outer_frame is empty
style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/window_icon.png"

style game_menu_navigation_frame is empty
style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame is empty
style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport is gui_viewport
style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side is gui_side
style game_menu_side:
    spacing 15

style game_menu_label is gui_label
style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text is gui_label_text
style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style about_label_text is gui_label_text
style about_label_text:
    size gui.label_text_size

style return_button is navigation_button
style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45

style page_label is gui_label
style page_label:
    xpadding 75
    ypadding 5

style page_label_text is gui_label_text
style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button is gui_button
style page_button:
    properties gui.button_properties("page_button")

style page_button_text is gui_button_text
style page_button_text:
    properties gui.text_properties("page_button")

style slot_button is gui_button
style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text is gui_button_text
style slot_button_text:
    properties gui.text_properties("slot_button")

style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label is gui_label
style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text is gui_label_text
style pref_label_text:
    yalign 1.0

style pref_vbox is vbox
style pref_vbox:
    xsize 338

style radio_vbox is pref_vbox
style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button is gui_button
style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/window_icon.png"

style radio_button_text is gui_button_text
style radio_button_text:
    properties gui.text_properties("radio_button")

style check_vbox is pref_vbox
style check_vbox:
    spacing gui.pref_button_spacing

style check_button is gui_button
style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/window_icon.png"

style check_button_text is gui_button_text
style check_button_text:
    properties gui.text_properties("check_button")

style slider_slider is gui_slider
style slider_slider:
    xsize 525

style slider_button is gui_button
style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text is gui_button_text
style slider_button_text:
    properties gui.text_properties("slider_button")

style slider_vbox:
    xsize 675

style history_window is empty
style history_window:
    xfill True
    ysize gui.history_height

style history_name is gui_label
style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text is gui_label_text
style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign

style history_text is gui_text
style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label is gui_label
style history_label:
    xfill True

style history_label_text is gui_label_text
style history_label_text:
    xalign 0.5

style help_button is gui_button
style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text is gui_button_text
style help_button_text:
    properties gui.text_properties("help_button")

style help_label is gui_label
style help_label:
    xsize 375
    right_padding 30

style help_label_text is gui_label_text
style help_label_text:
    size gui.text_size
    xalign 1.0
    textalign 1.0

style confirm_frame is gui_frame
style confirm_frame:
    background Frame([ "gui/window_icon.png", "gui/window_icon.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"

style confirm_button is gui_medium_button
style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text is gui_medium_button_text
style confirm_button_text:
    properties gui.text_properties("confirm_button")

style skip_frame is empty
style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/window_icon.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text is gui_text
style skip_text:
    size gui.notify_text_size

style skip_triangle is skip_text
style skip_triangle:
    ## Нам надо использовать шрифт, имеющий в себе символ U+25B8 (стрелку выше).
    font "DejaVuSans.ttf"

style notify_frame is empty
style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/window_icon.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text is gui_text
style notify_text:
    properties gui.text_properties("notify")

################################################################################
## Мобильные варианты стилей
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

style window:
    variant "small"
    background "gui/window_icon.png"

style radio_button:
    variant "small"
    foreground "gui/window_icon.png"

style check_button:
    variant "small"
    foreground "gui/window_icon.png"

style main_menu_frame:
    variant "small"
    background "gui/window_icon.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/window_icon.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/window_icon.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/window_icon.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/window_icon.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/window_icon.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/window_icon.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/window_icon.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/window_icon.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/window_icon.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/window_icon.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/window_icon.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/window_icon.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/window_icon.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900

image menu_button = "gui/button/Menu_Button.png"