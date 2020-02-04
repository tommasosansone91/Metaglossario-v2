function get_today_date() {
var now = new Date();
var day = ("0" + now.getDate()).slice(-2);
var month = ("0" + (now.getMonth() + 1)).slice(-2);
var today = now.getFullYear()+"-"+(month)+"-"+(day);
document.getElementById('date_to_turn_into_toda').value = today;
}

