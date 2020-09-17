this.window.addEventListener('scroll', function() {
    if (this.window.scrollY <= 1000){
        changeFrogSize();
    }
});


function changeFrogSize(){
    var main = this.document.getElementById("main");
    main.style = "margin-top: " + this.window.scrollY + "px;";
//    console.log(this.window.scrollY);
}