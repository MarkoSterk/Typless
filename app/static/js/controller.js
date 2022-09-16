import { resetForm } from "./formUtils.js";
import { sendPdf, saveDataToDb } from "./requestFuncs.js";

const form = document.getElementById("submitForm");
const uploadField = document.getElementById('invoiceUpload');
const processInvoiceBtn = document.getElementById('processInvoice');
const email = document.getElementById('userEmail');
const flashMsg = document.getElementById('flashMsg');
const processedData = document.getElementById('processedData');
const saveDataBtn = document.getElementById('saveProcessedData');
const resetFormBtn = document.getElementById('resetForm');

let saveProcessedData;
let formData = new FormData();
const PROCESS_API_URL = '/api/v1/data/process';
const SAVE_API_URL = '/api/v1/data/save';


uploadField.addEventListener('change', function() {
    formData.append('file', uploadField.files[0])
});

processInvoiceBtn.addEventListener('click', async function(){
    saveProcessedData = await sendPdf(email, formData, processedData, PROCESS_API_URL, processInvoiceBtn, saveDataBtn, resetFormBtn, flashMsg);
})

resetFormBtn.addEventListener('click', function(){
    formData = resetForm(form, formData, processInvoiceBtn, saveDataBtn, resetFormBtn, processedData);
})

saveDataBtn.addEventListener('click', async function() {
    await saveDataToDb(processedData, SAVE_API_URL, saveProcessedData, flashMsg, resetFormBtn);
})

