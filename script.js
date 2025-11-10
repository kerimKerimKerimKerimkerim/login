document.getElementById("loginForm").addEventListener("submit", function(e){
    e.preventDefault();

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    const message = document.getElementById("message");

    fetch("data.json")
        .then(response => response.json())
        .then(data => {
            const user = data.find(u => u.username === username && u.password === password);
            if(user){
                message.style.color = "green";
                message.textContent = "Giriş başarılı!";
            } else {
                message.style.color = "red";
                message.textContent = "Kullanıcı adı veya şifre yanlış.";
            }
        })
        .catch(err => {
            message.style.color = "red";
            message.textContent = "Hata: " + err;
        });
});
