//  This code prints out the outcome of pressing A
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    basic.showString("YOUAREENOUGH!", 70)
})
//  This code prints out the outcome of tilting the bit left
input.onGesture(Gesture.TiltLeft, function on_gesture_tilt_left() {
    basic.showArrow(ArrowNames.North)
})
//  This code prints out the outcome of pressing A and B
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    basic.showString("LIVEYOURLIFE! ", 70)
})
//  This code prints out the outcome of pressing B
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    basic.showString("YOUAREYOURSELF!", 70)
})
//  This code prints out the outcome of shaking the micro bit
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    basic.showString("HAVEAGREATDAY!", 70)
})
//  This code prints out the outcome of tilting the bit right
input.onGesture(Gesture.TiltRight, function on_gesture_tilt_right() {
    basic.showString("LOVEYOURSELF!", 70)
})
//  This code prints out the outcome of tilting the bit upside down
input.onGesture(Gesture.LogoDown, function on_gesture_logo_down() {
    basic.showIcon(IconNames.Fabulous)
})
//  This code displays the forever loop
basic.forever(function on_forever() {
    basic.showIcon(IconNames.Happy)
    basic.showIcon(IconNames.Heart)
})
