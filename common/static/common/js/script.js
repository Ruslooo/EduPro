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

document.addEventListener('DOMContentLoaded', () => {
    const likeButton = document.querySelector('.like-button');
    const likeCount = document.querySelector('.like-count');

    // Получение сохраненного количества лайков из localStorage
    const savedCount = localStorage.getItem('likeCount');

    // Если сохраненное значение существует, устанавливаем его в likeCount
    if (savedCount) {
        likeCount.textContent = savedCount;
    }

    likeButton.addEventListener('click', () => {
        const currentCount = parseInt(likeCount.textContent, 10);
        likeCount.textContent = currentCount + 1;

        // Обновление отображаемого количества лайков
        likeCount.textContent = newCount;

        // Сохранение нового значения в localStorage
        localStorage.setItem('likeCount', newCount);
    });
});
