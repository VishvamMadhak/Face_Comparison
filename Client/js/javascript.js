function showImage(imageId) {
            
            var fileInput = document.getElementById(imageId.replace("image", "file"));
            var image = document.getElementById(imageId);

            if (fileInput.files && fileInput.files[0]) {
                var reader = new FileReader();
                reader.onload = function (e) {
                    image.style.display = "block";
                    image.src = e.target.result;
                    document.getElementById('compareButton').style.display = "block";
                };
                reader.readAsDataURL(fileInput.files[0]);
            }
        }
function compareButton() {
    var formData = new FormData();

    formData.append('file1', document.getElementById('file1').files[0]);
    formData.append('file2', document.getElementById('file2').files[0]);

    fetch('http://127.0.0.1:5000/dashboard', {
        method: 'POST',
        body: formData 
    })
    .then(response => response.text())
    .then(data => {
        console.log(data);
        document.getElementById('message').textContent = data; 
    })
    .catch(error => console.error(error));
}

function signup() {

    var formData = new FormData();

    formData.append('name' , document.getElementById('name').value);
    formData.append('email' , document.getElementById('email').value);
    formData.append('password' , document.getElementById('password').value);

    fetch('http://127.0.0.1:5000/signup' , {

        method : 'POST' ,
        body : formData
    })
    .then(response => {
        console.log(response)
        if (response.ok)
        {
            window.location.replace("login.html" );
        }
        else {
            console.error('Signup failed');
            document.getElementById('errormsg').textContent = 'Signup failed';
        }
    })
    .then (data => console.log(data))

}

function login() {
    var formData = new FormData();
    formData.append('email', document.getElementById('email').value);
    formData.append('password', document.getElementById('password').value);

    fetch('http://127.0.0.1:5000/login', {
        method: 'POST',
        body: formData
    })
    .then(data => {
        data.json().then(res =>{
            console.log("this is the message" , res);
            let username = encodeURIComponent(res.user_name);
            window.location.replace("dashboard.html?user_name=" +username);
            console.log("Name of the user:" + username);
        }

        )
       
    })
    
    .catch(error => {
        console.error(error);
    });
}




