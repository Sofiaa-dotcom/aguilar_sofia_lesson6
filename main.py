while True:
    if input.sound_level() > 2:
         light.set_all(color.rgb(0, 180, 255))
    else: 
        light.clear()
