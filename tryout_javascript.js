console.log("hi");

function randomMsg() {
    
var goodLuckMsgs = ["have a lovely day", "goodluck", "You can do it"];

var randInt = Math.floor(Math.random() * (goodLuckMsgs.length) );


    if(randInt == 0){
        document.getElementById('msg').innerText = goodLuckMsgs[0]
        console.log(goodLuckMsgs[0])
    } else if(randInt == 1){
        document.getElementById('msg').innerText = goodLuckMsgs[1]
        console.log(goodLuckMsgs[1])
    }else{
        document.getElementById('msg').innerText = goodLuckMsgs[2]
        console.log(goodLuckMsgs[2])
    }
}
 document.getElementById('btn').addEventListener('click', randomMsg);  // alternative to adding onclick="randomMsg()" on the html <button> tag

