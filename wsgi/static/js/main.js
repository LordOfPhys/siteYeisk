$(function() {
    var x = document.getElementById("length").innerHTML; 
    var y = document.getElementById("height").innerHTML;
    document.addEventListener("click", function (e) {
        var number = e.target.id;
        var a = Math.floor(number / 10);
        var b = number - a * 10;
        document.getElementById("previous").innerHTML = [a, b];
    });
});