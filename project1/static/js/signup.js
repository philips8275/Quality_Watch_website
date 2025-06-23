const txtmusic = new Audio("https://www.soundjay.com/buttons/sounds/beep-21.mp3");


document.getElementById("name").addEventListener("click", function(){
    txtmusic.play()
})

document.getElementById("email").addEventListener("click", function(){
    txtmusic.play()
})

document.getElementById("password").addEventListener("click", function(){
    txtmusic.play()
})

document.getElementById("confirmpassword").addEventListener("click", function(){
    txtmusic.play()
})

document.getElementById("phone").addEventListener("click", function(){
    txtmusic.play()
})

document.getElementById("address").addEventListener("click", function(){
    txtmusic.play()
})

document.getElementById("submit").addEventListener("click", function(){
    txtmusic.play()
})

document.getElementById("reset").addEventListener("click", function(){
    txtmusic.play()
})

function validatePassword() {
    var password = document.getElementById("password").value;
    var confirmPassword = document.getElementById("confirmpassword").value;

    if (password != confirmPassword) {
        alert("Passwords do not match!");
        return false;
    }
    
    return true;
}