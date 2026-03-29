var foldBtns = document.getElementsByClassName("fold-button");

for (var i = 0; i < foldBtns.length; i++) {
    foldBtns[i].addEventListener("click", function(e) {
        var post = e.target.parentElement.parentElement;

        if (post.className === "one-post folded") {
            post.className = "one-post";
            e.target.innerHTML = "свернуть";
        } else {
            post.className = "one-post folded";
            e.target.innerHTML = "развернуть";
        }
    });
}
