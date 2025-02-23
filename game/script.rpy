# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define e = Character('Эйлин', color="#c8ffc8")

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:

    scene bg room

    show eileen happy

    e "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed pellentesque quam id diam facilisis consectetur. Sed fringilla a risus in volutpat. Sed vulputate dictum felis, quis volutpat massa fermentum egestas. Aliquam erat volutpat. Aenean id maximus eros, nec aliquet velit. Aenean vel nibh eget turpis interdum aliquam."

    e "Добавьте сюжет, изображения и музыку и отправьте её в мир!"

    return
