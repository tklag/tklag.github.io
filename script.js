/* DOM elements */
const menuBtn = document.getElementById("menu-icon");
const menuBar = document.getElementById("menu-bar");
const menuBarBG = document.getElementById("menu-bar-background");



menuBtn.addEventListener("click", menuCloseOpen);

function menuCloseOpen(){
    if(menuBarBG.style.display === "grid"){
        menuBarBG.style.display = "none";
        menuBtn.style.display = "grid";
    }else{
        menuBarBG.style.display = "grid";
        menuBtn.style.display = "none";
    }
}

