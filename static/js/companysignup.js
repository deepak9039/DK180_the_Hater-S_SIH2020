let form = document.forms.register;

function validateForm()
{
    form.username.setCustomValidity("");
    form.password.setCustomValidity("");
    form.confirm_password.setCustomValidity("");


    
    if(form.username.value.length < 6)
    {
        form.username.setCustomValidity("your username must be 6 characters. ");
    }

    if(form.password.value.length < 8)
    {
        form.password.setCustomValidity("your password must be at least 8 characters. ");
    }

    if(form.password.value != form.confirm_password.value)
    {
        form.confirm_password.setCustomValidity("this password does not match our other password");
    }

}
form.addEventListener("input", validateForm);


