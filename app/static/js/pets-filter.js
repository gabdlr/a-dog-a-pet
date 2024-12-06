(() => {
    'use strict'
    const fromYearsFilter = document.querySelector('#from-years-filter');
    const toYearsFilter = document.querySelector('#to-years-filter');
    const toTextSpan = document.querySelector('#to-text');
    fromYearsFilter.addEventListener('change', updateToYearsFilter);
    fromYearsFilter.dispatchEvent(new Event('change'));
    updateToYearsFilterWithQueryParams();
    
    function updateToYearsFilter(event) {
        const startYear = event.target.value;
        if(startYear == 7) {
            toYearsFilter.removeAttribute('name');
            toYearsFilter.classList.add('d-none');
            toTextSpan.classList.add('d-none');
        } else {
            toYearsFilter.setAttribute('name', 'age-to');
            toYearsFilter.classList.remove('d-none');
            toTextSpan.classList.remove('d-none');            
        }

        const option = document.createElement('option');
        option.value = "7";
        option.innerText = "7+";
        option.selected = true;
        toYearsFilter.replaceChildren(option);

        for(let i = 6; i > startYear; i--) {
            const option = document.createElement('option');
            const value = i.toString();
            option.value = value;
            option.innerText = value;
            toYearsFilter.appendChild(option);
        }
        
    }

    function updateToYearsFilterWithQueryParams() {
        let address = window.location.search;
        let parameterList = new URLSearchParams(address)
        let ageToParam = parameterList.get('age-to');
        for (const option of toYearsFilter.children) {
            if (option.value === ageToParam) option.setAttribute("selected","")
        }
    }
})()