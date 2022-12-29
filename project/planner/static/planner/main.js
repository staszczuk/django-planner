function switchWeek(weekId) {
    let current = document.getElementsByClassName('week--active')[0];
    if (current != null) {
        current.classList.remove('week--active');
    }
    console.log(weekId);
    document.getElementById(weekId).classList.add('week--active');
}