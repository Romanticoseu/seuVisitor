// ==UserScript==
// @name         seuVisitor
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  一键实现车牌预约，需手动填写信息
// @author       Romanticoseu
// @match        https://infoplus.seu.edu.cn/infoplus/form/*
// @icon         https://www.google.com/s2/favicons?sz=64&domain=seu.edu.cn
// @grant        none
// ==/UserScript==

(function () {
    'use strict';
    let myCarId = ''       //车牌号
    let myDomitory = ''         // 宿舍
    let myDepartmentId = ''         //院系Id
    let myDepartmentName = ''       //院系名称
    let myDaoyuanId = ''            //导员Id
    let myDaoyuanName = ''      //导员姓名
    let myDaoyuanPhone = ''      // 导员电话
    let myReason = ''                   // 入校原因(一卡通+名字)
    function handleCheckbox(checkBoxs) {
        for(let checkBox of checkBoxs) {
            checkBox.click()
        }
    }
    function CompleteForm() {
        // 找到具有指定ID的复选框
        var checkBoxs = []
        var parentIs = document.getElementById("V1_CTRL390")
        var commiment = document.getElementById("V1_CTRL267");
        var campusLonghu = document.getElementById("V1_CTRL274");
        var driverIs = document.getElementById("V1_CTRL215");
        checkBoxs.push(parentIs, commiment, campusLonghu, driverIs)
        handleCheckbox(checkBoxs)

        // 处理文字填充框
        var carId = document.getElementById("V1_CTRL217");
        carId.value = myCarId
        var domitoryArea = document.getElementById("V1_CTRL376");
        domitoryArea.value = myDomitory

        var department = document.getElementById("V1_CTRL377")
        var departmentOption = document.createElement("option");
        departmentOption.value = myDepartmentId
        departmentOption.text = myDepartmentName
        department.appendChild(departmentOption)
        department.value = myDepartmentId

        var daoyuan = document.getElementById("V1_CTRL378")
        var daoyuanOption = document.createElement("option")
        daoyuanOption.value = myDaoyuanId
        daoyuanOption.text = myDaoyuanName
        daoyuan.appendChild(daoyuanOption)
        daoyuan.value = myDaoyuanId
        
        var daoyuanPhone = document.getElementById("V1_CTRL379")
        daoyuanPhone.value = myDaoyuanPhone
        var reason = document.getElementById("V1_CTRL380")
        reason.value = myReason
    }

    window.onload = function () {
        // 在这里编写你想执行的操作
        console.log("网页加载完毕！");
        setTimeout(function () {
            CompleteForm()
        }, 1000);
    };



    // Your code here...
})();