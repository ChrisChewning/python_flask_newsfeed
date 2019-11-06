function summary(event){
    event.target.parentElement.parentElement.nextElementSibling.firstElementChild.classList.toggle("show")
}

//ADD BUTTON
function show_new_note(event){
    event.target.classList.toggle("hide") //hide this button
    event.target.parentElement.nextElementSibling.classList.toggle("show") //show textarea
    event.target.parentElement.nextElementSibling.nextElementSibling.classList.toggle("hide") //hide delete article
}

function add_new_note(event){
    event.target.form[0].classList.toggle("hide")
}

//EDIT BUTTON
function show_edit_note(event){
    event.target.parentElement.lastElementChild.firstElementChild.lastElementChild.parentElement.classList.toggle("hide") //delete note btn
    event.target.classList.toggle("hide") //edit note button
    event.target.nextElementSibling[0].classList.toggle("show")  //textarea 
    event.target.nextElementSibling[1].classList.toggle("show")  //submit button
    event.target.nextElementSibling[2].classList.toggle("hide")  //
    event.target.nextElementSibling.nextElementSibling.classList.toggle("hide")
    event.target.parentElement.firstElementChild.classList.toggle("hide") //note text
    console.log(event.target)
}
