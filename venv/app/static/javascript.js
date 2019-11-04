
function summary(event){
    // event.target.nextElementSibling.firstChild.nextElementSibling.classList.toggle("show")
    // event.target.nextElementSibling.firstElementChild.classList.toggle("show")
    // event.target.parentElement.nextSibling.parentElement.nextElementSibling.classList.toggle("show")
    event.target.parentElement.parentElement.nextElementSibling.firstElementChild.classList.toggle("show")
    console.log(event.target.parentElement.nextSibling.parentElement.nextElementSibling)
    console.log(event.target)
}

function show_new_note(event){
    console.log(event.target)
    console.log(event.target.nextElementSibling.firstElementChild)
    event.target.classList.toggle("hide") //hide this button
    event.target.nextElementSibling[1].classList.toggle("show") //show new button
    event.target.nextElementSibling.firstElementChild.classList.toggle("show") //show textarea
}

function add_new_note(event){
    console.log(event.target.form.nextElementSibling[1])
    event.target.form[0].classList.toggle("hide")
    event.target.form.nextElementSibling[1].classList.toggle("show")
}

function show_edit_note(event){
    console.log(event.target)
    event.target.classList.toggle("hide")
    event.target.nextElementSibling[0].classList.toggle("show")
    event.target.nextElementSibling[1].classList.toggle("show")
}


