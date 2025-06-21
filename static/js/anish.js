document.addEventListener('DOMContentLoaded', () => {
    const closeBtn = document.querySelector('.close');
    const infoBox = document.querySelector('.info');
    console.log(closeBtn);
    console.log(infoBox);

    if (closeBtn && infoBox) {
        closeBtn.addEventListener('click', function (event) {
            console.log("fdsf");

            infoBox.style.display = 'none';
        });
    }
});

function handleClickRow(data) {
    console.log(data);
    let info = document.querySelector('.info');
    info.style.display = 'block';
    let imgContainer = document.querySelector('.image');
    imgContainer.innerHTML = '';
    let img = document.createElement('img');
    img.src = data.image;
    img.alt = 'image preview';
    img.style.maxWidth = '100%';
    img.style.maxHeight = '400px';
    img.style.border = '2px solid';
    img.style.marginTop = '10px';
    imgContainer.appendChild(img);
    let tagContainer = document.querySelector('.tags-container');
    tagContainer.innerHTML = "";
    let tagList = data.tags.split(',');
    tagList.forEach(tag => {
        let span = document.createElement('span');
        span.textContent = tag.trim();
        span.style.display = 'inline-block';
        span.style.padding = '20px 20px';
        span.style.margin = '5px';
        span.style.borderRadius = '8px';
        span.style.backgroundColor = '#c0decc';
        span.style.fontSize = '14px';
        tagContainer.appendChild(span);
    });
    // console.log(data.subject)
    console.log(data.description)
    let subjectContainer = document.querySelector('.subject-container');
    subjectContainer.innerHTML = data.subject;
    let desContainer = document.querySelector('.desription-container');
    desContainer.innerHTML = data.description;
}

