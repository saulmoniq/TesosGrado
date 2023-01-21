function sidebar(){
    var hamburger = document.getElementById("hamburguer");
    hamburger.classList.remove("hidden");
}
function closeSidebar(){
    let close = document.getElementById("hamburguer");
    close.classList.add("hidden");
}

function userSidebar(){
    var user = document.getElementById("user");
    user.classList.remove("hidden-user");
}
function closeUserSidebar(){
    let close = document.getElementById("user");
    close.classList.add("hidden-user");
}