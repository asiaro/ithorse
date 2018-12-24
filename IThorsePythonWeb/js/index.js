window.onload = function(){
    var oBtn01 = document.getElementById('btn01');
    var oBtn02 = document.getElementById('btn02');
    var oLink = document.getElementById('link01');

    oBtn01.onclick = function(){
        oLink.href = 'css/skin01.css';
}

    oBtn02.onclick = function(){
        oLink.href = 'css/skin02.css';
}
}
