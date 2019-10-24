
function summary(event){
    event.target.nextElementSibling.nextElementSibling.classList.toggle("show")
    // event.target.previousSibling.previousElementSibling.classList.toggle("show")
    console.log(event.target)
}


function save(event){
    console.log('target, ', event.target)
    console.log(event.target.nextElementSibling.innerHTML)
    // article = Article(article=event.)

    // db.session.add(article)
    // db.session.commit()
}

// function save_article(){
//         console.log('hit')
//         article = Article(waPo_article.link_url)
//         db.session.add(article)
//         db.session.commit()
//         flash('Saved')

    
// }