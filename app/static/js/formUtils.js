import { removeSpinner } from "./utilFuncs.js";

export const showPreview = (data, parentDiv) => {
    let markup = '<div class="bg-dark p-2">';
    markup = markup + '<h3 class="text-light">Invoice preview</h3>'

    for(let field of data.data.extracted_fields){
        //console.log(field.name, field.values[0].value)
        markup = markup + `<p class="text-light">${field.name}: ${field.values[0].value}</p>`
    }
    markup = markup + '</div>'
    removeSpinner(parentDiv);
    parentDiv.insertAdjacentHTML('afterbegin', markup);
    return data.data;
}

export const resetForm = (formFields, formData, processBtn, saveBtn, resetBtn, parentDiv) => {
    formFields.reset();
    formData.delete('file');
    formData.delete('email');

    processBtn.style.display = 'inline'
    saveBtn.style.display = 'none'
    resetBtn.style.display = 'none'

    parentDiv.innerHTML = '';

    return formData;
}