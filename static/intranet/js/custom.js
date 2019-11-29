
const sidebar_container = document.getElementById("sidebar-container");
const sidebar_overlay = document.getElementById("sidebar-overlay");

// function close_sidebar(){
//     sidebar_overlay.style.display = "none";
//
//     sidebar_container.classList.remove('sidebar-animate-open')
//     sidebar_container.classList.add('sidebar-animate-close')
//     sidebar_container.style.display = "none";
// }
//
// function open_sidebar(){
//     sidebar_container.style.display = "flex";
//     sidebar_overlay.style.display = "flex"
//
//     sidebar_container.classList.remove('sidebar-animate-close')
//     sidebar_container.classList.add('sidebar-animate-open')
// }


$("#show-sidebar").click(function(){
    const width = window.innerWidth

    $("#sidebar-content").css({display :"flex"});
    if (width <= 992) {
        console.log(width)
        $("#sidebar-container").animate({width: "100%"});
    } else if (width > 992 && width <= 1200){
        $("#sidebar-container").animate({width: "30%"});
    } else if (width > 1200){
        $("#sidebar-container").animate({width: "20%"});
    }
    $("#sidebar-overlay").css({display :"flex"});
});

$("#sidebar-overlay").click(function(){
    $("#sidebar-container").animate({width :"0%"});
    $("#sidebar-content").css({display :"none"});
    $("#sidebar-overlay").css({display :"none"});
    $("#show-sidebar").show();
});

$("#sidebar-action-close").click(function(){
    $("#sidebar-container").animate({width :"0%"});
    $("#sidebar-content").css({display :"none"});
    $("#sidebar-overlay").css({display :"none"});
    $("#show-sidebar").show();
});


window.onscroll = function() {makeSticky()};

const navbar = document.getElementById("main-navbar");
const nav_scroller = document.getElementById("nav-scroller");
const sticky = navbar.offsetTop;



function makeSticky() {
    if (window.pageYOffset >= sticky) {
        navbar.classList.add("navbar-sticky-top")
        nav_scroller.classList.add('d-flex')
    } else {
        navbar.classList.remove("navbar-sticky-top");
        nav_scroller.classList.remove('d-flex')
    }
}
