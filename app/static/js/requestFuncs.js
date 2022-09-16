import { removeSpinner, renderSpinner, flashMessage } from "./utilFuncs.js";
import { showPreview } from "./formUtils.js";

export const sendPdf = async (email, formData, parentDiv, PROCESS_API_URL, processInvoiceBtn, saveDataBtn, resetFormBtn, flashMsg) => {
    if(email.value.length > 4){
        formData.append('email', email.value)
    }
    else {
        return flashMessage('Please insert a valid email address', 'danger', flashMsg)
    }

    if(!formData.has('file')){
        return flashMessage('Please upload a valid invoice first!', 'danger', flashMsg)
    }
    let saveProcessedData
    renderSpinner(parentDiv);
    await axios.post(PROCESS_API_URL, formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      }).then(function (response) {
        saveProcessedData = showPreview(response.data, parentDiv);
        processInvoiceBtn.style.display = 'none';
        saveDataBtn.style.display = 'inline';
        resetFormBtn.style.display = 'inline';
      })
      .catch(function (error) {
        removeSpinner(processedData);
        flashMessage('Something went wrong. Please try again later.', 'danger', flashMsg)
      });

      return saveProcessedData
};

export const saveDataToDb = async (parentDiv, SAVE_API_URL, saveProcessedData, flashMsg, resetBtn) => {
    let previewHtml = parentDiv.innerHTML;
    renderSpinner(parentDiv);
    await axios.post(SAVE_API_URL, saveProcessedData, {
        headers: {
          "Content-Type": "application/json",
        },
      }).then(function (response) {
        if(response.data.status == 'success'){
            removeSpinner(parentDiv);
            flashMessage(response.data.message, response.data.status, flashMsg)
            resetBtn.click();
        }
      })
      .catch(function (error) {
        removeSpinner(parentDiv);
        parentDiv.innerHTML = previewHtml;
        flashMessage('Something went wrong. Please try again later.', 'danger', flashMsg)
      }); 
}