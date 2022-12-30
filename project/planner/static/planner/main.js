function switchWeek(weekId) {
    let visibleCurrent = document.getElementsByClassName('week--visible')[0];
    let visibleNew = document.getElementById(weekId);
    if (visibleCurrent != null) {
        visibleCurrent.classList.remove('week--visible');
        visibleCurrent.classList.add('d-none');
    }
    visibleNew.classList.remove('d-none');
    visibleNew.classList.add('week--visible');
}