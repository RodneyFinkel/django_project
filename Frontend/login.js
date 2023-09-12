let form = document.getElementById('login-form')

form.addEventListener('submit', (e) => {
    e.preventDefault()
    
    let formData = {
        'username': form.username.value,
        'password': form.password.value
    }

    fetch('http://127.0.0.1:8000/api/users/token/', {
        method:"POST",
        headers:{
            'Content-Type': 'application/json',

        },
        body:JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => {
        console.log('DATA:', data.access)
        if (data.access){
            localStorage.setItem('token', data.access)
            window.location = 'file://Users/rodneyfinkel/Documents/Documents - Rodney’s MacBook Pro - 1/GitHub 19.43.21/django_project/Frontend/projects-list.html'
        }else{
            alert('Username OR password not correct')
        }
    })
})
