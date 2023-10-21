 // Import the functions you need from the SDKs you need
  import { initializeApp } from "https://www.gstatic.com/firebasejs/10.4.0/firebase-app.js";
  import { getAnalytics } from "https://www.gstatic.com/firebasejs/10.4.0/firebase-analytics.js";
  // TODO: Add SDKs for Firebase products that you want to use
  // https://firebase.google.com/docs/web/setup#available-libraries

  // Your web app's Firebase configuration
  // For Firebase JS SDK v7.20.0 and later, measurementId is optional
  const firebaseConfig = {
    apiKey: "AIzaSyBrc1UYBV52Wp3QuGqSvaGTGFuMZi4cQ8A",
    authDomain: "facecomparison.firebaseapp.com",
    projectId: "facecomparison",
    storageBucket: "facecomparison.appspot.com",
    messagingSenderId: "637583581991",
    appId: "1:637583581991:web:6acf4cab54c4083d4b3f02",
    measurementId: "G-DMRS9545VB"
  };

  // Initialize Firebase
  const app = initializeApp(firebaseConfig);
  const analytics = getAnalytics(app);

  document.getElementById('Google').addEventListener('click' , GoogleLogin)


  function GoogleLogin(){
    console.log('Login button call')
  }




//for google enabling

// var provider = new firebase.auth.GoogleAuthProvider();

// firebase.auth().signInWithPopup(provider).then(function(result) {
//    // This gives you a Google Access Token. You can use it to access the Google API.
//    var token = result.credential.accessToken;
//    // The signed-in user info.
//    var user = result.user;
//    // ...
//  }).catch(function(error) {
//    // Handle Errors here.
//    var errorCode = error.code;
//    var errorMessage = error.message;
//    // The email of the user's account used.
//    var email = error.email;
//    // The firebase.auth.AuthCredential type that was used.
//    var credential = error.credential;
//    // ...
//  });

//  firebase.auth().signOut().then(function() {
//    // Sign-out successful.
//  }).catch(function(error) {
//    // An error happened.
//  });


// // Initialize Firebase
// const database = getDatabase(app);
// const analytics = getAnalytics(app);
// const auth = getAuth();
// // Initialize Firebase

// // Google Authentication start
// const Google = document.getElementById("Google");
// const provider = new GoogleAuthProvider();

// Google.addEventListener('click', (e)=>{
//     console.log('Google')
//     e.preventDefault();

//     signInWithPopup(auth, provider)
//   .then((result) => {
//     // This gives you a Google Access Token. You can use it to access the Google API.
//     const credential = GoogleAuthProvider.credentialFromResult(result);
//     const token = credential.accessToken;
//     // The signed-in user info.
//     const user = result.user;
//     // console.log(user);
//     // alert(user.displayName)
//     // alert(user.email)

//     location.href = ("http://127.0.0.1:5000/signup.html");
   
//   }).catch((error) => {
//     // Handle Errors here.
//     const errorCode = error.code;
//     console.log(errorCode);
//     const errorMessage = error.message;
//     alert(errorMessage);
//     // The email of the user's account used.
//     const email = error.customData.email;
//     alert(email)
//     location.href = ("http://127.0.0.1:5000/signup.html");
//     // The AuthCredential type that was used.
//     const credential = GoogleAuthProvider.credentialFromError(error);
//     // ...
//   });
// });
// // Google Authentication end