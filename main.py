# This code prints out the outcome of pressing A

def on_button_pressed_a():
    basic.show_string("YOUAREENOUGH!", 70)
input.on_button_pressed(Button.A, on_button_pressed_a)

# This code prints out the outcome of tilting the bit left

def on_gesture_tilt_left():
    basic.show_arrow(ArrowNames.NORTH)
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

# This code prints out the outcome of pressing A and B

def on_button_pressed_ab():
    basic.show_string("LIVEYOURLIFE! ", 70)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

# This code prints out the outcome of pressing B

def on_button_pressed_b():
    basic.show_string("YOUAREYOURSELF!", 70)
input.on_button_pressed(Button.B, on_button_pressed_b)

# This code prints out the outcome of shaking the micro bit

def on_gesture_shake():
    basic.show_string("HAVEAGREATDAY!", 70)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

# This code prints out the outcome of tilting the bit right

def on_gesture_tilt_right():
    basic.show_string("LOVEYOURSELF!", 70)
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)

# This code prints out the outcome of tilting the bit upside down

def on_gesture_logo_down():
    basic.show_icon(IconNames.FABULOUS)
input.on_gesture(Gesture.LOGO_DOWN, on_gesture_logo_down)

# This code displays the forever loop

def on_forever():
    basic.show_icon(IconNames.HAPPY)
    basic.show_icon(IconNames.HEART)
basic.forever(on_forever)
