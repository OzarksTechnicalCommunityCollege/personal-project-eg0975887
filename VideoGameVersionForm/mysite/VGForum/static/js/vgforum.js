document.addEventListener("DOMContentLoaded", function() {

    const button = document.getElementById("aboutBtn");
    const text = document.getElementById("aboutText");

    button.addEventListener("click", function() {

        if (text.style.display === "block") {
            text.style.display = "none";
        } else {
            text.style.display = "block";
        }

    });

});