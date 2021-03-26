window.addEventListener('scroll', function () {
    let header = document.querySelector('header')
    header.classList.toggle('sticky', window.scrollY > 0);
})
function toggleMenu(){
    let toggleM=document.querySelector(".toggle");
    let menu=document.querySelector(".menu");
    
    toggleM.classList.toggle('active')
    menu.classList.toggle('active')
    
}
function toggleMenu2(){
    let float=document.querySelector(".float");
    float.classList.toggle('active2')
}
document.getElementById("submit").addEventListener("click", function(event){
    event.preventDefault()
  });