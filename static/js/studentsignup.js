// console.log("===============");
// console.log("===============");
// console.log("===============");
// console.log("it is working");
// console.log("===============");
// console.log("===============");



let form = document.forms.register;

function validateForm()
{
    form.username.setCustomValidity("");
    form.password.setCustomValidity("");
    form.conf_password.setCustomValidity("");


    
    if(form.username.value.length < 6)
    {
        form.username.setCustomValidity("your username must be 6 characters. ");
    }

    if(form.password.value.length < 8)
    {
        form.password.setCustomValidity("your password must be at least 8 characters. ");
    }

    if(form.password.value != form.conf_password.value)
    {
        form.conf_password.setCustomValidity("this password does not match our other password");
    }

}
form.addEventListener("input", validateForm);


