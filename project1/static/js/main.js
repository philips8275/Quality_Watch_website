const txtmusic = new Audio("https://www.soundjay.com/buttons/sounds/beep-21.mp3");

document.getElementById("name").addEventListener("click", function () {
    txtmusic.play()
})

document.getElementById("email").addEventListener("click", function () {
    txtmusic.play()
})

document.getElementById("message").addEventListener("click", function () {
    txtmusic.play()
})

function Contact_submit(event) {
    event.preventDefault(); // Stop form from submitting immediately

    Swal.fire({
        title: "Thank You..! For Your Message",
        text: "We will get back to you soon",
        text: "Message sent successfully",
        icon: "success",
        confirmButtonText: "OK"
    }).then((result) => {
        if (result.isConfirmed) {
            txtmusic.play();
            event.target.closest("form").submit();
        }
    });
}

