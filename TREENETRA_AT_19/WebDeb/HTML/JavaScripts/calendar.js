const d = new Date();
const m = d.toLoacleString('default',{moonth:'long'});
const y  = d.getFullYear(),day= d.getDate();
document.getElementById("calendar").innerText='{m} ${y}-${today}';