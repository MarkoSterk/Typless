export const renderSpinner = (parentDiv) => {
    const markup = `<div style="margin-left: 45%"><div class="loader"></div></div>`;
    parentDiv.innerHTML = '';
    parentDiv.insertAdjacentHTML('afterbegin', markup);
}

export const removeSpinner = (parentDiv) => {
    parentDiv.innerHTML = '';
}

export const removeFlashMsg = (parentDiv) => {
    parentDiv.innerHTML = '';
}

export const flashMessage = (msg, status, parentDiv) => {
    const msgString = `<p class="text-center bg-${status} text-light m-0 p-3">${msg}</p>`

    parentDiv.insertAdjacentHTML('afterbegin', msgString);

    setTimeout(function(){
        removeFlashMsg(parentDiv)
    }, 5000)
}