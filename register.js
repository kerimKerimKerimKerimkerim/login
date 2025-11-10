document.getElementById("registerForm").addEventListener("submit", function(e){
    e.preventDefault();

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    const confirmPassword = document.getElementById("confirmPassword").value;
    const message = document.getElementById("message");

    if(password !== confirmPassword){
        message.style.color = "red";
        message.textContent = "Şifreler eşleşmiyor!";
        return;
    }

    fetch("http://127.0.0.1:5000/register", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({username, password})
    })
    .then(res => res.json())
    .then(data => {
        message.style.color = data.status === "success" ? "green" : "red";
        message.textContent = data.message;
    })
    .catch(err => {
        message.style.color = "red";
        message.textContent = "Sunucu hatası!";
        console.error(err);
    });
});
