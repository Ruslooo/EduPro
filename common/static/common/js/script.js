document.addEventListener("DOMContentLoaded", () => {
    document.addEventListener("click", e => console.log(e.target))
    document.querySelectorAll(".js-trigger-thumbs").forEach(trigger => {
        trigger.addEventListener("click", async (e) => {
            e.stopPropagation();
            if (!e.target.classList.contains("js-trigger-thumbs")) {
                return;
            }

            e.preventDefault();
            const url = e.target.dataset.url;
            await fetch(location.origin + url, {
                method: "GET",
            })
                .then(res => res.json())
                .catch(err => alert("Произошла ошибка"))
                .then(res => {
                    if (res.status) alert(res.message)
                })

        })
    })
})

function show_comments_form(parent_comment_id)
{
    if (parent_comment_id == 'write_comment')
    {
        $("#id_parent_comment").val('')
    }
    else
    {
        $("#id_parent_comment").val(parent_comment_id);
    }
    $("#comment_form").insertAfter("#" + parent_comment_id);
}