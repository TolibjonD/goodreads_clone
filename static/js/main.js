window.addEventListener("DOMContentLoaded", ()=> {
    // WINDOW SCROLL UP WHILE PAGE LOW DOWN
    up_arrow = document.querySelector(".up__arrow");
    window.addEventListener("scroll", () => {
        if (window.pageYOffset > 100) {
            up_arrow.classList.add("show");
        } else {
            up_arrow.classList.remove("show")
        }
    })

    // SHOW REVIEWS MORE AND LESS
    comment = document.querySelector(".comment");
    if (comment) {
        showMoreBtn = document.querySelector(".comment_more");
    commentText = comment.innerText;
    // RESPONSIVELY SHOWING TEXT
    width = window.innerWidth
    if (width >= 768) {
        commentText = comment.innerText;
        comment.innerText = comment.innerText.slice(0,520);
    } else {
        commentText = comment.innerText;
        comment.innerText = comment.innerText.slice(0,120);
    }
    // ? SHOW FULL COMMENT MORE OR LESS WHEN SHOW BTN CLICK
    showMoreBtn.addEventListener("click", () => {
        if (showMoreBtn.innerText === "show more...") {
            showMoreBtn.innerText = "show less...";
            comment.innerText = commentText
        } else {
            showMoreBtn.innerText = "show more...";
            width = window.innerWidth
            if (width >= 768) {
                commentText = comment.innerText;
                comment.innerText = comment.innerText.slice(0,520);
            } else {
                commentText = comment.innerText;
                comment.innerText = comment.innerText.slice(0,120);
            }
        }
    })
    }


})