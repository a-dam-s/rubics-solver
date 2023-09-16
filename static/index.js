const color_map = { 'w': "white", 'y': "yellow", 'b': "blue", 'g': "green", 'r': "red", 'o': "orange", "t": "" }
let current_field = 0
let block = false
let number_of_rotations = 0
let cube = [[], [], [], [], [], []]
$(() => {
let asd
if (window.mobileAndTabletCheck()){
     asd = document.getElementById("getKeyboard")
}
else{
    asd = document
}
$(asd).keydown(function (e) {
    let key = e.key.toLowerCase()
    console.log(key)
    if (['w', 'y', 'b', 'g', 'r', 'o'].includes(key) && !block) {
        addColor(key)
    }

    else if (key == 'enter' && current_field % 4 == 0) {
        console.log("Enter!!!")
        for (let i = 0; i < 4; i++) {
            changeColor(i, "t")
        }
        $("#alert").text("")
        block = false
        number_of_rotations += 1
    }

    else if (key == 'backspace' && (((current_field) % 4) > 0 || block)) {
        console.log("backspace!!!")
        current_field -= 1
        cube[number_of_rotations][current_field % 4] = ""
        block = false
        $("#alert").text("")
        changeColor(current_field % 4, "t")
    }
});

function addColor(color) {
    let alert = ""
    cube[number_of_rotations][current_field % 4] = color
    changeColor(current_field % 4, color)
    current_field += 1
    if (current_field == 24) {
        console.log(cube)
        solve()
    }
    if (current_field % 4 == 0) {
        block = true
        if (number_of_rotations == 0 || number_of_rotations == 4) {
            alert = "Rotate the whole cube upwards <br> <img src='/static/rotate_up.png'>"
        }
        else if (number_of_rotations > 0 && number_of_rotations < 4) {
            alert = "Rotate the whole cube to the left. <br> <img src='/static/rotate_left.png'>"
        }
        else{
            $("#alert").html(alert + "<h3>Calculating...</h3>")
            return
        }
        $("#alert").html(alert + "<br>Press enter to continue")
    }
}

function changeColor(field, color) {
    $("#c" + field).css("background", color_map[color])
}

function solve() {
    console.log(cube)
    two = cube[1]
    three = cube[2]
    four = cube[3]
    one = cube[4]
    cube[1] = one
    cube[2] = two
    cube[3] = three
    cube[4] = four
    zero = cube[5][1]
    one = cube[5][2]
    two = cube[5][3]
    three = cube[5][0]
    cube[5][0] = zero
    cube[5][1] = one
    cube[5][2] = two
    cube[5][3] = three
    scramble = cube.toString().replaceAll(",", "")
    window.location.replace("http://truet0123.eu.pythonanywhere.com/solve/" + scramble);
}})