window.onload = function () {
    var oInput01 = document.getElementById('input01');
    var oInput02 = document.getElementById('input02');
    var oInput03 = document.getElementById('input03');
    var oInput04 = document.getElementById('input04');
    var oInput05 = document.getElementById('input05');
    var oInput06 = document.getElementById('input06');
    var oInput07 = document.getElementById('input07');
    var oBtn = document.getElementById('setcard');
    var oCard = document.getElementById('card_wrap');

    oBtn.onclick = function () {
        var sVal01 = oInput01.value;
        var sVal02 = oInput02.value;
        var sVal03 = oInput03.value;
        var sVal04 = oInput04.value;
        var sVal05 = oInput05.value;
        var sVal06 = oInput06.value;
        var sVal07 = oInput07.value;

        // 判断输入框不为空
        if (sVal01 == '' || sVal02 == '' || sVal03 == '' || sVal04 == '' || sVal05 == '' || sVal06 == '') {
            alert('输入框不能为空！');
            //结束程序往下执行
            return;
        }

        var sTr = '<div class="p01">' + sVal01 + '<em>' + sVal02 + '</em></div>' +
            '<div class="p02">' +
            '<p class="company">' + sVal03 + '</p>' +
            '<p>手机：' + sVal04 + '</p>' +
            '<p>email：' + sVal05 + '</p>' +
            '<p>地址：' + sVal06 + '</p>' +
            '</div>';

        // 改变名片内容
        oCard.innerHTML = sTr;

        // 改变名片风格
        if (sVal07 == 0) {
            oCard.className = 'idcard01';
        } else if (sVal07 == 1) {
            oCard.className = 'idcard02';
        } else {
            oCard.className = 'idcard03';
        }
    }
}