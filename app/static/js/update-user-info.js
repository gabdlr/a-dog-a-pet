(() => {
    'use strict'
    const personalInformationForm = document.querySelector('#personal-information-form');
    const personalInformationSubmitBtn = personalInformationForm.querySelector('button');
    personalInformationSubmitBtn.disabled = true;
    personalInformationForm.oninput = function (){
        personalInformationSubmitBtn.disabled = false;
    }
})()